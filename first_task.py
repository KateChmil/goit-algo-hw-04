def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")
                salary = int(salary)

                total += salary
                count += 1

    except FileNotFoundError:
        print("File not found")
        return 0, 0

    except (ValueError, TypeError):
        print("Invalid data in file")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count

    return total, average




total, average = total_salary("salary.txt")

print(f"Total salary: {total}, Average salary: {average}")