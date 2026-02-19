# globalPlugins/askOpenRouter/__init__.py

# Copyright(C) 2026-2028 Abdel <abdelkrim.bensaid@gmail.com>
# Released under GPL 2
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import scriptHandler
import config
import wx
import addonHandler
import globalPluginHandler
import gui
from typing import Callable
from .dialogs import addonSummary, OpenRouterSettingsPanel, ChatDialog
from gui.settingsDialogs import NVDASettingsDialog
from .functions import disableInSecureMode

addonHandler.initTranslation()

_: Callable[[str], str]


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = addonSummary

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		if "askOpenRouter" not in config.conf.spec:
			config.conf.spec["askOpenRouter"] = {
				"apiKey": "string(default='')",
				"fullHistory": "boolean(default=True)"
			}

		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(
			OpenRouterSettingsPanel
		)

	def terminate(self) -> None:
		if OpenRouterSettingsPanel in gui.settingsDialogs.NVDASettingsDialog.categoryClasses:
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(
				OpenRouterSettingsPanel
			)

	def onChatDialog(self, evt):
		gui.mainFrame.prePopup()
		dialog = ChatDialog(gui.mainFrame)
		dialog.Show()
		gui.mainFrame.postPopup()

	@scriptHandler.script(
		# Translators: Description of the script which opens the interaction dialog box with OpenRouter.
		description=_("Opens a dialog allowing the user to ask questions to OpenRouter"),
		gesture="kb:control+alt+a",
	)
	def script_openRouterDialog(self, gesture):
		wx.CallAfter(self.onChatDialog, gui.mainFrame)

	@scriptHandler.script(
		# Translators: Description of the script which allows to create a new chat.
		description=_("Opens the prompt to start a new OpenRouter chat."),
	)
	def script_newChat(self, gesture):
		dialog = ChatDialog(gui.mainFrame)
		dialog.onNew(None)

	@scriptHandler.script(
		# Translators: Description of the script which allows to continue an existing chat.
		description=_("Opens the prompt to continue an existing OpenRouter chat."),
	)
	def script_continueChat(self, gesture):
		dialog = ChatDialog(gui.mainFrame)
		dialog.onContinue(None)

	@scriptHandler.script(
		# Translators: Description of the script which allows to show OpenRouter settings panel..
		description=_("Opens the add-on settings panel."),
	)
	def script_showOpenRouterSettingsPanel(self, gesture):
		gui.mainFrame.popupSettingsDialog(
			NVDASettingsDialog,
			OpenRouterSettingsPanel
		)
