# Exercise: Harder Daily Challenge
def sort_user_inputs():
    users_list = []
    
    print("Please enter information for 5 users (Name, Age, Score):")
    for _ in range(5):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        score = int(input("Enter Score: "))
        users_list.append((name, age, score))

    # Sort the list by Name (index 0), then Age (index 1), then Score (index 2) using a lambda function
    users_list.sort(key=lambda x: (x[0], x[1], x[2]))
    
    print("\nSorted Users List:")
    print(users_list)

sort_user_inputs()
