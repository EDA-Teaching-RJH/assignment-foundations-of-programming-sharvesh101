def init_database():
    Names = ["Picard", "Riker", "Data", "Worf", "Crusher"]
    Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Commander"]
    Divisions = ["Command", "Command", "Operations", "Security", "Medical"]
    IDs = ["1", "2", "3", "4", "5"]
    return Names, Ranks, Divisions, IDs

def display_menu(names, ranks, divs, ids):
    print(f"\n{'NAME':<10} | {'Ranks':<10} | {'Divisions':<10} | {'IDs':<10}")
    for name, rank, div, id in zip(names, ranks, divs, ids):
        print(f"{name:<11} {rank:<12} {div:<12} {id:<10}")

def add_member(names, ranks, divs, ids, new_name, new_rank, new_div, new_id):
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print(f"Member {new_name} added successfully!")
    return names, ranks, divs, ids

def main():
    Names, Ranks, Divisions, IDs = init_database()
    
    while True:
        print("\n-----Menu-----")
        print("1 Display Members")
        print("2 Add Members")
        print("3 Exit")
        print()
        choise = int(input("Enter Choice: "))
        if choise == 1:
            display_menu(Names, Ranks, Divisions, IDs)
        elif choise == 2:
            new_name = input("Enter Name of the member: ")
            new_rank = input("Enter Rank of the member: ")
            new_div = input("Enter Division of the member: ")
            new_id = input("Enter ID of the member: ")
            Names, Ranks, Divisions, IDs = add_member(Names, Ranks, Divisions, IDs, new_name, new_rank, new_div, new_id)
        elif choise == 3:
            print("Exiting...")
            break
        else:
            print("Enter A proper Choice")

main()