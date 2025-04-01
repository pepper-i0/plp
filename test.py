languages = ("python", "javascript", "go", "java", "csharp", "go", "ruby", "php", "swift", "kotlin", "typescript")
#del languages[1]
# print(languages[-1])


# print (len(languages))

#for accent in languages[7:]:
#    print(accent)
print(languages.index("java"))


make_map = {
    "python": "py",
    "javascript": "js",
    "go": "g",
    "java": "java",
    "csharp": "cs",
    "ruby": "rb",
    "php": "php",
    "swift": "swift",
    "kotlin": "kt",
    "typescript": "ts"
}
print(make_map)

make_map["ccc"] = "idk"
print("new map:", make_map)

del make_map["ccc"]
print("new map:", make_map)


make_map["ruby"] = "babyS"
print("new map:", make_map)

print(make_map["kotlin"])
print(make_map["php"], ["go"])

