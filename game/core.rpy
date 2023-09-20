define config.log = "log.txt"

label after_load:
    # renpy-utility-lib
    $ update_flags()
    call update_current_flags
    return
