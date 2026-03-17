# Phase 0: program init
def hacker_init(hacker_name = "Neo", hacker_hp = 100, hacker_en = 30):
    hacker_name = hacker_name if hacker_name else "Neo"
    hacker_hp = min(hacker_hp, 100)
    hacker_en = min(hacker_en, 100)

def sysadmin_init(sysadmin_name = "Agent Smith", sysadmin_hp = 100, sysadmin_en = 30):
    sysadmin_name = sysadmin_name if sysadmin_name else "Agent Smith"
    sysadmin_hp = min(sysadmin_hp, 100)
    sysadmin_en = min(sysadmin_en, 100)

def hacker_attacks(sequence):
    valid = 0
    while valid == 0:
        sequence = input("Enter a 3 digit sequence using only 1, 2, or 3: ")
        valid = 1 
    if sequence == "":
        valid = 0
    elif sequence[0:1] == "":
        valid = 0
    elif sequence[1:2] == "":
        valid = 0
    elif sequence[2:3] == "":
        valid = 0
    elif sequence[3:4] != "":
        valid = 0
    elif sequence[0] != "1" and sequence[0] != "2" and sequence[0] != "3":
        valid = 0
    elif sequence[1] != "1" and sequence[1] != "2" and sequence[1] != "3":
        valid = 0
    elif sequence[2] != "1" and sequence[2] != "2" and sequence[2] != "3":
        valid = 0
    
    if valid == 0: 
        print("Invalid sequence. Try again.")
    
    i = 0
    while i < 3:
        val = int(sequence[i])
        if val == 1:

            if hacker_en <= 15:
                print("Frozen! Not enough energy") #TODO: skip turn
            else: 
                hacker_en -= 15
                sysadmin_hp -= 20
                print("DDos attack! -20 hp to {sysadmin_name}!")

        elif val == 2:

            if hacker_hp <= 10:
                print("Not enough HP")
            else:
                hacker_en += 20
                hacker_en = max(hacker_en, 100)
                print("Phishing scam! +20 energy to {hacker_name}! {hacker_en} / 100 energy")

        elif val == 3:  

            if hacker_en <= 10:
                print("Frozen! Not enough energy") #TODO: skip turn
            else:
                hacker_en -= 10
                #TODO: block SysAdmin's move 1 (firewall purge)
        i += 1

def sysadmin_attacks():
    pass



game_running = True
while game_running:
    hacker_name = input("Hacker name?: ")
    hacker_init(hacker_name)

    sysadmin_name = input("SysAdmin name?: ")
    sysadmin_init(sysadmin_name)

    