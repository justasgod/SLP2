def options(arg):
    if arg.islist():
        count = 0
        for i in arg:
            if i % 2 == 0:
                count += 1
            if i < 0:
                arg.remove(i)
        return max(arg), count, arg
    elif arg.isdictionary():
        sort_dict = dict(sorted(arg.items(), key=lambda item: item[1]))
        return sort_dict
    elif arg.isfinite():
        if arg < 0:

    else:
        pass

