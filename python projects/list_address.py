names = []
names.append("irum")
print(names)
names.append("saba")
print(names)
names.insert( 2, "ritu")
print(names)
otherNames = ["rosy","rose"]
names.extend(otherNames)
print(names)
first_index = names.index("rosy")
print(first_index)
if "irum" in names:
    print("irum found")
    if "ritu" not in names:
        print("ritu not found")
        names.sort()
        print(names)




