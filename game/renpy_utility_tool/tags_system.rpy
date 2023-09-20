default cur_tags_enabled = []

label update_tags:
    if renpy.has_label("update_tags_enabled"):
        call update_tags_enabled
        python:
            if not isinstance(cur_tags_enabled, list[str]):
                cur_tags_enabled = []
    else:
        $ cur_tags_enabled = []
    return
