class Card:
    title = "UNTITLED"
    activeDefense = "Any"
    movement = "None"

    def getHitBonus(self):
        return 0

    def isWildSwing(self):
        return False


class Nothing(Card):
    title = "Do Nothing"


class Attack(Card):
    title = "Attack"
    movement = "Step. You may step and attack, or attack and then step. To move further and still attack, take All-Out Attack or Move and Attack."

    def isWildSwing(self):
        print("\tIf you move more than 1 hex and attack with a hand weapon, it is a Wild Swing; can’t make a wild impaling attack at more than 1 hex distance")
        print("\tCannot target specific hit locations (use the Random Location table if needed)")
        print("\tSkill is at -5, the current darkness penalty, or 9, whichever is lowest")
        return True


class Move(Card):
    title = "Move"
    movement = "Full Movement"


class Ready(Card):
    title = "Ready"
    movement = "Step"


class AllOutAttack(Attack):
    title = "All-Out Attack"
    activeDefense = "You may make no active defenses at all until your next turn."
    movement = "You may move up to half your Move, but you can only move forward."

    def getHitBonus(self):
        print("\ta)\tTwo attacks against the same foe if you have two readied weapons or one weapon that does not have to be readied after use")
        print("\tb)\tOne feint and one attack")
        print("\tc)\tA single attack at +4 to hit")
        print("\td)\tA single attack doing +2 damage if successful")
        return 0


class AllOutDefense(Card):
    title = "All-Out Defense"
    activeDefense = "You may choose any legal active defense, with bonuses as described above."
    movement = "If you choose Increased Dodge, you may move up to half your Move. Otherwise, the only movement you may take is a step."
