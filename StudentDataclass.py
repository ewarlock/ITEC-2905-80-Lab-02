import dataclasses
from dataclasses import dataclass
#get dataclass so I can use dataclasses...

#make this class a dataclass
@dataclass
class Student:
    #just need names of properties and data types
    #much more concise than regular class, easier to read/write
    #would probably want to use regular class if I need to do more with the data
    #like calculations and more involved formatting
    name: str
    id: str
    GPA: float

    #str method is built in but can override
    def __str__(self):
        #just prints name and GPA
        return f'Name {self.name}, GPA: {self.GPA}'



def main():
    alex = Student('Alex', 'abcdef', 2.4)
    print(alex.name)
    print(alex.id)
    print(alex) #now calls the str method in Student
    print(alex.GPA)

    alex.GPA = 3.4

    print(alex)

    stacy = Student('Stacy Lastname', '00aa11', 4.0)
    print(stacy)
    print(stacy.id)

if __name__ == '__main__':
    main()