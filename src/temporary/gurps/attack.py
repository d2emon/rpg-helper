import environment
import person


class Attack:
    skill = 10

    personal = 1
    target = 1
    rangedMod = 1
    wildSwing = True
    ranged = True
    opportunity = False
    aiming = True
    SS = 20
    SSpenalty = -4
    acc = 2
    fireGroup = False
    miss1 = False
    missile = True
    dodge = False
    knockback = True
    vitals = False
    dmgEffects = True
    hp = 1

    def __init__(self):
        self.environment = environment.Environment()
        self.attacker = person.Attacker()

    def p1(self):
        wpnSkl = self.attacker.weaponSkill
        mdfEnv = self.environment.getCombatModifier()
        mdfPrs = self.attacker.getPersonalCombatModifier()

        print("1. Start with unmodified weapon skill and go to [2]")
        print("\tSkill:\t{}".format(wpnSkl))
        print("2. Apply all environmental modifiers - for bad footing (B107), darkness (B92), etc - and go to [3]")
        print("\tEnvironment:\t{}".format(mdfEnv))
        print("3. Apply all personal modifiers - for attacking on the move (B117), with your off hand (B13) or while using an unfamiliar weapon (B43); attacking with an All Out Attack or a Wild Swing (B105); attacking using a weapon in close combat (B111); and for your position (B203), shock from wounds (B126), etc - and go to [4]")
        print("\tPersonal:\t{}".format(mdfPrs))

        skill = wpnSkl
        skill += mdfEnv
        skill += mdfPrs
        print("\tTotal skill:\t{}".format(skill))
        # self.skill = 200

        print("4. If the attack is a Wild Swing or a randomly-targeted blow (B109), go on to [5]; otherwise, skip to [6].")
        if self.wildSwing:
            self.doWildSwing()

        skill += self.target
        print("6. Apply all target modifiers - for cover (B118) and obstructing figures (B117), hit location (CII53), relative elevation (B123), size (B201), striking into a close combat (B114), etc ({}). - and go to [7].".format(self.skill))
        print("7. If the attack is a ranged attack, go to [8]; otherwise, go immediately to [14]")
        if self.ranged:
            self.doRanged()

        self.doMakeRoll()

    def doWildSwing(self):
        print("5. Roll for hit location (B203 or CII53); go to [6].")

    def doRanged(self):
        self.skill += self.rangedMod
        print("8. Apply all special ranged combat modifiers, including the Speed/Range modifier (B201) modified for both elevation and erratic movement (B117), and any applicable Rcl penalties (B119); ({}) and go on to [9]".format(self.skill))

        print("9. If this attack is opportunity fire taken while watching more than 1 hex (B118) or if it is a pop-up attack (B116), apply the appropriate penalty and go to [12]; otherwise, go to [10]")
        if self.opportunity:
            self.doSnapShot()
        else:
            print("10. Did you take at least 1 turn to aim (B116) or are you aiming successive groups from an automatic weapon (B121)? If so, go to [13]; otherwise go on to [11].")
            if self.aiming:
                self.doAimedShot()
            else:
                self.doRegularShot()

    def doRegularShot(self):
        print("11. Is your modified skill({}) greater than the SS number({}) of your weapon (B115)? If so, skip to [14]; otherwise continue on to [12]".format(self.skill, self.SS))
        if self.skill <= self.SS:
            self.doSnapShot()

    def doSnapShot(self):
        self.skill += self.SSpenalty
        print("12. Apply a Snap Shot (B115) penalty of -4 ({}) (or less, for some UT weapons) and go directly to [14]".format(self.SSpenalty))

    def doAimedShot(self):
        self.skill += self.acc
        print("13. Apply the Acc bonus of your weapon (B115)({}), including any bonuses for high-tech sights or scopes (CII31), and an extra +1 per additional turn of aiming - or per additional group fired from an automatic weapon, if aiming successive groups - to a maximum additional +3. Add +1 more if you are braced. Now go on to [14].".format(self.skill))

    def doMakeRoll(self):
        roll = (self.skill >= 20)
        print("14. Roll against your modified skill to hit. This can be no greater than 9 if this attack is a Wild Swing or an attack against the wrong target (B114, B117, B119). Note the result. If the skill roll succeeds, go immediately to [21] (note that a group from an automatic weapon can hit with more than one bullet - see B120); otherwise, continue on to [15]")
        if roll:
            self.doHit()
        else:
            self.doMiss()

    def doMiss(self):
        crit = False
        print("15 Did the attack critically miss (B110)? If so, go on to [16]; otherwise, go to [17]..")
        if crit:
            self.doCritMiss()
        else:
            self.doRegularMiss()

    def doCritMiss(self):
        disarm = False
        selfattack = False
        print("16. Roll on the appropriate Critical Miss Table (B202) and note the result. Apply any immediate effects. If you dropped, broke, or disabled your weapon, go to [52]. If you hit yourself, you are now the target of your attack; go to [28] and assess the damage. Otherwise, go to [19].")
        if disarm:
            self.p52()
        else:
            if selfattack:
                self.p28()
            else:
                self.p19()

    def doRegularMiss(self):
        missByOne = True
        print("17. Did the attack miss by only one? If so, proceed to [18]; if not go to [19]")
        if missByOne:
            self.p18()
        else:
            self.p19()

    def p18(self):
        print("18. If you were firing a group of three or more rounds from an automatic weapon (B120), a miss by 1 still hits with one round; go to [23]. If your target was a hit location that lists a \"Miss by 1\" result (CII53), you have hit this new location instead; again, proceed to [23]. Otherwise go to [19]")
        if self.fireGroup:
            self.p23()
        else:
            if self.miss1:
                self.doRegularHit()
            else:
                self.p19()

    def p19(self):
        print("19. Was the attack a missile weapon, or aimed into close combat? If so, proceed to [20]; if not, go to [52].")
        if self.missile:
            self.skill = 100
            print("20. Check to see if you have hit the wrong target. Start with the target nearest to you on a miss with a missile (B117), the first target behind your intended target on a missile attack that was dodged (B119), or with a random target if striking into a close combat (B114). Return to [1] and attack your new target. Your final modified skill cannot exceed 9.")
            self.p1()
        else:
            self.p52()

    def doHit(self):
        crit = False
        print("21.Did the attack critically hit (B109)? If so, go to [22]; otherwise, move on to [23].")
        if crit:
            self.doCritHit()
        else:
            self.doRegularHit()

    def doCritHit(self):
        print("22. Roll on the appropriate Critical Hit Table (B202) and note the result - (note that this applies to one round in a group if firing an automatic weapon). Apply any immediate effects, then go immediately to [28].")
        self.p28()

    def doRegularHit(self):
        roll = False
        print("23. The target rolls his active defense, modified for his position (B203), stunning (B127), the angle of the attack (-2 from the side, B108, or above, B124), relative elevation (B123), retreating (B109), and for any feints (B105) or wounds (B126) that took place since his last turn. If the target did an All-Out Attack, or was attacked by surprise, he gets only his PD. Parries have their own unique modifiers (see modifiers sheet and B99). If the defense roll fails, go to [26]. Otherwise, go to [24]")
        if not roll:
            self.p26()
        else:
            self.p24()

    def p24(self):
        crit = False
        print("24.Did the target critically succeed on his active defense (non-ranged attacks only)? If so, go immediately to [16]. Otherwise, go on to [25].")
        if crit:
            self.p16()
        else:
            self.p25()

    def p25(self):
        print("25. Was the target's active defense a Dodge? If so, go to [19]; otherwise, go to [52].")
        if self.dodge:
            self.p19()
        else:
            self.p52()

    def p26(self):
        crit = True
        print("26. Did the target critically fail on his active defense? If so, go to [27]. If not, go to [28].")
        if crit:
            self.p27()
        else:
            self.p28()

    def p27(self):
        print("27. If the target Dodged, he falls down. If he Blocked, his shield is now unready. If he Parried, he goes to the Critical Miss Table (B202). Go to [28].")
        self.p28()

    def p28(self):
        print("28. A HIT! Roll the basic damage for your weapon (B73). A bullet, or a cutting or impaling weapon, can never do less than 1 hit of damage. Natural attacks and crushing attacks can do 0 damage. Go to [29].")
        self.p29()

    def p29(self):
        print("29. Modify the damage result for extra damage - from an All Out Attack (B105), the target's Vulnerability disads, etc- and multiply it by any multiplier that was given on the Critical Hit Table, or any multiplier for a special ammunition type (CII55) that applies before DR. Go to [30].")
        self.p30()

    def p30(self):
        print("30. If the attack is impaling, a bullet or any other attack that does not inflict knockback (B106), go to [33]; otherwise, continue on to [31].")
        if not self.knockback:
            self.p33()
        else:
            self.p31()

    def p31(self):
        damage = 16
        hexes = damage / 8
        print("31. Apply 1 hex of knockback for every 8 points of damage you have rolled. If the target is knocked back at least 1 hex, go to [32]; otherwise, go on to [33].")
        if hexes >= 1:
            self.p32()
        else:
            self.p33()

    def p32(self):
        print("32. The target must roll versus DX or fall down. Continue on to [33].")
        self.p33()

    def p33(self):
        print("33. Apply any armor divisors - for armor-piercing bullets, shaped-charge rounds, monowire, etc.- to the target's DR at the hit location you have hit, using the DR that applies to the attack in question (e.g., Kevlar is less effective versus impaling attacks). Now go on to [34].")
        self.p34()

    def p34(self):
        dr = 0
        print("34. Subtract the modified DR of step [33] from the damage rolled in step [29]; if the result is greater than 0, go immediately to [36]. If the result is exactly 0 (0 or less if you are attacking with a bullet), go immediately to [35]. In all other cases, go to [53].")
        if dr > 0:
            self.p36()
        else:
            if dr == 0:
                self.p35()
            else:
                self.p53()

    def p35(self):
        damage = 1
        print("35. If your target is wearing flexible armor (like Kevlar), then for each 6 rolled on the damage dice, you inflict 1 hit of blunt trauma (B211). This is treated just like an ordinary crushing attack. If damage was inflicted, go immediately to [36]. If your target was the brain, head (including the nose or jaw) or vitals (including groin or kidneys), go immediately to [39]. Otherwise, go to [53].")
        if damage >= 1:
            self.p36()
        else:
            if self.vitals:
                self.p39()
            else:
                self.p53()

    def p36(self):
        print("36. Multiply your damage by any bonus damage modifiers (B74) for your attack type - cutting or impaling weapons, special ammo types, etc. If the hit location you have hit specifies a damage multiplier for your attack type, use this instead (CII53). Go to [37].")
        self.p37()

    def p37(self):
        print("37. If the hit location that you have hit is subject to blow-through (B109, CII53) from your weapon type, reduce the damage to the appropriate blow-through limit and proceed to [38].")
        self.p38()

    def p38(self):
        print("38. Subtract the final damage from the target's hit points. The target will have a shock (B126) penalty equal to this final damage on all DX- based and IQ-based skills next turn. Go to [39].")
        self.p39()

    def p39(self):
        print("39. Does the hit location in question have any special damage effects (see Hit Locations, CII53)? If so, go to [40]; otherwise, go to [41].")
        if self.dmgEffects:
            self.p40()
        else:
            self.p41()

    def p40(self):
        death = False
        print("40. Follow any special rules for special damage effects such as stunning, k n o c k o u t , crippling, or instant death. See CII53 for the effects of hitting certain hit locations; see B126-127 for the definition of these terms. If the foe suffers instant death as a result, go to [56]; otherwise, go to [41].")
        if death:
            self.p56()
        else:
            self.p41()

    def p41(self):
        halfHT = True
        print("41. Was the damage inflicted greater than the target's HT/2? If so, go to [42]; otherwise, go to [44]")
        if halfHT:
            self.p42()
        else:
            self.p44()

    def p42(self):
        print("42. The target is stunned (B127). He must roll versus HT to recover on his turn. Go to [43].")
        self.p43()

    def p43(self):
        print("43. The target must roll vs. HT or suffer knockdown (B127). Go to [44].")
        self.p44()

    def p44(self):
        print("44. If the target has 4 or more hit points left, go to [54]. If he has 3 or fewer hit points left, go to [45].")
        if self.hp >= 4:
            self.p54()
        else:
            self.p45()

    def p45(self):
        print("45. The target now has half his usual Move and Dodge scores (B126). Go to [46].")
        self.p46()

    def p46(self):
        newHP = 0
        print("46. If your attack caused your target's hit points to fall to 0 or less, go to [47]. Otherwise, go to [48].")
        if newHP <= 0:
            self.p47()
        else:
            self.p48()

    def p47(self):
        print("47. The target must roll versus HT (plus or minus any Strong or Weak Will) or fall unconscious, and must roll again each turn until healed to above 0 hit points. See B126 for details. Go to [48].")
        self.p48()

    def p48(self):
        doubled = True
        print("48. If your attack reduced the target's hit points to -HT or less, go to [49]; otherwise, go to [55]")
        if doubled:
            self.p49()
        else:
            self.p55()

    def p49(self):
        failHT = True
        print("49. The target must roll vs. HT or die, once at -HT and once again for each further -5 points (B126). He need only do this once, ever, at each threshold. If he fails any of these HT rolls, go to [56]; otherwise, go to [50].")
        if failHT:
            self.p56()
        else:
            self.p50()

    def p50(self):
        killed = False
        print("50. If your attack reduced the target's hit points to -5xHT (B126), go to [56]. Otherwise, go to [51].")
        if killed:
            self.p56()
        else:
            self.p51()

    def p51(self):
        print("51. The foe is critically injured. END.")

    def p52(self):
        print("52. You have missed. END.")

    def p53(self):
        print("53. The blow hits, but has no effect on the target. Unless you were attacking for the purpose of simply touching the foe (as a mage or psi may wish to)...END")

    def p54(self):
        print("54. The foe is slightly injured. END")

    def p55(self):
        print("55. The foe is severely injured. END.")

    def p56(self):
        print("56. The foe is dead. END.")

    def run(self):
        self.p1()
