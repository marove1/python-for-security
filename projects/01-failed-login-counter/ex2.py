failed_login = "sample_logs/failed_login.log"

with open(failed_login, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            from_index = parts.index("from")
            ip = parts[from_index + 1]
            print(ip)