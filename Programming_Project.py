import time 

green = "\033[92m" # default text color for hacker
blue = "\033[94m" # default text color for sysadmin
orange_red_bg = "\x1b[48;5;202m" # for server event bg
cyan_bg = "\x1b[48;5;14m" # for frozen state bg 
yellow = "\033[93m" # for skipped sequence bg
flash = "\x1b[5m" # for server event text
reset = "\033[0m" # reset text color and bg to default

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


        print(f"Sequence {i + 1}:")
        
        time.sleep(1) 

        if hacker_val == 1:
            if hacker_en <= 15:
                print(f"{cyan_bg}Frozen! Not enough energy{reset}")
                hacker_sequence_skipped = True
            else:
                hacker_en -= 15
                sysadmin_hp -= 20
                print(f"{green}Hacker {hacker_name} uses DDoS attack!{reset} {blue}-20 hp to SysAdmin {sysadmin_name}{reset}")
        elif hacker_val == 2:
            if hacker_hp <= 10:
                print(f"{cyan_bg}Not enough HP{reset}")
                hacker_sequence_skipped = True
            else:
                hacker_hp -= 10
                hacker_en += 20
                hacker_en = min(hacker_en, 100)
                print(f"{green}{hacker_name} uses Phishing scam! +20 energy{reset}")
        elif hacker_val == 3:
            if hacker_en <= 10:
                print(f"{cyan_bg}Frozen! Not enough energy{reset}")
                hacker_sequence_skipped = True
            else:
                hacker_en -= 10
                hacker_stealth = True
                print(f"{green}{hacker_name} uses Stealth Mode!{reset}")

        if sysadmin_val == 1:
            if sysadmin_en <= 15:
                print(f"{cyan_bg}Frozen! Not enough energy{reset}\n")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en -= 15
                
                if hacker_stealth == True:
                    print(f"{blue}{sysadmin_name} uses Firewall purge!{reset} {yellow}Blocked by Hacker {hacker_name} Stealth Mode!{reset}\n")
                else:
                    hacker_hp -= 20
                    max(0, hacker_hp)
                    print(f"{blue}{sysadmin_name} uses Firewall purge! -20 hp to Hacker {hacker_name}!{reset} \n")

        elif sysadmin_val == 2:
            if sysadmin_hp <= 10:
                print(f"{cyan_bg}Not enough HP{reset}\n")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_hp -= 10
                sysadmin_en += 20
                sysadmin_en = min(sysadmin_en, 100)
                print(f"{blue}{sysadmin_name} uses Reboot system! +20 energy{reset}\n")

        elif sysadmin_val == 3:
            if sysadmin_en <= 10:
                print(f"{cyan_bg}Frozen! Not enough energy{reset}")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en -= 10
                hacker_hp -= 10
                hacker_hp = max(0, hacker_hp)
                print(f"{blue}{sysadmin_name} uses Trace route!{reset}\n")
                if hacker_stealth == True:
                    hacker_stealth = False
                    print(f"{yellow}Bypassed Hacker {hacker_name} Stealth Mode!{reset}\n")

        if hacker_sequence_skipped == True:
            print(f"{yellow}Hacker sequence {i + 1} skipped.{reset}")

        if sysadmin_sequence_skipped == True:
            print(f"{yellow}SysAdmin sequence {i + 1} skipped.{reset}")

        print(f"{green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}\n")

        round_result = game_over(hacker_hp, sysadmin_hp)
        if round_result is not None:
            print(round_result)
            sequence_active = False

        i += 1


hacker_stealth = False

game_running = 1

while game_running == 1:
    turn_number = 1
    print(f"WELCOME to the Hacker vs SysAdmin Hacking Game!\n")
    print("boilerplate rules and instructions here\n")

    # phase 2 input/validation
    hacker_name = input("Hacker name?: ")
    hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)
    

    sysadmin_name = input("SysAdmin name?: ")
    sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

    print(f"Current Hacker: {green}{hacker_name}{reset} vs Current SysAdmin: {blue}{sysadmin_name}{reset}\n")

    # Phase 3: attack phase
    while hacker_hp > 0 and sysadmin_hp > 0:
        print(f"Round {turn_number}: ", end="")
        print(f"{green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}\n")

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
            print(f"\n{flash}{orange_red_bg}Server overheats! -10 hp to both sides!{reset}\n")
            hacker_hp -= 10
            sysadmin_hp -= 10
            print(f"{green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}")

        turn_number += 1

    print("Game over!\n")

    hacker_hp = max(0, hacker_hp)
    sysadmin_hp = max(0, sysadmin_hp)

    print(f"Final status - {green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}\n")

    play_again = input("Reboot the competition or Shut Down? (R/S): ")

    while play_again.lower() != "r" and play_again.lower() != "s":
        print("Invalid input! Enter 'R' to reboot or 'S' to shut down.\n")
        play_again = input("Reboot the competition or Shut Down? (R/S): ")

    if play_again.lower() == "r":
        print(f"\n{yellow}Rebooting the competition...{reset}\n")
        game_running = 2
        time.sleep(2)

    else:
        print("Shutting down the program. Goodbye!")
        game_running = 0

while game_running == 2: 
    turn_number = 1

    hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)
    sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

    print(f"Current Hacker: {green}{hacker_name}{reset} vs Current SysAdmin: {blue}{sysadmin_name}{reset}\n")

    # Phase 3: attack phase of rebooted game
    while hacker_hp > 0 and sysadmin_hp > 0:
        print(f"Round {turn_number}")
        print(f"{green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}\n")

        hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

        while is_valid_sequence(hacker_sequence) == False:
            print("Invalid sequence. Try again.")
            hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

        sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

        while is_valid_sequence(sysadmin_sequence) == False:
            print("Invalid sequence. Try again.")
            sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

        attack_handling(hacker_sequence, sysadmin_sequence)

        # phase 4 server event of rebooted game
        if turn_number % 3 == 0 and game_over(hacker_hp, sysadmin_hp) is None:
            print(f"\n{flash}{orange_red_bg}Server overheats! -10 hp to both sides!{reset}\n")
            hacker_hp -= 10
            sysadmin_hp -= 10
            print(f"Overheat report: {green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}")

        turn_number += 1

    print("Game over!\n")

    hacker_hp = max(0, hacker_hp)
    sysadmin_hp = max(0, sysadmin_hp)

    print(f"Final status - {green}{hacker_name}: {hacker_hp} hp, {hacker_en} energy{reset} || {blue}{sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy{reset}\n")

    play_again = input("Reboot the competition or Shut Down? (R/S): ")

    while play_again.lower() != "r" and play_again.lower() != "s":
        print("Invalid input! Please enter 'R' to reboot or 'S' to shut down.\n")
        play_again = input("Reboot the competition or Shut Down? (R/S): ")

    if play_again.lower() == "r":
        print(f"\nRebooting the competition...{reset}\n")
        game_running = 2
        time.sleep(2)
    else:
        print("Shutting down the program. Goodbye!")
        game_running = 0
