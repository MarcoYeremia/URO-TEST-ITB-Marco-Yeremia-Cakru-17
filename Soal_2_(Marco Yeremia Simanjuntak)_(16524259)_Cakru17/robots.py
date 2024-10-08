import random

def main():
    robotz = picking_bots()
    robots_battle(robotz)


def picking_bots():
    bots = []
    provided_bots = ["Sagebot", "Botofsteel", "Onepunchbot"]
    print("1. Sagebot\nHP = 350\nDamage = 30 - 50")
    print("1. Botofsteel\nHP = 450\nDamage = 20 - 30")
    print("1. Onepunchbot\nHP = 300\nDamage = 40 - 60\n")
    print("expect an answer of the robot name, ex: 'Sagebot'")
    while True:
        bot1 = input("pick your first robot: ").title()
        if bot1 in provided_bots:
            bots.append(bot1)
            while True:
                bot2 = input("pick your second robot: ").title()
                if bot2 in provided_bots:
                    bots.append(bot2)
                    return bots
                else:
                    print("ain't no bot like that over here mate")

        else:
            print("no such bot exist pal")





def robots_battle(botsz):
    database = [
                {"bot" : "Sagebot", "HP": 300},
                {"bot" : "Botofsteel", "HP": 450},
                {"bot" : "Onepunchbot", "HP": 250},
                ]
    input("\nshall we begin?? (click anything)")
    print(f"\nlet the battle of {botsz[0]} and {botsz[1]} begins!!\n")
    input("(click anything)")
    hps = []
    for bots in database:
        if botsz[0] == bots["bot"]:
            hp1 = bots["HP"]
            hps.append(hp1)
    for bots in database:
        if botsz[1] == bots["bot"]:
            hp2 = bots["HP"]
            hps.append(hp2)




    hpone = hps[0]
    hptwo = hps[1]
    i = 1
    while hpone > 0 and hptwo > 0:
        print(f"round {i}\n")
        damage1 = produce_damage(botsz[0])
        damage2 = produce_damage(botsz[1])

        print(f"HP {botsz[0]} = {hpone}")
        print(f"HP {botsz[1]} = {hptwo}")

        print(f"\n{botsz[0]} deals {damage1} damage\n")
        input("(click anything)\n")
        hptwo = hptwo - damage1
        if hptwo <= 0:
            print(f"{botsz[1]} is defeated\n{botsz[0]} wins!")
            break

        print(f"{botsz[1]} deals {damage2} damage\n")
        input("(click anything)\n")
        hpone = hpone - damage2
        if hpone <= 0:
            print(f"{botsz[0]} is defeated\n{botsz[1]} wins!")
            break
        i += 1




def produce_damage(bot):
    if bot == "Sagebot":
        damage = random.randint(30, 50)
        return damage
    elif bot == "Botofsteel":
        damage = random.randint(20, 30)
        return damage
    elif bot == "Onepunchbot":
        damage = random.randint(40, 60)
        return damage


if __name__ == "__main__":
    main()
