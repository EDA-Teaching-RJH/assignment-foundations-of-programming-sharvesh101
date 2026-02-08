def init_database():
    Names = ["Jack", "Mike"]
    Ranks = ["senior", "junior"]
    Divisions = ["Dev","Ops"]
    IDs = ["1","2"]
    return Names , Ranks, Divisions,IDs

def display_menu():
    Names , Ranks , Divisons, IDs = init_database()
    print(f"{'NAME':<10} | {'Ranks':<10} | {'Divisions':<10} | {'IDs':<10}")
    for name ,rank , div, id in zip(Names,Ranks,Divisons,IDs):
        print(f"{name:<11} {rank:<12} {div:<12} {id:<10}")

def main():
    display_menu()

main()