x = [4, "Warner", 1, "Barclay", 5, "Dad", 25]

def draw_stars(y):
    for e in y:
        if isinstance(e, int):
            print "*" * e
        else:
            z = len(e)
            print e[:1].lower() * z
    return "complete"

draw_stars(x)
