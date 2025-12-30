def read_users(path='users.txt'):
    users = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Expect lines like: Name, 34
                if ',' in line:
                    name, age_part = line.split(',', 1)
                    name = name.strip()
                    try:
                        age = int(age_part.strip())
                    except ValueError:
                        # skip lines with non-integer ages
                        continue
                    users.append((name, age))
                else:
                    # skip lines without an age
                    continue
    except FileNotFoundError:
        print(f"File not found: {path}")
    return users


def filter_over_age(users, min_age=21):
    return [u for u in users if u[1] > min_age]


def print_sorted_by_age(users):
    for name, age in sorted(users, key=lambda t: t[1]):
        print(f"{name}, {age}")


def main(path='users.txt'):
    users = read_users(path)
    adults = filter_over_age(users, 21)
    print_sorted_by_age(adults)


if __name__ == '__main__':
    main()