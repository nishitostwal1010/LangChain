from typing import TypedDict

class Person(TypedDict):
    
    name: str
    age: int

new_person: Person = {'name':'nishit', 'age': 21}

print(new_person)
