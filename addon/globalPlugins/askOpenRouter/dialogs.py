# pyright: reportUnusedCallResult=false
# globalPlugins/askOpenRouter/dialogs.py

# Copyright(C) 2026-2028 Abdel <abdelkrim.bensaid@gmail.com>
# Released under GPL 2

from collections.abc import Callable
import typing
from typing import Any, cast
import wx
import addonHandler
import config
import gui

from gui.settingsDialogs import SettingsPanel
from .functions import askOpenRouter, inputBox, getAvailableModels

addonHandler.initTranslation()

_: Callable[[str], str]
addonSummary: str = cast(str, cast(Any, addonHandler).getCodeAddon().manifest["summary"])


# Chat Dialog
class ChatDialog(wx.Dialog):
	"""
	Dialog for managing OpenRouter chat sessions.

	Allows the user to:
		- Start a new chat
		- Continue an existing chat
		- Close the dialog
	"""

	_instance: "ChatDialog | None" = None

	def __new__(cls, *args: Any, **kwargs: Any) -> "ChatDialog":
		if not ChatDialog._instance:
			return super().__new__(cls, *args, **kwargs)
		return ChatDialog._instance

	def __init__(self, parent: wx.Window) -> None:
		"""
		Initialize the ChatDialog.

		Args:
			parent (wx.Window): Parent window.
		"""
		if ChatDialog._instance is not None:
			return

		ChatDialog._instance = self

		super().__init__(
			parent,
			# Translators: Title of the dialog box.
			title=_("Chat Manager"),
		)

		mainSizer: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper: gui.guiHelper.BoxSizerHelper = gui.guiHelper.BoxSizerHelper(
			self,
			wx.VERTICAL,
		)

		buttonGroup: gui.guiHelper.ButtonHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)

		self.newButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: Prompt label to create a new chat.
			label=_("C&reate a New Chat"),
		)

		self.continueButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: Prompt label to continue an existing chat.
			label=_("Co&ntinue a Chat"),
		)

		self.closeButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: Label of the closing button.
			label=_("&Close"),
		)

		self.newButton.SetDefault()
		self.SetEscapeId(self.closeButton.GetId())

		self.newButton.Bind(wx.EVT_BUTTON, self.onNew)  # type: ignore
		self.continueButton.Bind(wx.EVT_BUTTON, self.onContinue)  # type: ignore
		self.Bind(wx.EVT_BUTTON, self.onClose, self.closeButton)  # type: ignore

		sHelper.addItem(buttonGroup)

		mainSizer.Add(  # type: ignore
			sHelper.sizer,
			border=gui.guiHelper.BORDER_FOR_DIALOGS,
			flag=wx.ALL | wx.EXPAND,
		)

		self.SetSizerAndFit(mainSizer)
		self.newButton.SetFocus()

	def __del__(self) -> None:
		ChatDialog._instance = None

	def onClose(self, evt: wx.CommandEvent) -> None:
		"""
		Close the dialog and reset the singleton instance.
		"""
		ChatDialog._instance = None
		self.Destroy()

	def onNew(self, evt: wx.CommandEvent) -> None:
		"""
		Start a new OpenRouter chat.
		"""
		inputBox(
			# Translators: Title of the dialog box to start a new chat.
			_("New Chat"),
			askOpenRouter,
		)

	def onContinue(self, evt: wx.CommandEvent) -> None:
		"""
		Continue an existing OpenRouter chat.
		"""
		inputBox(
			# Translators: Title of the dialog box to continue an existing chat.
			_("Continue Chat"),
			askOpenRouter,
			new=False,
		)


# Settings Panel
class OpenRouterSettingsPanel(SettingsPanel):
	"""
	NVDA settings panel for configuring OpenRouter integration.

	This panel allows the user to:
		- Enter and store their OpenRouter API key
		- Toggle visibility of the API key
		- Enable full chat history display
		- Enable selection of all available models (free and paid)
		- Choose a specific model sorted by price
	"""

	title: str = addonSummary

	@typing.override
	def makeSettings(self, sizer: wx.Sizer) -> None:
		"""
		Build the settings UI components.

		Args:
			sizer (wx.Sizer): Parent sizer provided by NVDA.
		"""
		self.sHelper: gui.guiHelper.BoxSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=sizer)

		# =========================
		# API KEY
		# =========================

		self.apiKeyLabel: wx.StaticText = wx.StaticText(
			self,
			# Translators: Label of the field that must contain the OpenRouter API key.
			label=_("OpenRouter API Key:"),
		)
		self.sHelper.addItem(self.apiKeyLabel)

		self.apiKeyHidden: wx.TextCtrl = wx.TextCtrl(
			self,
			style=wx.TE_PASSWORD,
		)
		self.sHelper.addItem(self.apiKeyHidden, flag=wx.EXPAND)

		# OpenRouter configuration dictionary
		conf_dict = cast(dict[str, Any], config.conf["askOpenRouter"])

		self.apiKeyHidden.SetValue(
			cast(str, conf_dict["apiKey"]),
		)

		self.apiKeyVisible: wx.TextCtrl = wx.TextCtrl(self)
		self.sHelper.addItem(self.apiKeyVisible, flag=wx.EXPAND)
		self.apiKeyVisible.Hide()

		self.showApiKeyCheckBox: wx.CheckBox = wx.CheckBox(
			self,
			# Translators: Label of the checkbox to display the OpenRouter API key.
			label=_("Show API key"),
		)
		self.sHelper.addItem(self.showApiKeyCheckBox)

		self.showApiKeyCheckBox.Bind(  # type: ignore
			wx.EVT_CHECKBOX,
			self.onToggleApiVisibility,
		)

		# =========================
		# FULL HISTORY
		# =========================

		self.fullHistoryCheckBox: wx.CheckBox = wx.CheckBox(
			self,
			# Translators: Label of the checkbox to display chat history.
			label=_("Display the full chat history for continuous discussions"),
		)
		self.sHelper.addItem(self.fullHistoryCheckBox)

		self.fullHistoryCheckBox.SetValue(
			cast(bool, conf_dict["fullHistory"]),
		)

		# =========================
		# USE ALL MODELS
		# =========================

		self.useAllModelsCheckBox: wx.CheckBox = wx.CheckBox(
			self,
			# Translators: Label of the checkbox to show the list of models, including paid ones.
			label=_("Use all models, including paid ones."),
		)
		self.sHelper.addItem(self.useAllModelsCheckBox)

		self.useAllModelsCheckBox.SetValue(
			cast(bool, conf_dict.get("useAllModels", False)),
		)

		self.useAllModelsCheckBox.Bind(  # type: ignore
			wx.EVT_CHECKBOX,
			self.onToggleModelsList,
		)

		# =========================
		# MODELS LIST
		# =========================

		self.modelsList: wx.ListBox = wx.ListBox(self)
		self.sHelper.addItem(self.modelsList, flag=wx.EXPAND)

		self.modelsList.Hide()
		self.modelsData: list[dict[str, object]] = []

		wx.CallAfter(self.onToggleModelsList, None)

	def onToggleApiVisibility(self, evt: wx.CommandEvent) -> None:
		"""
		Toggle visibility of the API key field.
		"""
		if self.showApiKeyCheckBox.IsChecked():
			self.apiKeyVisible.SetValue(self.apiKeyHidden.GetValue())
			self.apiKeyHidden.Hide()
			self.apiKeyVisible.Show()
			self.apiKeyVisible.SetFocus()
		else:
			self.apiKeyHidden.SetValue(self.apiKeyVisible.GetValue())
			self.apiKeyVisible.Hide()
			self.apiKeyHidden.Show()
			self.apiKeyHidden.SetFocus()

		self.Layout()

	def onToggleModelsList(self, evt: wx.CommandEvent | None) -> None:
		"""
		Show or hide the models list depending on checkbox state.
		"""
		if self.useAllModelsCheckBox.IsChecked():
			self.modelsList.Show()
			self._loadModelsIfNeeded()
		else:
			self.modelsList.Hide()

		self.Layout()

	def _loadModelsIfNeeded(self) -> None:
		"""
		Load available models from OpenRouter if required.

		Models are sorted by ascending prompt price.
		"""
		if not self.useAllModelsCheckBox.IsChecked():
			return

		if self.modelsData:
			return

		apiKey: str = self.getApiKeyValue().strip()

		if not apiKey:
			return

		try:
			models: list[dict[str, object]] = getAvailableModels(apiKey)
		except Exception:
			return

		models.sort(key=lambda m: cast(float, m["promptPricing"]))

		self.modelsData = models

		displayNames: list[str] = []

		for m in models:
			price: float = cast(float, m["promptPricing"])
			priceLabel: str = "FREE" if price == 0 else f"{price}$"
			displayNames.append(f"{m['id']} ({priceLabel})")

		self.modelsList.Set(displayNames)

		conf_dict = cast(dict[str, Any], config.conf["askOpenRouter"])
		savedModel: str = cast(str, conf_dict.get("selectedModel", ""))

		for index, m in enumerate(models):
			if m["id"] == savedModel:
				self.modelsList.SetSelection(index)
				break

	def getApiKeyValue(self) -> str:
		"""
		Return the currently entered API key.

		Returns:
			str: API key value.
		"""
		if self.showApiKeyCheckBox.IsChecked():
			return self.apiKeyVisible.GetValue()
		return self.apiKeyHidden.GetValue()

	@typing.override
	def onSave(self) -> None:
		"""
		Save settings into NVDA configuration.
		"""
		conf_dict = cast(dict[str, Any], config.conf["askOpenRouter"])

		conf_dict["apiKey"] = self.getApiKeyValue().strip()
		conf_dict["fullHistory"] = self.fullHistoryCheckBox.GetValue()
		conf_dict["useAllModels"] = self.useAllModelsCheckBox.GetValue()

		index: int = self.modelsList.GetSelection()

		if index != wx.NOT_FOUND and self.modelsData:
			conf_dict["selectedModel"] = self.modelsData[index]["id"]
