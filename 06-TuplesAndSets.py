# Tuple like a List are index but unchangable (immutable). Duplicates are allowed
stirzakerFamily = ("Nigel", " Sandra", "Rachael", "Luke", "Florence")

print(stirzakerFamily)

# stirzakerFamily[0] = "Harry Potter"
# stirzakerFamily.append("Harry Potter")


# Sets are like Lists are not index are Unchangable. Duplcates are not allowed
# item cannot be changed, but items can be removed and new ones added
stirzakerFamilySet = {"Nigel", " Sandra", "Rachael", "Luke", "Florence"}
print(stirzakerFamilySet)

jkRowlingSet = {"Harry Potter"}
stirzakerFamilySet.update(jkRowlingSet)
print(stirzakerFamilySet)

# stirzakerFamilySet.discard("Harry Potter")
# print(stirzakerFamilySet)
