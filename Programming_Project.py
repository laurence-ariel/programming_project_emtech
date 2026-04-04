import time 

clear = "\033[2J\033[H" # clear screen after name input, each sequence, each round, and after game over

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
    return sysadmin_name, sysadmin_hp, sysadmin_en

def sysadmin_name_init(sysadmin_name = "Agent Smith"):
    sysadmin_name = sysadmin_name if sysadmin_name and sysadmin_name.strip() else "Agent Smith"
    return sysadmin_name 

def game_over(hacker_hp, sysadmin_hp):
    if hacker_hp <= 0 and sysadmin_hp <= 0:
        return "Double KO\n"
    elif hacker_hp <= 0:
        return f"SysAdmin {sysadmin_name} wins the competition\n"
    elif sysadmin_hp <= 0:
        return f"Hacker {hacker_name} wins the competition\n"
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

        print(f"Sequence {i + 1}:")
        
        time.sleep(1) 

        if hacker_val == 1:
            if hacker_en <= 15:
                print(f"Frozen, Not enough energy; Hacker {hacker_name} sequence {i + 1} skipped")
            else:
                hacker_en -= 15
                sysadmin_hp -= 20
                print(f"Hacker {hacker_name} uses DDoS attack, -20 HP to SysAdmin {sysadmin_name}")

        elif hacker_val == 2:
            hacker_hp -= 10
            hacker_en += 20
            hacker_en = min(hacker_en, 100)
            print(f"Hacker {hacker_name} uses Phishing scam; +20 energy, -10 HP to self")

        elif hacker_val == 3:
            if hacker_en <= 10:
                print(f"Frozen, Not enough energy; Hacker {hacker_name} sequence {i + 1} skipped")
            else:
                hacker_en -= 10
                hacker_stealth = True
                print(f"Hacker {hacker_name} uses Stealth Mode for sequence {i + 1}")

        if sysadmin_val == 1:
            if sysadmin_en <= 15:
                print(f"Frozen, Not enough energy; SysAdmin {sysadmin_name} sequence {i + 1} skipped \n ")
            else:
                sysadmin_en -= 15

                if hacker_stealth == True:
                    print(f"SysAdmin {sysadmin_name} uses Firewall purge, blocked by Hacker {hacker_name} Stealth Mode \n")
                else:
                    hacker_hp -= 20
                    max(0, hacker_hp)
                    print(f"SysAdmin {sysadmin_name} uses Firewall purge, -20 HP to Hacker {hacker_name} \n ")

        elif sysadmin_val == 2:
            sysadmin_hp -= 10
            sysadmin_en += 20
            sysadmin_en = min(sysadmin_en, 100)
            print(f"SysAdmin {sysadmin_name} uses Reboot system, +20 energy, -10 HP to self \n")

        elif sysadmin_val == 3:
            if sysadmin_en <= 10:
                print(f"Frozen, Not enough energy; SysAdmin {sysadmin_name} sequence {i + 1} skipped \n")
            else:
                sysadmin_en -= 10
                hacker_hp -= 10
                hacker_hp = max(0, hacker_hp)
                print(f"SysAdmin {sysadmin_name} uses Trace route,", end=" ")

                if hacker_stealth == True:
                    hacker_stealth = False
                    print(f"bypassing Hacker {hacker_name} Stealth Mode; -10 HP to {hacker_name} \n")
                else:
                    print(f"-10 HP to Hacker {hacker_name} \n")

        print(f"{hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy\n")

        round_result = game_over(hacker_hp, sysadmin_hp)
        if round_result is not None:
            print(round_result)
            sequence_active = False

        i += 1
        hacker_stealth = False


hacker_stealth = False

game_running = 1

while game_running == 1:
    turn_number = 1
    
    print("----------------------------------------------")
    print("--------- Greetings, Hacker! -----------------")
    print("----------------------------------------------")
    print("--------- Welcome to Escape SysAdmin! --------")
    print("----------------------------------------------")
    print("")
    print("The rules are simple : ")
    print("                       - This is a two-player game, enter your name (Hacker) and the name of your opponent (SysAdmin)")
    print("                       - You and your opponent will each be given a chance to enter an attack sequence.")
    print("                                    (Each attack sequence must be a 3 digit number, a mix of the numbers 1, 2, and 3. Nothing more, nothing less.")
    print("                                    1 = DDoS attack, 2 = Phishing scam, 3 = Stealth mode for Hacker")
    print("                                    1 = Firewall purge, 2 = Reboot system, 3 = Trace route for SysAdmin")
    print("                       - Each sequence number corresponds to an attack that goes against your opponent")
    print("                       - Play the right attacks. In this game, you must make sure your opponent loses their HP first")
    print("                       - If you run out of energy, you can't perform the attack and you will be frozen for that sequence")
    print("                       - Every 3 turns, the server will overheat, causing -10 HP to both sides")
    print("")
    print("---------------------------------------------------------------")
    print("---- May the Divine steer your fate towards the better --------")
    print("---------------------------------------------------------------")

    # phase 2 input/validation
    hacker_name = input("Enter the Hacker's name: ")
    hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)
    
    print("")

    sysadmin_name = input("Enter the SysAdmin's name: ")
    sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

    print(clear, end="")

    print("")
    print(f"Current Hacker: {hacker_name} vs Current SysAdmin: {sysadmin_name}")
    print("Let the competition begin!\n")

    time.sleep(1)

    # Phase 3: attack phase
    overheat_ctr = 3
    while hacker_hp > 0 and sysadmin_hp > 0:
        time.sleep(2)
        print(clear, end="")
        print(f"=========================== Round {turn_number} =========================== ")
        print(f"{hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy\n")

        # phase 4 server event
        overheat_ctr -= 1
        if overheat_ctr == 0 and game_over(hacker_hp, sysadmin_hp) is None:
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print("")
            print("Server overheats, -10 HP to both sides")

            hacker_hp = max(0, hacker_hp - 10)
            sysadmin_hp = max(0, sysadmin_hp - 10)

            print(f"Overheat report: {hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy")
            print("")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print("")

            overheat_ctr = 3

            overheat_result = game_over(hacker_hp, sysadmin_hp)
            if overheat_result is not None:
                print(overheat_result)

        if game_over(hacker_hp, sysadmin_hp) is None:
            hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

            while is_valid_sequence(hacker_sequence) == False:
                print("Invalid sequence. Try again.")
                hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

            sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

            while is_valid_sequence(sysadmin_sequence) == False:
                print("Invalid sequence. Try again.")
                sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

            print("")

            attack_handling(hacker_sequence, sysadmin_sequence)

            turn_number += 1

    print("Game over!\n")

    hacker_hp = max(0, hacker_hp)
    sysadmin_hp = max(0, sysadmin_hp)

    print(f"Final status - {hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy\n")

    time.sleep(4)
    print(clear, end="")

    play_again = input("Would you like to reboot the competition or escape to the real world? (R/E): ")

    while play_again.lower() != "r" and play_again.lower() != "e":
        print("Invalid input, enter 'R' to reboot or 'E' to escape.\n")
        play_again = input("Would you like to reboot the competiton or escape to the real world? (R/E): ")

    if play_again.lower() == "r":
        print("\n Rebooting the competition...\n")
        game_running = 2
        time.sleep(2)

    else:
        print(f"You have to let it all go, {hacker_name}. Fear, doubt, and disbelief. Free your mind.")
        time.sleep(3)
        game_running = 0
        

while game_running == 2: 
    turn_number = 1

    hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)
    sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

    print(f"Current Hacker: {hacker_name} vs Current SysAdmin: {sysadmin_name}\n")

    # Phase 3: attack phase of rebooted game
    overheat_ctr = 3
    while hacker_hp > 0 and sysadmin_hp > 0:
        time.sleep(2)
        print(clear, end="")
        print(f"=========================== Round {turn_number} =========================== ")
        print(f"{hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy\n")

        # phase 4 server event of rebooted game
        overheat_ctr -= 1
        
        if overheat_ctr == 0 and game_over(hacker_hp, sysadmin_hp) is None:
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print("")
            print("Server overheats, -10 HP to both sides")
            hacker_hp = max(0, hacker_hp - 10)
            sysadmin_hp = max(0, sysadmin_hp - 10)
            print(f"Overheat report: {hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy")
            print("")
            print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
            print("")
            overheat_ctr = 3

            overheat_result = game_over(hacker_hp, sysadmin_hp)
            if overheat_result is not None:
                print(overheat_result)

        if game_over(hacker_hp, sysadmin_hp) is None:
            hacker_sequence = input(f"Hacker {hacker_name}, enter your attack sequence: ")

            while is_valid_sequence(hacker_sequence) == False:
                print("Invalid sequence. Try again.")
                hacker_sequence = input(f"Hacker {hacker_name}, enter your attack sequence: ")

            sysadmin_sequence = input(f"Sysadmin {sysadmin_name}, enter your attack sequence: ")

            while is_valid_sequence(sysadmin_sequence) == False:
                print("Invalid sequence. Try again.")
                sysadmin_sequence = input(f"Sysadmin {sysadmin_name}, enter your attack sequence: ")

            print("")

            attack_handling(hacker_sequence, sysadmin_sequence)

            turn_number += 1

    print("Game over!\n")

    hacker_hp = max(0, hacker_hp)
    sysadmin_hp = max(0, sysadmin_hp)

    print(f"Final status - {hacker_name}: {hacker_hp} HP, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} HP, {sysadmin_en} energy\n")

    time.sleep(4)
    print(clear, end="")

    play_again = input("Would you like to reboot the competition or escape to the real world? (R/E): ")

    while play_again.lower() != "r" and play_again.lower() != "e":
        print("Invalid input, enter 'R' to reboot or 'E' to escape.\n")
        play_again = input("Would you like to reboot the competiton or escape to the real world? (R/E): ")

    if play_again.lower() == "r":
        print("")
        print("Rebooting the competition...\n")
        game_running = 2
        time.sleep(2)
    else:
        print(f"You have to let it all go, {hacker_name}. Fear, doubt, and disbelief. Free your mind.")
        time.sleep(3)
        game_running = 0