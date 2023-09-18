from typing import Optional
import renpy as renpy

__all__ = [
    "DRCharacter",
]


class DRCharacter:
    """DR Character class."""

    def __init__(
        self,
        character: renpy.character.ADVCharacter,
        icon: str,
        info_screen: Optional[str] = None,
    ):
        """Initialize the DRCharacter class."""
        self.character = character
        self.icon = icon
        self.info_screen = info_screen

    @property
    def character(self) -> renpy.character.ADVCharacter:
        """Character."""
        return self._character

    @character.setter
    def character(self, value: renpy.character.ADVCharacter):
        self._character = value

    @property
    def icon(self) -> str:
        """Icon."""
        return self._icon

    @icon.setter
    def icon(self, value: str):
        self._icon = value

    @property
    def info_screen(self) -> Optional[str]:
        """Info screen. For https://github.com/DRincs-Productions/DS-toolkit"""
        return self._info_screen

    @info_screen.setter
    def info_screen(self, value: Optional[str]):
        self._info_screen = value
