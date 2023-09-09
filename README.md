# Ren'Py Utility Library

Ren'Py Utility Library is DRincs Productions's library for Ren'Py, used into all our renpy project.

* Flags: Is a library for Ren'Py to manage flags. ( Read more into the Wiki )
* Logs: Is a my Log system for Ren'Py, wen you use it, you can see the log into the console, file and Notification. ( Read more into the Wiki )
* Notification: Is a library for Notification for Ren'Py. ( Read more into the Wiki )
* Character Disct: Is my solution for know all the character in the game, and add more information about them. ( Read more into the Wiki )
* There are function for improve the code, like: IsNullOrWhiteSpace...

## Install
You can install this library manually: download the zip and extract it in your project folder.
But I recommend you to use git submodule:
```bash
git submodule add -b python-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'pythonpackages/renpy_utility'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'game/renpy_utility_tool'
```

**AND** create a empty file `__init__.py` into pythonpackages `pythonpackages/` so `pythonpackages/__init__.py`.

## Update new version
```bash
git submodule update --init --recursive
```
