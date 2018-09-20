
def check_teen(workers):

    for worker in workers:
        name = worker["name"]
        for child in worker["children"]:
            if child["age"] > 18:
                print(name)


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }]
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }]
}

olga = {
    "name": "olga",
    "age": 41,
    "children": [{
        "name": "kira",
        "age": 1,
    }, {
        "name": "lola",
        "age": 19,
    }]
}

emps = [ivan, darja, olga]

check_teen(emps)
