cohort = ['Adele', 'Alicia', 'Christina', 'Cori', 'Elizabeth', 'Fionnie', 'Hunter', 'Ilana', 'Janaki', 'Jen', 'Kamaile', 'Katherine', 'Kieva', 'Liv', 'May', 'Nan', 'Trew', 'Paresa', 'Rachael', 'Rachel', 'Tamara', 'Vicki', 'Yvonne']

def all_pairs(cohort):
    result = []
    for person1 in range(len(cohort)):
            for person2 in range(person1+1,len(cohort)):
                    result.append([cohort[person1],cohort[person2]])
    return result

pairings = all_pairs(cohort)
num_pairs = len(pairings)
print(f"{num_pairs} pairings")
for pair in pairings:
    print(pair)
