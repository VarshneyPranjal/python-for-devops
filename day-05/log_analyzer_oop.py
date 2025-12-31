import json
class LogAnalyzer :
    def __init__(self, filename, json_object):         #self is like a constructor which calls whenever we create an object
        self.filename = filename
        self.json_object = json_object
    def read_logs(self):
        with open(self.filename,"r") as file:
            return file.readlines()
    def write_logs(self, counts):
        with open(self.json_object,"w+") as file:
            json.dump(counts, file)
    def print_summary(self, counts):
        print(f"log counts of {self.filename} is : {counts}")
    def analyze_logs(self):
        lines = self.read_logs()
        log_count = {"INFO":0, "WARNING":0, "ERROR":0}
        for line in lines :
            if "INFO" in line :
                log_count.update({"INFO" : log_count["INFO"]+1})
            elif "WARNING" in line :
                log_count.update({"WARNING" : log_count["WARNING"]+1})
            elif "ERROR" in line :
                log_count.update({"ERROR" : log_count["ERROR"]+1})
            else:
                pass
        self.write_logs(log_count)
        self.print_summary(log_count)

log_1 = LogAnalyzer("app.log", "output.json")
log_1.analyze_logs()

log_2 = LogAnalyzer("app2.log", "output2.json")
log_2.analyze_logs()   
