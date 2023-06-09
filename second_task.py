import re


def fill_base() -> dict:
    result = {}
    with open('data_for_2_task', encoding='utf-8') as file:
        for row in file.readlines():
            row = row.strip()
            name, hours = re.findall(r'(.+?) (\d+)', row)[0]
            result[name] = result.get(name, []) + [hours]
    return result


def print_hours(employees: dict) -> None:
    for name, hours in employees.items():
        print(f"{name}: {', '.join(hours)}; sum: {sum(map(int,hours))}")


if __name__ == "__main__":
    employees = fill_base()
    print_hours(employees)
