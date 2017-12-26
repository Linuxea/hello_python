import json

stu = {
    "name" : "linuxea",
    "age" : 13,
    "hobby" : [
        "footall", "basketball", "pingpong"
    ]
}

print(stu["name"])

print(json.dumps(stu))
