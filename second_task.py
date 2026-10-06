def get_cats_info(path):
    cats = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            id, name, age = line.split(",")

            cat = {
                "id": id,
                "name": name,
                "age": age
            }

            cats.append(cat)

    return cats