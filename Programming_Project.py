import time # @NOTE subject to change

# Phase 0: program init
def hacker_init(hacker_name = "Neo", hacker_hp = 100, hacker_en = 30): #init hacker default values 
    hacker_name = hacker_name_init(hacker_name)
    hacker_hp = min(hacker_hp, 100)
    hacker_en = min(hacker_en, 100)
    return hacker_name, hacker_hp, hacker_en

def hacker_name_init(hacker_name = "Neo"):
    hacker_name = hacker_name if hacker_name and hacker_name.strip() else "Neo"
    return hacker_name

def sysadmin_init(sysadmin_name = "Agent Smith", sysadmin_hp = 100, sysadmin_en = 30): #init sysadmin default values
    sysadmin_name = sysadmin_name_init(sysadmin_name)
    sysadmin_hp = min(sysadmin_hp, 100)
    sysadmin_en = min(sysadmin_en, 100)
    return sysadmin_name, sysadmin_hp, sysadmin_en

def sysadmin_name_init(sysadmin_name = "Agent Smith"):
    sysadmin_name = sysadmin_name if sysadmin_name and sysadmin_name.strip() else "Agent Smith"
    return sysadmin_name 

def game_over(hacker_hp, sysadmin_hp):
    if hacker_hp <= 0 and sysadmin_hp <= 0:
        return "Double KO! It's a tie!\n"
    elif hacker_hp <= 0:
        return "SysAdmin wins!\n"
    elif sysadmin_hp <= 0:
        return "Hacker wins!\n"
    else:
        return None

hacker_stealth = False

def is_valid_sequence(sequence):
    if sequence[0:1] == "":
        return False
    elif sequence[1:2] == "":
        return False
    elif sequence[2:3] == "":
        return False
    elif sequence[3:4] != "":
        return False
    elif sequence[0:1] != "1" and sequence[0:1] != "2" and sequence[0:1] != "3":
        return False
    elif sequence[1:2] != "1" and sequence[1:2] != "2" and sequence[1:2] != "3":
        return False
    elif sequence[2:3] != "1" and sequence[2:3] != "2" and sequence[2:3] != "3":
        return False
    return True

def attack_handling(hacker_sequence, sysadmin_sequence):
    global hacker_name, hacker_hp, hacker_en
    global sysadmin_name, sysadmin_hp, sysadmin_en
    global hacker_stealth

    i = 0
    sequence_active = True

    while i < 3 and sequence_active:
        hacker_val = int(hacker_sequence[i])
        sysadmin_val = int(sysadmin_sequence[i])
        hacker_sequence_skipped = False
        sysadmin_sequence_skipped = False
        hacker_damage = 0
        sysadmin_damage = 0

        print(f"Sequence {i+1}:")
        time.sleep(1) # @NOTE subject to change, just want to add some delay for better UX, can remove or adjust as needed

        if hacker_val == 1:
            if hacker_en <= 15:
                print("Frozen! Not enough energy")
                hacker_sequence_skipped = True
            else:
                hacker_en -= 15
                hacker_damage = 20
                print(f"{hacker_name} uses DDoS attack!")
        elif hacker_val == 2:
            if hacker_hp <= 10:
                print("Not enough HP")
                hacker_sequence_skipped = True
            else:
                hacker_en += 20
                hacker_en = min(hacker_en, 100)
                print(f"{hacker_name} uses Phishing scam! +20 energy")
        elif hacker_val == 3:
            if hacker_en <= 10:
                print("Frozen! Not enough energy")
                hacker_sequence_skipped = True
            else:
                hacker_en -= 10
                hacker_stealth = True
                print(f"{hacker_name} uses Stealth Mode!")

        if sysadmin_val == 1:
            if sysadmin_en <= 15:
                print("Frozen! Not enough energy")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en -= 15
                if hacker_stealth == True:
                    print(f"{sysadmin_name} uses Firewall purge! Blocked by Stealth Mode!")
                else:
                    sysadmin_damage = 20
                    print(f"{sysadmin_name} uses Firewall purge!")
        elif sysadmin_val == 2:
            if sysadmin_hp <= 10:
                print("Not enough HP")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en += 20
                sysadmin_en = min(sysadmin_en, 100)
                print(f"{sysadmin_name} uses Reboot system! +20 energy")
        elif sysadmin_val == 3:
            if sysadmin_en <= 10:
                print("Frozen! Not enough energy")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en -= 10
                print(f"{sysadmin_name} uses Trace route! Bypasses Stealth Mode!")
                if hacker_stealth == True:
                    hacker_stealth = False
                    print("Stealth mode bypassed!")

        if hacker_damage > 0:
            sysadmin_hp -= hacker_damage
            print(f"DDoS attack deals -20 hp to {sysadmin_name}!")

        if sysadmin_damage > 0:
            hacker_hp -= sysadmin_damage
            print(f"Firewall purge deals -20 hp to {hacker_name}!")

        if hacker_sequence_skipped == True:
            print(f"Hacker sequence {i+1} skipped.")

        if sysadmin_sequence_skipped == True:
            print(f"SysAdmin sequence {i+1} skipped.")

        print(f"{hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy")

        round_result = game_over(hacker_hp, sysadmin_hp)
        if round_result is not None:
            print(round_result)
            sequence_active = False
        i += 1


hacker_stealth = False

game_running = True 

while game_running:
    turn_number = 1
    print("WELCOME to the Hacker vs SysAdmin Hacking Game!\n")
    print("boilerplate rules and instructions here\n")

    # phase 2 input/validation
    hacker_name = input("Hacker name?: ")
    hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)

    sysadmin_name = input("SysAdmin name?: ")
    sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

    print(f"Current Hacker: {hacker_name} vs Current SysAdmin: {sysadmin_name}\n")

    # Phase 3: attack phase
    while hacker_hp > 0 and sysadmin_hp > 0:
        print(f"Round {turn_number}")
        print(f"{hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy\n")
        hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")
        while is_valid_sequence(hacker_sequence) == False:
            print("Invalid sequence. Try again.")
            hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

        sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")
        while is_valid_sequence(sysadmin_sequence) == False:
            print("Invalid sequence. Try again.")
            sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

        attack_handling(hacker_sequence, sysadmin_sequence)

        # phase 4 server event
        if turn_number % 3 == 0 and game_over(hacker_hp, sysadmin_hp) is None:
            print("Server overheats! -10 hp to both sides!")
            hacker_hp -= 10
            sysadmin_hp -= 10
            print(f"{hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy")

        turn_number += 1

    print("Game over!\n")
    print(f"Final status - {hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy\n")


    game_running = False

