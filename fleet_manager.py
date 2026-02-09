def init_database():
    Names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Divisions = ["Command", "Command", "Operations", "Security", "Medical"]
    IDs = ["1", "2", "3", "4", "5"]
    return Names, Ranks, Divisions, IDs

def display_menu():
    print("\n-----Menu-----")
    print("1 Display Members")
    print("2 Add Members")
    print("3 Remove Members")
    print("4 Update Rank")
    print("5 Search Crew")
    print("6 Filter by Division")
    print("7 Calculate Payroll")
    print("8 Exit")
    print()
    choice = int(input("Enter Choice: "))
    return choice

def add_member(names, ranks, divs, ids, new_name, new_rank, new_div, new_id):
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print(f"Member {new_name} added successfully!")
    return names, ranks, divs, ids

def remove_member(names, ranks, divs, ids):
    print("\n--- Remove Member ---")
    remove_id = input("Enter ID of the Member to remove: ")
    
    if remove_id in ids:
        index = ids.index(remove_id)
        removed_name = names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print(f"Member {removed_name} removed successfully!")
    else:
        print(f"ID {remove_id} not found!")
    return names, ranks, divs, ids

def update_rank(names, ranks, ids):
    print("\n--- Update Rank ---")
    update_id = input("Enter ID of the Member to update rank: ")
    
    if update_id in ids:
        index = ids.index(update_id)
        new_rank = input(f"Enter new rank for {names[index]}: ")
        ranks[index] = new_rank
        print(f"Member {names[index]}'s rank updated successfully!")
    else:
        print(f"ID {update_id} not found!")
    return names, ranks, ids

def update_rank(names, ranks, ids):
    print("\n--- Update Rank ---")
    update_id = input("Enter ID of the Member to update rank: ")
    
    if update_id in ids:
        index = ids.index(update_id)
        new_rank = input(f"Enter new rank for {names[index]}: ")
        ranks[index] = new_rank
        print(f"Member {names[index]}'s rank updated successfully!")
    else:
        print(f"ID {update_id} not found!")
    
    return names, ranks, ids

def display_roster(names, ranks, divs, ids):
    print(f"\n{'NAME':<10} | {'Ranks':<10} | {'Divisions':<10} | {'IDs':<10}")
    for name, rank, div, id in zip(names, ranks, divs, ids):
        print(f"{name:<11} {rank:<12} {div:<12} {id:<10}")

def search_crew(names, ranks, divs, ids):
    term = input("Enter search term: ").strip().lower()
    print()
    header = f"{'NAME':<10} | {'Ranks':<10} | {'Divisions':<10} | {'IDs':<10}"
    matches = []
    for name, rank, div, id_ in zip(names, ranks, divs, ids):
        if term in name.lower():
            matches.append((name, rank, div, id_))
    if matches:
        print(header)
        for name, rank, div, id_ in matches:
            print(f"{name:<11} {rank:<12} {div:<12} {id_:<10}")
    else:
        print(f"No crew members found matching '{term}'.")
    return

def filter_by_division(names, divs):
    choice = input('Enter division (Command, Operations, Sciences): ').strip().title()
    matches = []
    match choice:
        case 'Command' | 'Operations' | 'Sciences':
            for name, div in zip(names, divs):
                if div == choice:
                    matches.append(name)
        case _:
            print(f"Invalid division: '{choice}'.")
            return

    if matches:
        print(f"\nMembers in {choice}:")
        for m in matches:
            print(m)
    else:
        print(f"No members found in {choice}.")
    return

def calculate_payroll(ranks):
    pay_table = {
        'captain': 1000,
        'commander': 800,
        'lt commander': 600,
        'lt. commander': 600,
        'lieutenant': 500,
        'ensign': 200,
    }
    total = 0
    for r in ranks:
        if not isinstance(r, str):
            continue
        key = r.strip().lower()
        key = key.replace('.', '')
        key = key.replace('  ', ' ')
        if key in pay_table:
            total += pay_table[key]
            continue
        if 'captain' in key:
            total += pay_table['captain']
        elif 'lt' in key and 'commander' in key:
            total += pay_table['lt commander']
        elif 'commander' in key:
            total += pay_table['commander']
        elif 'lieutenant' in key:
            total += pay_table['lieutenant']
        elif 'ensign' in key:
            total += pay_table['ensign']
        else:
            total += 250
    return total

def main():
    Names, Ranks, Divisions, IDs = init_database()    
    user_name = input("Enter your full name: ")
    print(f"Current user logged in: {user_name}")
    while True:
        choice = display_menu()
        if choice == 1:
            display_roster(Names, Ranks, Divisions, IDs)
        elif choice == 2:
            new_name = input("Enter Name of the member: ")
            new_rank = input("Enter Rank of the member: ")
            new_div = input("Enter Division of the member: ")
            new_id = input("Enter ID of the member: ")
            Names, Ranks, Divisions, IDs = add_member(Names, Ranks, Divisions, IDs, new_name, new_rank, new_div, new_id)
        elif choice == 3:
            Names, Ranks, Divisions, IDs = remove_member(Names, Ranks, Divisions, IDs)
        elif choice == 4:
            Names, Ranks, IDs = update_rank(Names, Ranks, IDs)
        elif choice == 5:
            search_crew(Names, Ranks, Divisions, IDs)
        elif choice == 6:
            filter_by_division(Names, Divisions)
        elif choice == 7:
            total_payroll = calculate_payroll(Ranks)
            print(f"Total Monthly Payroll: £{total_payroll}")
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Enter A proper Choice")

main()