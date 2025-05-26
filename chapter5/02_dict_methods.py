marks = {
    "Sabina": 100,
    "PRATIKSHYA": 56,
    "Apsara": 23,
    0: "Sabina"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Sabina": 99, "Renuka": 100})
# print(marks)

print(marks.get("sabina2")) # Prints None
print(marks["sabina2"]) # Returns an error