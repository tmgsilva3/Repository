def descending_order(num):
    descending = "".join(sorted(str(num), reverse=True))
    return int(descending)
