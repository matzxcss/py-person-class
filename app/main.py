class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = []
    husband_list = []
    wife_list = []

    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_list.append(new_person)

        if "wife" in person:
            husband_list.append((new_person, person["wife"]))
        if "husband" in person:
            wife_list.append((new_person, person["husband"]))

    for husband, wife_name in husband_list:
        wife = Person.people.get(wife_name)
        if wife:
            husband.wife = wife

    for wife, husband_name in wife_list:
        husband = Person.people.get(husband_name)
        if husband:
            wife.husband = husband

    return person_list
