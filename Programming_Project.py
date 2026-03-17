class Hacker: # Phase 0: values  and attacks init
    def __init__(self, name = "Neo", hp = 100, en = 30):
        self.name = name if name != "" else "Neo"
        self.hp = hp
        self.en = en # capped at 100, starts at 30

    def ddosAttack(self): # if hacker types in 1
        self.en -= 15
        #todo: Inflicts 20 dmg to the SysAdmin

    def phishingScam(self): # if hacker types in 2
        self.hp -= 10
        self.en += 20
        #todo: restores 20 energy (capped at 100)

    def stealthMode(self): # if hacker types in 3
        self.en -= 10
        #todo: Blocks SysAdmin's Firewall Purge

class SysAdmin:
    def __init__(self, name = "Agent Smith", hp = 100, en = 30):
        self.name = name if name != "" else "Agent Smith"
        self.hp = hp
        self.en = en # capped at 100, starts at 30


    def firewallPurge(self): # if sysadmin types in 1
        self.en -= 15
        #todo: Inflicts 20 dmg to the Hacker

    def rebootSystem(self): # if sysadmin types in 2
        self.hp -= 10
        self.en += 20
        #todo: restores 20 energy (capped at 100)

    def traceRoute(self): # if sysadmin types in 3
        self.en -= 10
        #todo: inflicts 10 dmg; bypasses Stealth



if __name__ == "__main__":
    print("placeholder entry screen")
    # todo: main game loop, prompt for input, call functions based on input, check for win conditions, print status updates
    game_running = True
    while game_running:
        hacker = Hacker()
        sysadmin = SysAdmin()

        print(f"Hacker: {hacker.name}, Hacker HP: {hacker.hp}, SysAdmin: {sysadmin.name}")