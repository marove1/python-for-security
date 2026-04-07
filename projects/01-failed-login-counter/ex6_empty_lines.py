log_file = "sample_logs/empty_lines.log"
empty_count = 0

with open (log_file, "r") as file:
    for line in file:
        if line.strip() == "":
            empty_count += 1
print("Empty lines: ", empty_count)