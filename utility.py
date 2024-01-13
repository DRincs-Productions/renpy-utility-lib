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
    for item in store.__dict__.values():
        if isinstance(item, character.ADVCharacter):
            my_list.append(item)
    return my_list


def get_value_by_character_key(character: character.ADVCharacter, dict: dict):
    if character in dict:
        return dict[character]
    else:
        for key, value in dict.items():
            if str(character) == str(key):
                dict[character] = value
                del dict[key]
                return value
        return None


def set_value_by_character_key(character: character.ADVCharacter, dict: dict, value):
    if character in dict:
        dict[character] = value
    else:
        for key in dict.keys():
            if str(character) == str(key):
                dict[character] = value
                del dict[key]
                return
        dict[character] = value


def del_value_by_character_key(character: character.ADVCharacter, dict: dict):
    if character in dict:
        del dict[character]
    else:
        for key in dict.keys():
            if str(character) == str(key):
                del dict[key]
                return
        return
