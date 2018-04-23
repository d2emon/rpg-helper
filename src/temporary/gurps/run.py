class HT:
    def __init__(self, val):
        self.value = val

    def current(self, val):
        if val > 3:
            print(val)
            return val
        if val > 0:
            print("1/2 Move/Dodge")
            return val
        if val > -self.value:
            print("Each turn roll vs. HT +/- Strong/Weak Will.")
            print("Success: act normally")
            print("Failure: unconscious")
            return val
        if val > -5 * self.value:
            print("Roll vs. HT (no Strong/Weak Will), first at –HT then at every further –5 thereafter.")
            print("Success: act normally")
            print("Failure: death")
            return val
        print("Automatic Death")
        return 0


def main():
    import dice
    import random
    import cards
    import environment
    import attack

    print("="*80)
    e = environment.Environment()
    e.footing = dice.byPercent({50: True, 100: False})
    e.darkness = random.randint(-10, 10)
    e.report()
    print("-"*80)

    a = attack.Attack()
    a.environment = e

    card = cards.Nothing()
    print(card.title)
    print("-"*80)
    # a.run()
    # print("-"*80)

    card = cards.Attack()
    print(card.title)
    print("-"*80)
    a.attacker.card = card
    a.run()
    print("-"*80)

    card = cards.Move()
    print(card.title)
    print("-"*80)
    # a.run()
    # print("-"*80)

    card = cards.Ready()
    print(card.title)
    print("-"*80)
    # a.run()
    # print("-"*80)

    card = cards.AllOutAttack()
    print(card.title)
    print("-"*80)
    a.attacker.card = card
    a.run()
    print("-"*80)

    card = cards.AllOutDefense()
    print(card.title)
    print("-"*80)
    # a.run()
    # print("-"*80)

    ht = HT(10)
    print("-"*80)
    ht.current(10)
    print("-"*80)
    ht.current(2)
    print("-"*80)
    ht.current(0)
    print("-"*80)
    ht.current(-12)
    print("-"*80)
    ht.current(-50)
    print("="*80)


if __name__ == "__main__":
    main()
