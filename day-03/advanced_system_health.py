import psutil, requests, json

# Improve system_health.py file by using try-except concept 
#1st APPROACH
def checkSystemHealth():
    while True:
        try:
            cpu_threshold = int(input("Enter CPU Usage: "))
            memory_threshold = int(input("Enter Memory Usage: " ))
            disk_threshold = int(input("Enter Disk Usage: "))
            break
        except ValueError:
            print("Invalid input! Please Enter integers only.")

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

#2nd APPROACH (more-concise)
def checkHealth():
    component = input("Enter component (CPU, DISK, MEMORY): ").upper()
    if component not in ("CPU", "DISK", "MEMORY"):
        print("Invalid input! Please enter CPU, DISK, or MEMORY.")
    if component == "CPU" :
        usage = psutil.cpu_percent(interval=1)
    elif component == "DISK" :
        usage = psutil.disk_usage('.')
    else:
        usage = psutil.virtual_memory()

    try:
        threshold = int(input(f"Enter {component} threshold: "))
    except :
        print("Invalid input! Please Enter integer only")

    if component == "CPU":
        if usage > threshold:
            print(f"{component} Usage: {usage}\n")
            print(f"WARNING: High {component} usage!")
        else:
            print(f"{component} is in Safe State")
    elif usage.total > threshold:
        print(f"{component} Usage: {usage}\n")
        print(f"WARNING: High {component} usage!")
    else:
        print(f"{component} is in Safe State")
# checkHealth()

# Improve api_data_fetcher.py file by using try-except concept 
def getCatFacts():
    base_url = "https://catfact.ninja/fact"
    try: 
        response = requests.get(url=base_url)
        # print(response.json()["fact"])
        with open('processed_data.json', 'w') as f:
            json.dump(response.json()["fact"], f, indent=4)
            print("Data saved to processed_data.json")
    except requests.exceptions.Timeout:
        print("Request timed out. Please check your internet connection.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

    except ValueError:
        print("Invalid JSON received from API.")

    except KeyError:
        print("Expected key 'fact' not found in response.")

    except IOError:
        print("File write error. Check permissions or disk space.")
getCatFacts()