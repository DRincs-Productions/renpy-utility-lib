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
    ):
        """Initialize the DRCharacter class."""
        self.character = character
        self.icon = icon

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
