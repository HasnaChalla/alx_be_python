task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} priority and time-bound task that needs your attention!")
        else:
            print(
                f"Note: '{task}' is a {priority} priority and time-bound task that needs your attention!")
    case "medium":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} priority and time-bound task. Don't forget to complete it!")
        else:
            print(
                f"Note: '{task}' is a {priority} priority task. Try to get to it when you can.")
    case "low":
        if time_bound == "yes":
            print(
                f"Reminder: '{task}' is a {priority} priority but time-bound task. Schedule it accordingly.")
        else:
            print(
                f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
