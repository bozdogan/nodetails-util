def progress_line(done, all, bar_length=60, show_percentage=True):
    done = min(max(0, done), all)
    if done == 0:
        ratio = 0
    elif all == 0:
        ratio = 1
    else:
        ratio = done/all
    filled_cells = int(ratio*bar_length)
    
    bar = "[{full}{empty}]".format(full="#"*filled_cells,
                                   empty="-"*(bar_length - filled_cells))
    items = " %s/%s" % (done, all)
    percent = " %s%%" % int(ratio*100)

    erase_line = "\b"*(len(bar) + len(f" {all}/{all}"))
    bar_line = bar + items
    if show_percentage:
        erase_line += "\b"*len(" 888%")
        bar_line += percent
    
    print(erase_line, end="")
    print(bar_line, end="", flush=True)


if __name__ == "__main__":
    import time
    
    for i in range(100):
        time.sleep(.1)
        progress_line(i + 1, 100)
    
    print()
