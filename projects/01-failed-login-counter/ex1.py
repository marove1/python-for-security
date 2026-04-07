errors_file = "sample_logs/errors.log"
errors_count = 0

with open(errors_file, "r") as file:
    for line in file:
        if "error" in line:
            errors_count += 1

print(f"The error count is" , errors_count)


