schedules = {
    "Africa": [(5, 13.0), (10, 7.5), (15, 6.5), (20, 5.0)],
    "America": [(5, 13.0), (10, 7.5), (15, 6.5), (20, 5.0)],
    "Antarctica": [(5, 20.0), (10, 10.0), (15, 7.5), (20, 7.0)],
    "Asia": [(5, 12.0), (10, 7.0), (15, 5.5), (20, 4.0)],
    "Europe": [(5, 5.0), (10, 4.0), (15, 2.5), (20, 1.5)],
    "Oceania": [(5, 12.0), (10, 7.0), (15, 5.5), (20, 4.0)],
}

class ContinentNotFoundError(Exception):
    pass

def get_price(cont: str, kg: int) -> float:
    cont_schedule = schedules.get(cont, None)
    if cont_schedule is None:
        raise ContinentNotFoundError(f"Continent '{cont}' not found")

def main():
    try:
        kg = get_price("Africa", 23)
        print(f"kg = {kg}")
    except KeyError as exc:
        print(f"Continent not found: {exc}")
    except ContinentNotFoundError as exc:
        print(f"My exception: {exc}")
        raise Exception("xxx") from exc
    except Exception as exc:
        print(f"Unhandled error: {exc}")
        raise
    finally:
        print("Anyway")

if __name__ == '__main__':
    main()
