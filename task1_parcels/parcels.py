schedules = {
    "Africa": [(5, 13.0), (10, 7.5), (15, 6.5), (20, 5.0)],
    "America": [(5, 13.0), (10, 7.5), (15, 6.5), (20, 5.0)],
    "Antarctica": [(5, 20.0), (10, 10.0), (15, 7.5), (20, 7.0)],
    "Asia": [(5, 12.0), (10, 7.0), (15, 5.5), (20, 4.0)],
    "Europe": [(5, 5.0), (10, 4.0), (15, 2.5), (20, 1.5)],
    "Oceania": [(5, 12.0), (10, 7.0), (15, 5.5), (20, 4.0)],
}

def get_price(cont: str, kg: int) -> float:
    cont_schedule = schedules[cont]

def main():
    kg = get_price("France", 23)
    print(f"kg = {kg}")

if __name__ == '__main__':
    main()
