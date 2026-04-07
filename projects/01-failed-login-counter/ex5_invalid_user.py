log_file = "sample_logs/auth.log"

with open(log_file, "r") as file:
    for line in file:
        if "invalid" in line:
            print(line.strip())


