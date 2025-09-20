task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match (priority, time_bound):
    case ("high", "yes"):
        print(
            f"Reminder: '{task}' is a high priority and time-bound task that needs your attention!")
    case ("high", "no"):
        print(
            f"Reminder: '{task}' is a high priority task. Please address it soon.")
    case ("medium", "yes"):
        print(
            f"Reminder: '{task}' is a medium priority and time-bound task. Don't forget to complete it!")
    case ("medium", "no"):
        print(
            f"Reminder: '{task}' is a medium priority task. Try to get to it when you can.")
    case ("low"):
        if time_bound == "yes":
            print(
                f"Note: '{task}' is a low priority but time-bound task. Schedule it accordingly.")
        else:
            print(
                f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
