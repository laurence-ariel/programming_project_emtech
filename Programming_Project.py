class Hacker:
    def __init__(self, name = input("Enter Player Hacker's Name:"), hp = 100, en = 100):
        if name == "":
            self.name = "Neo"
            self.hp = hp
            self.en = en
        else:
            self.name = name

    def ddosAttack(): # if hacker types in 1
        self.en -= 15
        #todo: Inflicts 20 dmg to the SysAdmin

    def phishingScam(): # if hacker types in 2
        self.hp -= 10
        self.en += 20
        #todo: restores 20 energy (capped at 100)

    def stealthMode(): # if hacker types in 3
        self.en -= 10
        #todo: Blocks SysAdmin's Firewall Purge

class SysAdmin:
    def __init__(self, name = input("Enter Player SysAdmin's Name:"), hp = 100, en = 100):
        if name == "":
            self.name = "Agent Smith"
            self.hp = hp
            self.en = en
        else:
            self.name = name

    def firewallPurge(): # if sysadmin types in 1
        self.en -= 15
        #todo: Inflicts 20 dmg to the Hacker

    def rebootSystem(): # if sysadmin types in 2
        self.hp -= 10
        self.en += 20
        #todo: restores 20 energy (capped at 100)

    def traceRoute(): # if sysadmin types in 3
        self.en -= 10
        #todo: inflicts 10 dmg; bypasses Stealth



if __name__ == "__main__":
    print("placeholder entry screen")
    hacker = Hacker() #todo: name prompt, hp and energy default to 100, 3 digit number valid input
    sysadmin = SysAdmin()
    # todo: main game loop, prompt for input, call functions based on input, check for win conditions, print status updates