# globalPlugins/askOpenRouter/__init__.py

# Copyright(C) 2026-2028 Abdel <abdelkrim.bensaid@gmail.com>
# Released under GPL 2
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from collections.abc import Callable
import scriptHandler
import config
import wx
import addonHandler
import globalPluginHandler
import gui
import typing
from typing import Any, cast
from .dialogs import addonSummary, OpenRouterSettingsPanel, ChatDialog
from gui.settingsDialogs import NVDASettingsDialog
from .functions import disableInSecureMode

addonHandler.initTranslation()

_: Callable[[str], str]


@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = addonSummary

	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)

		# Use cast(Any) to prevent reportUnknownMemberType on config.conf.spec
		conf_any = cast(Any, config.conf)
		if "askOpenRouter" not in conf_any.spec:
			conf_any.spec["askOpenRouter"] = {
				"apiKey": "string(default='')",
				"fullHistory": "boolean(default=True)",
				"useAllModels": "boolean(default=False)",
				"selectedModel": "string(default='')",
			}

		gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(
			OpenRouterSettingsPanel,
		)

	@typing.override
	def terminate(self) -> None:
		if OpenRouterSettingsPanel in gui.settingsDialogs.NVDASettingsDialog.categoryClasses:
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(
				OpenRouterSettingsPanel,
			)

	def onChatDialog(self, evt: Any) -> None:
		# Guard against Optional (MainFrame | None) type on gui.mainFrame
		mainFrame = gui.mainFrame
		if mainFrame is None:
			return

		mainFrame.prePopup()
		dialog = ChatDialog(mainFrame)
		dialog.Show()
		mainFrame.postPopup()

	@scriptHandler.script(
		# Translators: Description of the script which opens the interaction dialog box with OpenRouter.
		description=_("Opens a dialog allowing the user to ask questions to OpenRouter"),
		gesture="kb:control+alt+a",
	)
	def script_openRouterDialog(self, gesture: Any) -> None:
		wx.CallAfter(self.onChatDialog, None)

	@scriptHandler.script(
		# Translators: Description of the script which allows to create a new chat.
		description=_("Opens the prompt to start a new OpenRouter chat."),
	)
	def script_newChat(self, gesture: Any) -> None:
		mainFrame = gui.mainFrame
		if mainFrame is None:
			return
		dialog = ChatDialog(mainFrame)
		dialog.onNew(cast(wx.CommandEvent, None))

	@scriptHandler.script(
		# Translators: Description of the script which allows to continue an existing chat.
		description=_("Opens the prompt to continue an existing OpenRouter chat."),
	)
	def script_continueChat(self, gesture: Any) -> None:
		mainFrame = gui.mainFrame
		if mainFrame is None:
			return
		dialog = ChatDialog(mainFrame)
		dialog.onContinue(cast(wx.CommandEvent, None))

	@scriptHandler.script(
		# Translators: Description of the script which allows to show OpenRouter settings panel..
		description=_("Opens the add-on settings panel."),
	)
	def script_showOpenRouterSettingsPanel(self, gesture: Any) -> None:
		mainFrame = gui.mainFrame
		if mainFrame is None:
			return

		# Use cast(Any) to bypass the partially unknown type of popupSettingsDialog
		cast(Any, mainFrame).popupSettingsDialog(
			NVDASettingsDialog,
			OpenRouterSettingsPanel,
		)
