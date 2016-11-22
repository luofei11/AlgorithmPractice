from collections import deque

class Person(object):
    def __init__(self, id):
        self.id = id
        self.parents = [None, None]
def findBloodRelationship(p1, p2):
    p1Discovered, p2Discovered = deque(), deque()
    p1Discovered.append(p1)
    p2Discovered.append(p2)
    p1Ances, p2Ances = set(), set()
    while p1Discovered or p2Discovered:
        if p1Discovered:
            p1Curr = p1Discovered.popleft()
            if  p1Curr in p2Ances:
                return True
            for parent in p1Curr.parents:
                if parent:
                    p1Discovered.append(parent)
            p1Ances.add(p1Curr)
        if p2Discovered:
            p2Curr = p2Discovered.popleft()
            if p2Curr in p1Ances:
                return True
            for parent in p2Curr.parents:
                if parent:
                    p2Discovered.append(parent)
            p2Ances.add(p2Curr)
    return False

persons = [None for _ in range(10)]
for i in range(10):
    persons[i] = Person(i)

persons[1].parents = [persons[2], persons[3]]
persons[2].parents = [persons[5], persons[6]]
persons[3].parents = [persons[8], persons[9]]
persons[4].parents = [persons[8], persons[9]]
persons[7].parents = [persons[0], None]

print findBloodRelationship(persons[1], persons[7])

