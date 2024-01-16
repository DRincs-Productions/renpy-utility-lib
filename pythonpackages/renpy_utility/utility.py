from typing import Optional
import renpy.character as character

__all__ = [
    "isNullOrEmpty",
    "IsNullOrWhiteSpace",
    "all_characters",
    "get_value_by_character_key",
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


def is_equal_characters(
    character1: Optional[character.ADVCharacter],
    character2: Optional[character.ADVCharacter],
):
    if character1 is None or character2 is None:
        return False
    elif character1 is character2:
        return True
    elif str(character1) == str(character2):
        return True
    return False


def get_value_by_character_key(character: character.ADVCharacter, dict: dict):
    if character in dict:
        return dict[character]
    else:
        for key, value in dict.items():
            if is_equal_characters(character, key):
                dict[character] = value
                del dict[key]
                return value
        return None


def set_value_by_character_key(character: character.ADVCharacter, dict: dict, value):
    if character in dict:
        dict[character] = value
    else:
        for key in dict.keys():
            if is_equal_characters(character, key):
                dict[character] = value
                del dict[key]
                return
        dict[character] = value


def del_value_by_character_key(character: character.ADVCharacter, dict: dict):
    if character in dict:
        del dict[character]
    else:
        for key in dict.keys():
            if is_equal_characters(character, key):
                del dict[key]
                return
        return


def find_character_into_list(
    character: character.ADVCharacter, list: list[character.ADVCharacter]
):
    for i in range(len(list)):
        if is_equal_characters(character, list[i]):
            list[i] = character
            return list[i]
    return None
