log_file = "sample_logs/auth.log"
username_counts = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()

            if "invalid" in parts and "user" in parts:
                user_index = parts.index("user")
                username = parts[user_index + 1]
            else:
                for_index = parts.index("for")
                username = parts[for_index + 1]

            if username in username_counts:
                username_counts[username] += 1
            else:
                username_counts[username] = 1

print("Failed attempts by username:")
for username, count in username_counts.items():
    print(f"{username}: {count}")