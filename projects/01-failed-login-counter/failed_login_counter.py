log_file = "sample_logs/auth.log"
failed_count = 0
ip_counts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_count += 1

            parts = line.split()
            from_index = parts.index("from")
            ip = parts[from_index + 1]

            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

print("Total failed login attempts:", failed_count)
print()
print("Failed attempts by IP:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count}")