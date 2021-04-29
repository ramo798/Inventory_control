import get_items
import collections

all_items = []
users = ["younghoho_1121", "tomokimi_777"]
# users = ["tomokimi_777"]

for user in users:
    sc_data = get_items.get_items(user)
    for item in sc_data:
        all_items.append(item)

hikaku = []
for item in all_items:
    hikaku.append(item["measuring"]["id"])

tyouhuku = [k for k, v in collections.Counter(hikaku).items() if v > 1]

print(tyouhuku)

for item in all_items:
    if item["measuring"]["id"] in tyouhuku:
        print(item["url"])
