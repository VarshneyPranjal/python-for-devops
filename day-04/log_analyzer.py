import json, pdb                    #pdb is  a python debugger
def read_logs():
    """
    As a devops Engineer we need to read logs on a daily basis and fetch meaningful information.
    """
    with open("app.log","r") as file :
        return file.readlines()

def count_logs(logs):
    log_count = {
        "INFO" : 0,
        "WARNING" : 0,
        "ERROR" : 0
    }
    # pdb.set_trace()           #way to pause program execution and enter an interactive debugging session
    for log in logs:
        if "INFO" in log :
            log_count.update({"INFO" : log_count["INFO"] + 1})
        elif "WARNING" in log:
            log_count.update({"WARNING" : log_count["WARNING"] + 1})
        elif "ERROR" in log:
            log_count.update({"ERROR" :log_count["ERROR"] + 1})
        else :
            pass
    return log_count 

def write_logs(count):
    try :
        with open("log_summary.txt","w+") as json_file :
            # json_file.writelines()
            json.dump(count, json_file)
    except IOError :
        print("File write error. Check permissions or disk space.")
    
logs = read_logs()
count = count_logs(logs)
print(f"count of each logs are :{count}")
write_logs(count)
