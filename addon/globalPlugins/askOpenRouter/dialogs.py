# globalPlugins/askOpenRouter/dialogs.py

# Copyright(C) 2026-2028 Abdel <abdelkrim.bensaid@gmail.com>
# Released under GPL 2
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import wx
import addonHandler
import config
import gui
from typing import Callable

from gui.settingsDialogs import SettingsPanel
from .functions import askOpenRouter, inputBox

addonHandler.initTranslation()

_: Callable[[str], str]
addonSummary = addonHandler.getCodeAddon().manifest["summary"]


class ChatDialog(wx.Dialog):
	"""
	Dialog for managing OpenRouter chat.

	Allows the user to:
		- Start a new chat
		- Continue an existing chat
		- Close the dialog
	"""

	_instance = None

	def __new__(cls, *args, **kwargs):
		if not ChatDialog._instance:
			return super().__new__(cls, *args, **kwargs)
		return ChatDialog._instance

	def __init__(self, parent: wx.Window) -> None:
		"""
		Initialize the chat dialog.

		Creates buttons for new chat, continue, and close,
		and sets up layout and event bindings.

		Args:
			parent (wx.Window): Parent window for the dialog.
		"""
		if ChatDialog._instance is not None:
			return
		ChatDialog._instance = self
		super().__init__(
			parent,
			# Translators: The title of the chat dialog.
			title=_("Chat Manager")
		)

		mainSizer: wx.BoxSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper: gui.guiHelper.BoxSizerHelper = gui.guiHelper.BoxSizerHelper(self, wx.VERTICAL)

		buttonGroup: gui.guiHelper.ButtonHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)

		# Buttons
		self.newButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: Message informing the user that he's creating a new chat.
			label=_("C&reate a New Chat")
		)

		self.continueButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: Message informing the user that hi's continuing a chat.
			label=_("Co&ntinue a Chat")
		)

		self.closeButton: wx.Button = buttonGroup.addButton(
			self,
			# Translators: A button to close the dialog.
			label=_("&Close")
		)

		# Default button (Enter)
		self.newButton.SetDefault()

		# Escape closes the dialog
		self.SetEscapeId(self.closeButton.GetId())

		# Bind events
		self.newButton.Bind(wx.EVT_BUTTON, self.onNew)
		self.continueButton.Bind(wx.EVT_BUTTON, self.onContinue)
		self.Bind(wx.EVT_BUTTON, self.onClose, self.closeButton)

		sHelper.addItem(buttonGroup)

		mainSizer.Add(
			sHelper.sizer,
			border=gui.guiHelper.BORDER_FOR_DIALOGS,
			flag=wx.ALL | wx.EXPAND
		)

		self.SetSizerAndFit(mainSizer)
		self.onRun()

	def __del__(self):
		ChatDialog._instance = None

	def onClose(self, evt):
		del ChatDialog._instance
		self.Destroy()

	def onRun(self) -> None:
		"""
		Set initial focus when the dialog runs.

		Returns:
			None
		"""
		self.newButton.SetFocus()

	def onNew(self, evt: wx.CommandEvent) -> None:
		"""
		Start a new OpenRouter chat.

		Opens an input box for a new chat.
		"""
		inputBox(
			# Translators: Title of the dialog box for creating a new chat with OpenRouter.
			_("New Chat"),
			askOpenRouter
		)
		return

	def onContinue(self, evt: wx.CommandEvent) -> None:
		"""
		Continue an existing OpenRouter chat.

		Opens an input box for continuing a chat.
		"""
		inputBox(
			# Translators: Title of the dialog box for continuing a chat with OpenRouter.
			_("Continue Chat"),
			askOpenRouter,
			new=False
		)
		return


class OpenRouterSettingsPanel(SettingsPanel):
	"""
	NVDA settings panel for configuring OpenRouter integration.

	This panel allows the user to:
		- Enter and store their OpenRouter API key
		- Toggle visibility of the API key field
		- Enable or disable full chat history display
	"""

	title: str = addonSummary

	def makeSettings(self, settingsSizer: wx.Sizer) -> None:
		"""
		Build the settings UI components.

		Creates:
			- API key input field (hidden and visible modes)
			- Show/hide API key checkbox
			- Full chat history checkbox
		"""
		self.sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)

		# API key label
		self.apiKeyLabel: wx.StaticText = wx.StaticText(
			self,
			# Translators: A field to enter the OpenRouter API key.
			label=_("OpenRouter API Key:")
		)
		self.sHelper.addItem(self.apiKeyLabel)

		# Hidden (password) field
		self.apiKeyHidden: wx.TextCtrl = wx.TextCtrl(self, style=wx.TE_PASSWORD)
		self.sHelper.addItem(
			self.apiKeyHidden,
			flag=wx.EXPAND
		)

		# Load saved API key
		self.apiKeyHidden.SetValue(config.conf["askOpenRouter"]["apiKey"])

		# Visible field
		self.apiKeyVisible: wx.TextCtrl = wx.TextCtrl(self)
		self.sHelper.addItem(
			self.apiKeyVisible,
			flag=wx.EXPAND
		)

		# Hide visible field initially
		self.apiKeyVisible.Hide()

		# Show/hide checkbox
		self.showApiKeyCheckBox: wx.CheckBox = wx.CheckBox(
			self,
			# Translators: A checkbox to show the API key.
			label=_("Show API key")
		)
		self.sHelper.addItem(
			self.showApiKeyCheckBox
		)
		self.showApiKeyCheckBox.Bind(wx.EVT_CHECKBOX, self.onToggleApiVisibility)

		# Full history checkbox
		self.fullHistoryCheckBox: wx.CheckBox = wx.CheckBox(
			self,
			# Translators: A checkbox to choose whether to display the full history in the responses.
			label=_("Display the full chat history for continuous discussions")
		)
		self.sHelper.addItem(
			self.fullHistoryCheckBox
		)

		# Load saved setting
		self.fullHistoryCheckBox.SetValue(
			config.conf["askOpenRouter"]["fullHistory"]
		)

	def onToggleApiVisibility(self, evt: wx.CommandEvent) -> None:
		"""
		Toggle visibility of the API key input field.

		Switches between password-masked and visible text modes.

		Args:
			evt (wx.CommandEvent): Checkbox event.

		Returns:
			None
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

	def getApiKeyValue(self) -> str:
		"""
		Retrieve the current API key value from the appropriate field.

		Returns:
			str: The API key entered by the user.
		"""
		if self.showApiKeyCheckBox.IsChecked():
			return self.apiKeyVisible.GetValue()
		return self.apiKeyHidden.GetValue()

	def onSave(self) -> None:
		"""
		Save the settings to NVDA configuration.

		Stores:
			- API key (trimmed)
			- Full history preference
		"""
		keyValue: str = self.getApiKeyValue()

		config.conf["askOpenRouter"]["apiKey"] = keyValue.strip()
		config.conf["askOpenRouter"]["fullHistory"] = (
			self.fullHistoryCheckBox.GetValue()
		)
