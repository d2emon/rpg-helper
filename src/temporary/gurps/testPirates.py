def showChar(character):
    print(character)
    print("ST\t{}".format(character.ST))
    print("DX\t{}".format(character.DX))
    print("IQ\t{}".format(character.IQ))
    print("HT\t{}".format(character.HT))


def savePC(session):
    import pc
    from pirates.pc import Default, Monk

    rooster = [
        Monk(),
        Default(),
    ]

    for c in rooster:
        showChar(c)
        pc.save(c, session)
    return rooster


def main():
    import sqlalchemy
    print("Версия SQLAlchemy:", sqlalchemy.__version__)
    print("="*80)

    import db
    e, s = db.connect(False)

    import pc
    s.query(pc.PlayerCharacter).delete()
    s.commit()

    rooster = savePC(s)

    import sqlalchemy.orm.exc
    try:
        c = pc.load(s, 10)
        r = c.fill(s, 10)
        print(r)
    except sqlalchemy.orm.exc.NoResultFound:
        print("No result")

    chars = [pc.load(s, c.id) for c in rooster]
    for c in chars:
        print("="*80)
        c.afterLoad()

        thrust = c.ST.thrust()
        swing = c.ST.swing()

        print("-"*80)
        print("LOAD:")
        showChar(c)

        print("Thrust\t{}".format(thrust))
        print("Swing\t{}".format(swing))

        print("-"*80)
        print("SAVED:")
        print(c)

        print("="*80)

    showChar(chars[0])
    

if __name__ == "__main__":
    main()
