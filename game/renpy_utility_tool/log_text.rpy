init -999 python:
    if not "error_notify" in locals() | globals():
        error_notify = __("There is an {color=#f00}{b}ERROR{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    if not "warn_notify" in locals() | globals():
        warn_notify = __("There is an {color=#f5bc02}{b}WARN{/b}{/color}. Please send the developer the logs found in: {color=#00ccff}[config.log]{/color}")
    if not "info_notify" in locals() | globals():
        info_notify = False
