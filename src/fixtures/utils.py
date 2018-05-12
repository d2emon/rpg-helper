def filldata(c, data=[]):
    for fixture in data:
        if fixture is None:
            continue
        model = c.load_fixture(fixture)
        db.session.add(model)
    db.session.commit()
    print("Filled")
    return


def showdata(c, data=[]):
    for fixture in data:
        if fixture is None:
            continue
        model = c.load_fixture(fixture)
        print(model)
    print("Filled")
