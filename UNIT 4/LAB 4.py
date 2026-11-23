import json
try:
    with open("logs.json", "r") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Invalid JSON data: Expected a list of logs.")
    info_count = 0
    warning_count = 0
    error_count = 0
    print("\n----- ALL LOG RECORDS -----")
    for log in data:
        if not isinstance(log, dict):
            print("Invalid log record:", log)
            continue
        timestamp = log.get("timestamp", "N/A")
        level = log.get("level", "N/A")
        message = log.get("message", "N/A")
        print("Timestamp:", timestamp)
        print("Level:", level)
        print("Message:", message)
        print("--------------------------")
        level = str(level).upper()
        
     
if level == "INFO":
            info_count += 1
        elif level == "WARNING":
            warning_count += 1
        elif level == "ERROR":
            error_count += 1
    print("\n----- LOG SUMMARY -----")
    print("Total INFO messages:", info_count)
    print("Total WARNING messages:", warning_count)
    print("Total ERROR messages:", error_count)
    print("Total log records:", len(data))
except FileNotFoundError:
    print("Error: logs.json file not found.")
except json.JSONDecodeError:
    print("Error: Invalid JSON data in logs.json.")
except ValueError as e:
    print(e)
Code for logs.json:
[
    {
        "timestamp": "10:00",
        "level": "INFO",
        "message": "Application started"
    },
{
        "timestamp": "10:05",
        "level": "WARNING",
        "message": "Low memory detected"
    },
    {
        "timestamp": "10:10",
        "level": "ERROR",
        "message": "Database connection failed"
    },
    {
        "timestamp": "10:15",
        "level": "INFO",
        "message": "User logged in"
    },
    {
        "timestamp": "10:20",
        "level": "ERROR",
        "message": "File not found"
    },
    {
        "timestamp": "10:25",
        "level": "WARNING",
        "message": "High CPU usage"
    }
]

