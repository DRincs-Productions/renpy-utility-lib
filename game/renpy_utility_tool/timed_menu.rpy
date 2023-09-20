init python:
    import time

screen countdown(timer_range, not_click_label):
    default end_time = time.time() + timer_range
    default current_time = time.time()
    timer 0.05 repeat True action If(
        current_time < end_time, 
        true=SetScreenVariable('current_time', time.time()), 
        false=[Hide('countdown'), Call(label_call)]
    )
    # We have default dissolve in and dissolve out transform
    bar value (end_time-current_time)*100 range timer_range*100 xalign 0.5 yalign 0.9 xmaximum 300 at notify_appear 
