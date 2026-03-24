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

def hacker_attacks(hacker_sequence): #TODO: make hacker_attacks() and sysadmin_attacks() run in parallel sequence
    global hacker_name, hacker_hp, hacker_en
    global sysadmin_name, sysadmin_hp, sysadmin_en
    global hacker_stealth
    
    i = 0
    while i < 3:
        val = int(hacker_sequence[i])
        hacker_sequence_skipped = False
        print(f"Hacker sequence {i+1}: attack {val}")
        time.sleep(1) # @NOTE subject to change, just want to add some delay for better UX, can remove or adjust as needed
        if val == 1:
            if hacker_en <= 15:
                print("Frozen! Not enough energy")
                hacker_sequence_skipped = True
            else: 
                hacker_en -= 15
                sysadmin_hp -= 20
                print(f"DDos attack! -20 hp to {sysadmin_name}!")

        elif val == 2:

            if hacker_hp <= 10:
                print("Not enough HP")
                hacker_sequence_skipped = True
            else:
                hacker_en += 20
                hacker_en = max(hacker_en, 100)
                print(f"Phishing scam! +20 energy to {hacker_name}! {hacker_en} / 100 energy")

        elif val == 3:  

            if hacker_en <= 10:
                print("Frozen! Not enough energy")
                hacker_sequence_skipped = True
            else:
                hacker_en -= 10
                hacker_stealth = True
                print("Stealth mode! Blocks firewall purge!")
                #TODO: block SysAdmin's move 1 (firewall purge)

        if hacker_sequence_skipped == True:
            print(f"Hacker sequence {i+1} skipped.")
        i += 1

def sysadmin_attacks(sysadmin_sequence): #TODO: make hacker_attacks() and sysadmin_attacks() run in parallel sequence
    global hacker_name, hacker_hp, hacker_en
    global sysadmin_name, sysadmin_hp, sysadmin_en
    global hacker_stealth

    j = 0
    while j < 3:
        val = int(sysadmin_sequence[j])
        sysadmin_sequence_skipped = False
        print(f"SysAdmin sequence {j+1}: attack {val}")
        time.sleep(1) # @NOTE subject to change, just want to add some delay for better UX, can remove or adjust as needed
        if val == 1:
            if sysadmin_en <= 15:
                print("Frozen! Not enough energy")
                sysadmin_sequence_skipped = True
            else: 
                if hacker_stealth == True:
                    print("Firewall purge! Blocked by Stealth Mode!")
                else:
                    sysadmin_en -= 15
                    hacker_hp -= 20
                    print("Firewall purge! -20 hp to {hacker_name}! {sysadmin_en} energy left")
        elif val == 2:
            if sysadmin_hp <= 10:
                print("Not enough HP")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en += 20
                sysadmin_en = max(sysadmin_en, 100)
                print("Reboot system! +20 energy to {sysadmin_name}! {sysadmin_en} / 100 energy")
        elif val == 3:  
            if sysadmin_en <= 10:
                print("Frozen! Not enough energy")
                sysadmin_sequence_skipped = True
            else:
                sysadmin_en -= 10
                print("Trace route! Bypasses stealth mode!")
                if hacker_stealth == True:
                    hacker_stealth = False
                    print("Stealth mode bypassed!")

        if sysadmin_sequence_skipped == True:
            print(f"SysAdmin sequence {j+1} skipped.")
        j += 1


hacker_stealth = False

game_running = 0 # 0 == not running, 1 == default start, 2 == restart (resets hp and energy, keeps names), 3 == full reset (resets everything)
#TODO: implement game_running == 2 and game_running == 3



game_running = 1 #default start/game init

while game_running != 0:
    if game_running == 1:
        turn_number = 1


        print("WELCOME to the Hacker vs SysAdmin Hacking Game!")
        print("boilerplate rules and instructions here")

        hacker_name = input("Hacker name?: ")
        hacker_name, hacker_hp, hacker_en = hacker_init(hacker_name)

        sysadmin_name = input("SysAdmin name?: ")
        sysadmin_name, sysadmin_hp, sysadmin_en = sysadmin_init(sysadmin_name)

        print(f"Current Hacker: {hacker_name} vs Current SysAdmin: {sysadmin_name}")
        # Phase 3: attack phase
        while hacker_hp > 0 and sysadmin_hp > 0:
            print(f"Round {turn_number}")
            print(f"{hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy")
            hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")
            while is_valid_sequence(hacker_sequence) == False:
                print("Invalid sequence. Try again.")
                hacker_sequence = input(f"{hacker_name}, enter your attack sequence: ")

            sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")
            while is_valid_sequence(sysadmin_sequence) == False:
                print("Invalid sequence. Try again.")
                sysadmin_sequence = input(f"{sysadmin_name}, enter your attack sequence: ")

            hacker_attacks(hacker_sequence)
            sysadmin_attacks(sysadmin_sequence)


            if turn_number % 3 == 0:
                print("Server overheats! -10 hp to both sides!")
                hacker_hp -= 10
                sysadmin_hp -= 10
                print(f"{hacker_name}: {hacker_hp} hp, {hacker_en} energy || {sysadmin_name}: {sysadmin_hp} hp, {sysadmin_en} energy")

            turn_number += 1

        
    elif game_running == 2:
        pass
        # TODO: implement game_running == 2 (resets hp and energy, keeps names)
    elif game_running == 3:
        pass
        # TODO: implement game_running == 3 (resets everything)
    elif game_running == 0:
        print("Exiting game...")
        game_running = 0
    else: 
        print("Invalid game state")
        







   

"""
    
    Phase 3 Attack phase:

    - Hacker first then admin
    - Hacker: input 3 digit sequence of 1, 2, and 3
        - 1: DDoS attack (costs 15 energy, -20 hp to sysadmin)
        - 2: Phishing scam (restores 20 energy to hacker)
        - 3: Stealth Mode (costs 10 energy, blocks firewall purge)
    - SysAdmin: input 3 digit sequence of 1, 2, and 3
        - 1: Firewall purge (costs 15 energy, -20 hp to hacker, blocked by stealth mode)
        - 2: Reboot system (costs 10 hp, +20 energy to sysadmin (capped at 100))
        - 3: Trace route (cost 10 energy, bypass stealth mode)

    Each attack phase is done in 3 sequence per round
    Eg: Hacker inputs 123, then sysadmin inputs 321,
    then resolve the attacks in order 
    (hacker attack 1, sysadmin attack 1, 
    hacker attack 2, sysadmin attack 2, 
    hacker attack 3, sysadmin attack 3)

    
    - real time (per sequence) update of HP and energy for both sides
    - if hp of one side reaches 0, the other side wins and game ends (turn ends immediately)
    - if hp of both sides reaches 0, double KO (turn ends immediately)
"""

"""
    Sample turn:
    Round 1
    Hacker, enter your attack sequence: 123
    SysAdmin, enter your attack sequence: 321

    Sequence 1:
    Neo uses DDoS attack! -20 hp to Agent Smith! 
    Agent Smith uses Trace route! Bypasses Stealth Mode! 
    Neo: 100 hp, 15 energy || Agent Smith: 80 hp, 20 energy
    Sequence 2:
    Neo uses Phishing scam! +20 energy to Neo! 
    Agent Smith uses Reboot system! +20 energy to Agent Smith! 
    Neo: 100 hp, 35 energy || Agent Smith: 80 hp, 40 energy
    Sequence 3:
    Neo uses Stealth Mode! Blocks Firewall purge! 
    Agent Smith uses Firewall purge! Blocked by Stealth Mode!
    Neo: 100 hp, 25 energy || Agent Smith: 80 hp, 25 energy 
    """

"""
    Phase 4: server overheat
    - Every 3 rounds, system overheats
    - -10hp to both sides
    - post-overheat status update
"""
