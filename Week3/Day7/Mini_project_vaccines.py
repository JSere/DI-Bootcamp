class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans = [person] + self.humans
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        for idx in range(len(self.humans)):
            if self.humans[idx] == person:
                return idx
        return -1

    def swap(self, person1, person2):
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        if idx1 != -1 and idx2 != -1:
            self.humans[idx1], self.humans[idx2] = self.humans[idx2], self.humans[idx1]

    def get_next(self):
        if not self.humans:
            return None
        next_person = self.humans[0]
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type):
        for idx in range(len(self.humans)):
            if self.humans[idx].blood_type == blood_type:
                person = self.humans[idx]
                self.humans = self.humans[:idx] + self.humans[idx+1:]
                return person
        return None

    def sort_by_age(self):
        def custom_key(p):
            priority_rank = 0 if p.priority else 1
            age_rank = -p.age
            return (priority_rank, age_rank)

        n = len(self.humans)
        for i in range(n):
            for j in range(0, n - i - 1):
                if custom_key(self.humans[j]) > custom_key(self.humans[j+1]):
                    self.humans[j], self.humans[j+1] = self.humans[j+1], self.humans[j]

    def rearrange_queue(self):
        if len(self.humans) <= 2:
            return

        rearranged = [self.humans[0]]
        remaining = self.humans[1:]

        while remaining:
            placed = False
            for i in range(len(remaining)):
                candidate = remaining[i]
                if candidate not in rearranged[-1].family:
                    rearranged.append(candidate)
                    remaining = remaining[:i] + remaining[i+1:]
                    placed = True
                    break
            if not placed:
                rearranged.append(remaining[0])
                remaining = remaining[1:]

        self.humans = rearranged


h1 = Human("1", "Alice", 25, False, "A")
h2 = Human("2", "Bob", 65, False, "B")
h3 = Human("3", "Charlie", 30, True, "O")
h4 = Human("4", "Diana", 40, False, "AB")

h1.add_family_member(h2)

q = Queue()
q.add_person(h1)
q.add_person(h2)
q.add_person(h3)
q.add_person(h4)

print("Initial queue:")
for h in q.humans:
    print(h.name)

next_p = q.get_next()
print(f"\nNext vaccinated: {next_p.name}")

blood_p = q.get_next_blood_type("A")
print(f"Next blood type A: {blood_p.name if blood_p else 'None'}")