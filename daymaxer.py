# ilyanna verbuch 

# 0 Welcome Users Section + instructions 
# purpose is to explain the commands and intended usage 

def welcome():
    name = input("What is your name? ")
    

    instructions=('Here are some simple instructions on how to use this DayMaxer! \n'
                'You can add as many tasks as you desire!\n'
                'Please type "Remove" to remove task! (Cap Sensitive) \n'
                'Type "Done" when finished! (Cap Sensitive) \n')
    
    print(f'Hello {name}! Welcome to DayMaxer, a program where you can max out your day :)\n'
          'Please be aware this uses an 24 hour clock system\n')
    print (instructions)
    return name

# welcome()


# 1 sleep and wake time inputs 
# purpose is to gather sleep and wake times to see how much time is available for tasks 

def sleep_wake_times(): # 24hr system might convert 24hr to am/pm l8er 
    try: 
        wake_time= int(input("What time do you want to wake up? "))
        if wake_time> 24 or wake_time <0: # 24hr day
            print ("Invaild please try again") 
            return sleep_wake_times()
        
        sleep_time= int(input("What time do you want to go to bed? "))
        if sleep_time > 24 or sleep_time< wake_time: 
             print ("Invaild please try again") 
             return sleep_wake_times()

        total_time_in_day= sleep_time - wake_time 
        if not total_time_in_day>0 and not total_time_in_day < 24: 
            print("Not possible this is an 24 hour clock please try again!")
            return sleep_wake_times()
        
    except ValueError: 
        print("Please enter a number within the 24 hour clock: ")
        return sleep_wake_times()
    except: 
        print("You did something we didn't like please try again!")

        return sleep_wake_times()
    else: 
        print(f"You have {total_time_in_day} available hours in your day!")
        return wake_time, sleep_time, total_time_in_day

# sleep_wake_times()


# 2 adding all the tasks in list 
# purpose is basically a nested list for adding, remove tasks without repeats 

def add_tasks(): 
    task_list=[] # users will enter tasks 

    while True:
        add_task= input('What to do you have to do today? ') # KEEPS ADDING TASKS
    
        if add_task=="Done": # might  make it not cap sensitive 
            print('Here is your tasks in a list! :)')
            print (task_list)
            break # loop stops when entering Done 

        elif add_task=="Remove": # might  make it  not cap sensitive 
            
            remove_task = input ("Which task would you like to remove? ")

            for task in task_list:
                if task["name"]==remove_task: 
                 task_list.remove(task)
                 print(f'{remove_task} has been removed from tasks!')
                 break

            else: 
                print(f'"{remove_task}" is not in the task list! Please try again!')

        elif any(task["name"] == add_task for task in task_list): # Checks every task in the tasklist for repeats of the same task 
            print(f'We added "{add_task}" already lol!')
        else: 
            priority = input("Priority? - High, Med or Low (Cap Sensitive): ") # ONLY FOR THE TERMINAL IT WILL SHOW IN THE SCHEDULE FILE 
            duration = int(input("How many hours? "))

            task = {
                "name": add_task,
                "priority": priority,
                "duration": duration
            }
            task_list.append(task)
            print(f'Task {task["name"]} has been added!')

    return task_list

           

def build_schedule(task_list, time_available):
#  3 build schedule through filtering the priority high,med,low

    high_tasks=[]
    med_tasks = []
    low_tasks = []

    total_task_hours = 0
# creates list and will add the time it tasks to do a task in the total 

    for task in task_list:
        total_task_hours += task["duration"]

        if task["priority"] == "High":
          high_tasks.append(task)
      
        elif task["priority"] == "Med":
            med_tasks.append(task)
        
        elif task["priority"] == "Low":
            low_tasks.append(task)
        
    print("\n°⛧∘₊✧─────✧₊∘°⛧°DAY SCHEDULE °⛧°∘₊✧─────✧₊∘⛧°")
    print(f"\nAvailable Hours:╰┈➤ {time_available} hours")
    print(f"Planned Hours:╰┈➤ {total_task_hours} hours")

    if total_task_hours > time_available: 
        print("\n WARNING: You might not have enough time today! :(")

    else:
        print("\nYour schedule fits into your day! :) ")

    # print high priority from high priority task 
    print("\n── ⋆⋅☆⋅⋆ ── HIGH PRIORITY ── ⋆⋅☆⋅⋆ ──")

    for task in high_tasks:
        print(f'- {task["name"]} ({task["duration"]} hrs)')

    # print medium priority from med priority task
    print("\n ── ⋆⋅☆⋅⋆ ── MEDIUM PRIORITY ── ⋆⋅☆⋅⋆ ──")

    for task in med_tasks:
        print(f'- {task["name"]} ({task["duration"]} hrs)')

    # print all low priority tasks 
    print("\n── ⋆⋅☆⋅⋆ ── LOW PRIORITY ── ⋆⋅☆⋅⋆ ──")

    for task in low_tasks:
        print(f'- {task["name"]} ({task["duration"]} hrs)')

    return total_task_hours

    

# 4 print schedule

def save_schedule(task_list, available_hours, total_task_hours):

    with open("schedule.txt", "w") as file: # with open to not need to close file and w to write without constant new docs just overwriting it 

        file.write(f"FINAL SCHEDULE ≽^• ˕ • ྀི≼\n")
        file.write("୨ৎ────୨ৎ────୨ৎ────୨ৎ────୨ৎ\n")

        file.write(f"Available Hours: {available_hours}\n")
        file.write(f"Planned Hours: {total_task_hours}\n\n")

        for task in task_list: # just the 4 loop dict from #3 

            file.write(
                f'{task["name"]} | '
                f'{task["priority"]} | '
                f'{task["duration"]} hrs\n'
            )

    print("\nSchedule saved to schedule.txt")


# 5 
def brainrot_secret():
    # serves no purpose at all 

    secret = input("\nEnter secret code for a surprise: ")

    if secret == "skibidi":
        
        print("\n ﹌﹌﹌﹌﹌﹌﹌﹌ SECRET BRAINROT CHARACTER HAS BEEN SUMMONED ﹌﹌﹌﹌﹌﹌﹌﹌\n")
        
        print("Thank you for using DayMaxer! Tung Tung Tung Sahur has created your schedule!!!")

        print('''
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣛⣛⣛⣛⡻⠿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢁⣺⣿⣿⣿⣿⣿⣿⣿⣶⠈⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃⠼⢽⣿⣿⠿⠻⠛⠻⢿⣿⠀⣾
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠙⠁⠀⠀⢠⡀⠀⢬⠃⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠻⡄⠀⣇⠀⠃⠀⠘⡇⠀⠄⢿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢈⢸⡿⣦⣀⢀⣀⣴⣿⡆⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠙⠳⠞⠁⠸⠷⠦⠈⠉⠉⠉⠀⠀⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠆⠀⠀⠤⠿⠂⠀⠀⠀⠀⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡄⠀⠀⠀⠈⣠⡼⠃⠀⠀⠀⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠛⠉⠀⢀⠠⠀⠀⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠠⠀⠀⠀⠀⢤⠘⠤⠁⢰⡆⢸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢠⠋⠤⡉⠐⡀⠀⢿⠸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠄⠀⠀⡘⢀⠆⠡⠀⠀⣈⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⡐⠈⠤⢁⠂⠀⡟⢰
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡀⠀⠀⠀⠠⠁⠂⠄⠀⣸⠁⣸
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠈⠁⢰⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⠆⠀⠀⠀⢀⣐⠀⠀⠀⢀⣸⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡁⠁⣼⡇⠀⠀⣿⣿⠀⡀⢀⣷⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⡔⠀⣼⣿⡇⣀⠀⣿⣿⡆⣡⠘⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⡿⢡⡞⢀⣾⣿⣿⣇⠀⠀⢿⣿⡇⠁⠀⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡏⣴⡇⢠⣾⣿⣿⣿⣿⠀⠀⢸⣿⣧⠀⠀⣿⣿⣿
        ⣿⣿⣿⣿⣿⠏⣼⠍⢀⣿⣿⣿⣿⣿⣿⡀⠀⢸⣿⣿⡀⠀⣻⣿⣿
        ⣿⣿⣿⡿⠋⡸⠁⢀⣾⣿⣿⣿⣿⣿⣿⣇⢀⠈⣿⣿⡇⠀⢸⣿⣿
        ⣿⣿⠟⠁⠄⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢿⡿⠁⠀⠘⣿⣿
        ⡿⠋⠀⠀⠀⣠⣾⣿⣿⣿⠿⠛⣛⣹⡏⠀⠀⠀⠀⢠⣾⣆⠀⢻⣿
        ⣦⣀⡀⠀⢰⣿⣿⣿⡃⠄⠤⡶⠋⠉⣁⣠⣴⡆⠰⠛⠻⠻⠢⠘⣿
        ⣿⣿⣿⣷⣿⣿⣿⣿⣿⣷⣶⣶⣾⣿⣿⣿⣯⣁⣀⡊⣘⣀⣀⣤⣿''')

        print("Thank you, Goodbye!")
        print("Test cases below; Explaination paragraph in a seperate pdf:")

    
    else:
        print("Wrong secret code!")
        print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠻⠟⢉⠙⢿⠉⡌⢻⡿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠻⢿⣿⣿⣿⣿⣿⣿⡏⢀⣷⣄⠀⢿⣧⡀⠀⠇⠀⡠⠀⣿⣿⣿
⣿⣿⣿⣿⠇⢀⣦⡀⠙⢿⣿⣿⣿⠿⠀⠈⣉⡉⠂⠈⢿⣧⠴⢀⡜⠁⣈⣡⠈⢹
⣿⣿⣿⣿⡂⢸⣿⣿⣦⡀⣉⣠⣤⣴⣾⣧⣈⠙⠓⠢⡜⢠⣦⡄⠰⠞⠋⠡⣴⣿
⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⠏⢁⣤⣤⣴⠖⢁⡀⠙⢁⠼⣶⣶⣦⠀⣿
⣿⣿⣿⣿⡇⠘⣿⡿⠛⠛⠛⢿⡿⠋⠁⠀⠉⠉⡁⢀⣾⠋⠹⣷⠀⢠⣈⣤⣶⣿
⣿⣿⣿⣿⣧⠀⠃⡄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠁⠾⠋⠀⠀⢿⡇⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠸⣇⠀⠀⠀⠀⠀⠐⣄⣀⢀⣴⠗⢀⣠⣴⣦⣤⡄⠈⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡀⠙⣷⣦⣴⡞⠀⣄⠈⠛⠿⠁⢰⣿⡿⠿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣦⣀⠉⠛⠁⠚⠛⠛⠂⣠⡦⠀⣠⣤⣴⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⣰⣶⣶⣶⣿⣿⣿⡁⠸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠏⢀⣼⣿⣿⣿⣿⣿⣿⣿⣧⠀⢹⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠁⣠⠿⠋⣁⠈⣿⣿⣿⣿⣿⣿⡇⠰⠿⠿⠛⠉⢠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠁⠔⠁⣴⣿⠏⠀⣿⣿⣿⠿⢻⣿⣷⡄⢰⣶⣾⣧⡀⠹⣿⣿⣿⣿
⡿⠟⠉⠛⠿⠦⠴⠞⠛⢁⠀⢸⣿⣿⠋⢠⠀⢻⣿⡇⢸⣿⣿⣿⣿⣾⣿⣿⣿⣿
⠀⠰⣿⣶⣶⣶⣶⠶⠛⡁⠀⣾⣿⡟⠀⣾⡆⠘⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣷⣄⡈⢉⣉⣁⣤⣴⣾⡇⠠⣿⣿⠁⣸⣿⣿⡀⠘⠋⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠻⠇⢀⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""")
        print('Hint: Password is "skibidi" ;) ')
        print('Please Try Again!')
        return brainrot_secret()
    



welcome()

wake_time, sleep_time, available_hours = sleep_wake_times()

all_tasks = add_tasks()

total_hours = build_schedule(all_tasks, available_hours)

save_schedule(all_tasks, available_hours, total_hours,)

brainrot_secret()



# TEST CASES:
# This is program mainly uses inputs that is how I tested what works since errors are usually runtime errors 
# I just wrote them out here! 

# wake_time = 25 or -1  = invalid
# sleep_time < wake_time = invalid
# Hours = str or neg = invalid
# duplicate task =  invalid prints a warning 


