
    global status
    status = "BEGIN"
    while status == "BEGIN":
        if pattern == "RED":
            status = red(brightness) #returns DONE_RED
        elif pattern == "RAINBOW":
            while status != "DONE":
                if status != "BEING":
                    status == "BEGIN"
                else:
                    time.sleep(1/1000)