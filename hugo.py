import logging
from typing import Optional, Dict, Any
from pathlib import Path

import sublime
import sublime_plugin


logger = logging.getLogger(__name__)


def plugin_loaded() -> None:
    print("plugin_loaded!")
    logger.info("test")


def plugin_unloaded() -> None:
    print("plugin_unloaded!")
    logger.info("test")


class Listener(sublime_plugin.EventListener):
    def on_exit(self) -> None:
        print("on_exit")

    def on_post_window_command(self, window: sublime.Window, command_name: str, args: Optional[Dict[str, Any]]) -> None:
        print(f"on_post_window_command: {command_name}")


class HugoBuildCommand(sublime_plugin.TextCommand):
    def run(self, _: sublime.Edit) -> None:
        window = self.view.window()
        if window is None:
            return
        project_data = window.project_data()
        project_file_name = window.project_file_name()
        if project_data is None or project_file_name is None:
            return
        folders = project_data["folders"]
        if not folders:
            return
        paths_relative_to = Path(project_file_name).parent
        for folder in folders:
            project_folder = paths_relative_to.joinpath(folder["path"]).absolute()
            config_toml = project_folder.joinpath("config.toml")
            if config_toml.is_file():
                print(config_toml)
