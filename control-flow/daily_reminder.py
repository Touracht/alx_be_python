#
task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case n if priority == "high":
        if time_bound == "yes":
            print("Reminder:", (task), "is a high priority task that requires immediate attention today!")
    case n if priority == "medium":
        if time_bound == "yes":
            print("Reminder:", (task), "is a medium priority task that requires immediate attention today!")
    case n if priority == "low":
        if time_bound == "yes":
            print("Reminder:", (task), "is a low priority task that requires immediate attention today!")
    case _:
        print("Not applicable.")
        
match priority:        
    case n if priority == "high":
        if time_bound == "no":
            print("Note:", (task), "is a high priority task. Consider completing it when you have free time.")
    case n if priority == "medium":
        if time_bound == "no":
            print("Note:", (task), "is a medium priority task. Consider completing it when you have free time.")
    case n if priority == "low":
        if time_bound == "no":
            print("Note:", (task), "is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Not applicable.")
        #



    
    

    
    