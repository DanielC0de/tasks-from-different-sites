
def replace_first(items: list):
    if len(items) != 0:
        a = items[0]
        items.remove(a)
        items.append(a)
    return items


i = []
print(replace_first(i))
