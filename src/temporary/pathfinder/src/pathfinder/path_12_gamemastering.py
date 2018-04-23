def encounters(levels=[]):
    c = len(levels)
    if c > 0:
        apl = round(sum(levels) / float(c))
    else:
        apl = 0

    if c >= 6:
        apl += 1
    elif c <= 3:
        apl -= 1

    print("{} / {} = {}".format(sum(levels), c, apl))


def getCR(id=0):
    import yaml

    filename = "db/path/encounters.yml"
    data = []
    with open(filename) as f:
        obj = yaml.load(f)
    data = obj.get("design", [])[id]
    print(data.get("title"))
    print(data)
    print(obj)
