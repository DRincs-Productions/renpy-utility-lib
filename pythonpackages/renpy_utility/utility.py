from typing import Optional
import renpy.character as character

__all__ = [
    "isNullOrEmpty",
    "IsNullOrWhiteSpace",
    "all_characters",
]


def isNullOrEmpty(item: Optional[str]) -> bool:
    if not item:
        return True
    return False


def IsNullOrWhiteSpace(item: Optional[str]) -> bool:
    if not item or item.isspace():
        return True
    return False


def os_path_join(a: str, b: str) -> str:
    return a + "/" + b


def all_characters(store) -> list[character.ADVCharacter]:
    my_list: list[character.ADVCharacter] = []
    for item in store.__dict__():
        if isinstance(item, character.ADVCharacter):
            my_list.append(item)
    return my_list
