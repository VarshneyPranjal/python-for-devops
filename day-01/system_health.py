import psutil 

def checkSystemHealth():
    cpu_threshold = int(input("Enter CPU Usage: "))
    memory_threshold = int(input("Enter Memory Usage: "))
    disk_threshold = int(input("Enter Disk Usage: "))

    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%") 
    if cpu_threshold > cpu_usage :
        print("WARNING: High CPU usage!")
    else:
        print("CPU is in Safe State")

    # Memory Usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    if memory.total > memory_threshold:
        print("WARNING: High Memory usage!")
    else:
        print("Memory is in Safe State")
    
    #Disk Usage
    disk = psutil.disk_usage('.')
    print(f"Disk Usage: {disk}%")
    if disk.total > disk_threshold:
        print("WARNING: High Disk usage!")
    else:
        print("Disk is in Safe State")

# checkSystemHealth()

def checkHealth():
    user_input = input("Enter which computer component you want to check health usage of (CPU, DISK, MEMORY) :")
    if user_input == "CPU" :
        usage = psutil.cpu_percent(interval=1)
    elif user_input == "DISK" :
        usage = psutil.disk_usage('.')
    else:
        usage = psutil.virtual_memory()

    threshold = int(input(f"Enter {user_input} threshold: "))

    if user_input == "CPU":
        if usage > threshold:
            print(f"{user_input} Usage: {usage}\n")
            print(f"WARNING: High {user_input} usage!")
        else:
            print(f"{user_input} is in Safe State")
    elif usage.total > threshold:
        print(f"{user_input} Usage: {usage}\n")
        print(f"WARNING: High {user_input} usage!")
    else:
        print(f"{user_input} is in Safe State")

checkHealth()
    