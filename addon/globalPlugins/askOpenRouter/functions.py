# globalPlugins/askOpenRouter/functions.py

# Copyright(C) 2026-2028 Abdel <abdelkrim.bensaid@gmail.com>
# Released under GPL 2
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import wx
import os
import addonHandler
import pickle
import random
import markdown
import json
import config
import ui
import gui
import urllib.request
import urllib.error
import time
from typing import List, Dict, Callable, Optional
addonHandler.initTranslation()


_: Callable[[str], str]

# Temporary in-memory blacklist for unavailable models
_unavailableModels: Dict[str, float] = {}

# Cooldowns (seconds)
_RATE_LIMIT_COOLDOWN: int = 300      # 429
_POLICY_COOLDOWN: int = 180         # 404
_PAYMENT_COOLDOWN: int = 1800       # 402


def saveModel(model: str, filename: str) -> None:
	"""
	Save the selected model identifier to a text file.

	Args:
		model (str): Model identifier to save.
		filename (str): Destination file path.

	Returns:
		None
	"""
	with open(filename, "w", encoding="utf-8") as f:
		f.write(model)


def loadModel(filename: str) -> str:
	"""
	Load a model identifier from a text file.

	Args:
		filename (str): Path to the model file.

	Returns:
		str: Model identifier if the file exists, otherwise an empty string.
	"""
	if os.path.exists(filename):
		with open(filename, "r", encoding="utf-8") as f:
			return f.read()
	return ""


def saveHistory(history: List[Dict[str, str]], filename: str) -> None:
	"""
	Serialize and save conversation history to disk.

	Args:
		history (List[Dict[str, str]]): Conversation messages.
		filename (str): Destination file path.

	Returns:
		None
	"""
	with open(filename, "wb") as f:
		pickle.dump(history, f)


def loadHistory(filename: str) -> List[Dict[str, str]]:
	"""
	Load serialized conversation history from disk.

	Args:
		filename (str): Path to history file.

	Returns:
		List[Dict[str, str]]: Loaded conversation history, or an empty list.
	"""
	if os.path.exists(filename):
		with open(filename, "rb") as f:
			return pickle.load(f)
	return []


def _cleanupUnavailableModels() -> None:
	"""
	Remove expired entries from the temporary model blacklist.

	Returns:
		None
	"""
	currentTime: float = time.time()

	expired = [
		model for model, expiry in _unavailableModels.items()
		if currentTime > expiry
	]

	for model in expired:
		del _unavailableModels[model]


def _markModelUnavailable(model: str, errorCode: int) -> None:
	"""
	Mark a model as temporarily unavailable based on error code.

	Args:
		model (str): Model identifier.
		errorCode (int): HTTP error code received.

	Returns:
		None
	"""
	currentTime: float = time.time()

	if errorCode == 429:
		cooldown = _RATE_LIMIT_COOLDOWN
	elif errorCode == 404:
		cooldown = _POLICY_COOLDOWN
	elif errorCode == 402:
		cooldown = _PAYMENT_COOLDOWN
	else:
		cooldown = _RATE_LIMIT_COOLDOWN

	_unavailableModels[model] = currentTime + cooldown


def getRandomFreeModel(apiKey: str) -> str:
	"""
	Retrieve a random free model from OpenRouter.

	Filters:
		- Zero pricing (prompt and completion)
		- Not deprecated
		- Has provider and context length
		- Not temporarily blacklisted

	Args:
		apiKey (str): OpenRouter API key.

	Returns:
		str: A valid free model identifier.

	Raises:
		RuntimeError: If no free model is currently available.
		urllib.error.URLError: If network request fails.
	"""
	_cleanupUnavailableModels()

	modelsURL: str = "https://openrouter.ai/api/v1/models"

	headers: Dict[str, str] = {
		"Authorization": f"Bearer {apiKey}",
		"User-Agent": "Python-urllib",
	}

	req = urllib.request.Request(modelsURL, headers=headers, method="GET")

	with urllib.request.urlopen(req) as response:
		data = json.loads(response.read().decode("utf-8"))

	models = data["data"]

	candidates: List[str] = [
		m["id"]
		for m in models
		if float(m.get("pricing", {}).get("prompt", 1)) == 0
		and float(m.get("pricing", {}).get("completion", 1)) == 0
		and not m.get("deprecated", False)
		and m.get("top_provider")
		and m.get("context_length")
		and m["id"] not in _unavailableModels
	]

	if not candidates:
		# Translators: Message informing that no free model is available.
		raise RuntimeError(_("No free model currently available."))

	return random.choice(candidates)


def _sendRequest(url: str, headers: Dict[str, str], data: Dict) -> str:
	"""
	Send an HTTP POST request to OpenRouter.

	Args:
		url (str): Endpoint URL.
		headers (Dict[str, str]): HTTP headers.
		data (Dict): JSON payload.

	Returns:
		str: Assistant response text.

	Raises:
		urllib.error.HTTPError: If HTTP request fails.
		urllib.error.URLError: If network error occurs.
	"""
	body: bytes = json.dumps(data).encode("utf-8")
	req = urllib.request.Request(url=url, data=body, headers=headers, method="POST")

	with urllib.request.urlopen(req) as response:
		responseData = response.read()

	result = json.loads(responseData.decode("utf-8"))
	return result["choices"][0]["message"]["content"]


def markdownToHtml(markdownText: str) -> str:
	"""
	Convert Markdown text into HTML.

	This function creates a fresh Markdown parser instance
	and converts the provided Markdown string into HTML.

	Args:
		markdownText (str): Text containing Markdown formatting.

	Returns:
		str: Converted HTML string.
	"""
	if not markdownText:
		return ""

	md = markdown.Markdown()
	return md.convert(markdownText)


def getHistory(filename: str) -> str:
	"""
	Convert stored conversation history into formatted HTML.

	Reads the serialized conversation history file and converts it
	into formatted HTML using Markdown.

	Args:
		filename (str): Path to the serialized history file.

	Returns:
		str: HTML-formatted conversation history,
		or an empty string if no history exists.
	"""
	historyLines: List[str] = []
	allChat: List[Dict[str, str]] = []
	# Translators: Message announcing what the user said.
	userQuestion: str = _('You said:')
	# Translators: Message announcing what the model responded.
	modelResponse: str = _('Model replied:')

	if os.path.exists(filename):
		with open(filename, "rb") as f:
			allChat = pickle.load(f)

	if not allChat:
		return ""

	for message in allChat:
		role = message.get("role")
		content = message.get("content", "")

		if role == "user":
			historyLines.append(f"# {userQuestion}")
			historyLines.append(content)
		elif role == "assistant":
			historyLines.append(f"# {modelResponse}")
			historyLines.append(content)

	markdownText: str = "\n".join(historyLines)
	return markdownToHtml(markdownText)


def askOpenRouter(prompt: str, apiKey: str, new: bool = True) -> None:  # noqa: C901
	"""
	Send a prompt to OpenRouter with intelligent retry handling.

	Automatically retries with different free models if:
		- HTTP 402 (payment required)
		- HTTP 404 (policy/endpoint issue)
		- HTTP 429 (rate limit)

	Args:
		prompt (str): User input text.
		apiKey (str): OpenRouter API key.
		new (bool, optional): Whether to start a new conversation.

	Returns:
		None
	"""
	url: str = "https://openrouter.ai/api/v1/chat/completions"

	addonPath: str = addonHandler.getCodeAddon().path
	historyFile: str = os.path.join(addonPath, "open_router_history.pkl")
	modelFile: str = os.path.join(addonPath, "model.txt")

	if new:
		if os.path.exists(historyFile):
			os.remove(historyFile)
		if os.path.exists(modelFile):
			os.remove(modelFile)

	model: str = loadModel(modelFile)

	if not model:
		try:
			model = getRandomFreeModel(apiKey)
			saveModel(model, modelFile)
		except RuntimeError:
			ui.browseableMessage(
				# Translators: Message informing that no free models are available.
				_("No free model available at the moment."),
				# Translators: Title of the error message.
				title=_("Model Error")
			)
			return

	history: List[Dict[str, str]] = loadHistory(historyFile)

	history.append({
		"role": "user",
		"content": prompt
	})

	headers: Dict[str, str] = {
		"Authorization": f"Bearer {apiKey}",
		"Content-Type": "application/json",
		"HTTP-Referer": "http://localhost",
		"X-Title": "My question"
	}

	data: Dict = {
		"model": model,
		"messages": history
	}

	maxAttempts: int = 5
	attempt: int = 0
	answer: Optional[str] = None

	while attempt < maxAttempts:
		try:
			answer = _sendRequest(url, headers, data)
			break

		except urllib.error.HTTPError as e:
			if e.code in (402, 404, 429):
				_markModelUnavailable(model, e.code)

				try:
					model = getRandomFreeModel(apiKey)
					saveModel(model, modelFile)
					data["model"] = model
				except RuntimeError:
					break

				attempt += 1
				time.sleep(0.5)
			else:
				ui.browseableMessage(
					f"HTTP Error: {e.code}, {e.read().decode('utf-8')}",
					# Translators: Title of the error message.
					title=_("HTTP Error")
				)
				return

		except urllib.error.URLError as e:
			ui.browseableMessage(
				# Translators: Network error message.
				message=f"{_('Network error:')} {e.reason}",
				title="Network Error"
			)
			return

	if not answer:
		ui.browseableMessage(
			# Translators: Message informing that no free models are available at the moment.
			_("All free models are currently unavailable. Please try again later."),
			# Translators: Title of the error message.
			title=_("Model Unavailable")
		)
		return

	history.append({
		"role": "assistant",
		"content": answer
	})

	saveHistory(history, historyFile)

	answerHtml: str = markdownToHtml(answer)
	if config.conf["askOpenRouter"]["fullHistory"]:
		messageToDisplay: str = getHistory(historyFile)
	else:
		messageToDisplay = answerHtml

	ui.browseableMessage(
		message=messageToDisplay,
		# Translators: Title of the model response message.
		title=_("Model Response"),
		isHtml=True,
		copyButton=True
	)


def inputBox(
		title: str,
		func: Callable[[str, str, bool], None],
		new: bool = True
) -> None:
	"""
	Display a multiline input dialog and send the result to the given function.

	This dialog allows the user to enter a prompt that will be sent
	to OpenRouter using the provided function.

	Args:
		title (str): Dialog window title.
		func (Callable[[str, str, bool], None]):
			Function to call with parameters (prompt, apiKey, new).
		new (bool, optional):
			Whether to start a new conversation. Defaults to True.

	Returns:
		None
	"""
	if gui.message.isModalMessageBoxActive():
		return
	dialog: wx.TextEntryDialog = wx.TextEntryDialog(
		gui.mainFrame,
		# Translators: Message inviting the user to enter his question.
		_("Please enter the question you want to ask OpenRouter"),
		title,
		style=wx.TE_MULTILINE | wx.OK | wx.CANCEL
	)

	def callback(result: int) -> None:
		if result == wx.ID_OK:
			if not dialog.Value.strip():
				gui.messageBox(
					# Translators: Message informing the user that the field is empty, he must fill it in.
					message=_("You did not enter anything. Please try again."),
					# Translators: Title of the error message.
					caption=_("Input Error")
				)
				return

			apiKey: str = config.conf["askOpenRouter"]["apiKey"]

			if not apiKey.strip():
				gui.messageBox(
					# Translators: Message informing the user that no API key is configured.
					message=_("No API key is configured. Please configure it in settings."),
					# Translators: Title of the error message.
					caption=_("Configuration Error")
				)
				return

			func(
				dialog.Value,
				apiKey,
				new
			)

	gui.runScriptModalDialog(dialog, callback)
