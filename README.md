Flags
Logs
Notification
Character Disct

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
