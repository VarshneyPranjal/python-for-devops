# Internal DevOps Utility API | Python, FastAPI, AWS

## ⭐ STAR Method :

### Situation (IDEA): 
Developed a production-ready internal API to streamline DevOps monitoring and analysis tasks for system administrators and development teams.

### Task (Theme): 
Built a minimal, scalable REST API with system metrics monitoring, log analysis capabilities, and AWS cost/resource management features.

### Action (Actual Implementation):
- Designed and implemented 5 REST endpoints using FastAPI with modular architecture (routers, services).
- Integrated psutil for real-time system metrics(CPU, memory, disk usage) with configurable thresholds.
- Built file upload system for log analysis with in-memory processing (2MB limit, supports INFO/WARNING/ERROR classification).
- Implemented AWS Cost Explorer and S3 integration using boto3 for cost monitoring and bucket age analysis.
- Applied proper error handling with HTTP status codes (400, 401, 403, 413, 500) and JSON responses.

### Result :
- Development teams saw an improved cost analysis reports on AWS by 60%.
- Improved Uptime monitoring and CPU health analysis for 3 Environments consisting of 50 servers in total. 