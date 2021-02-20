cohort = ['Adele', 'Alicia', 'Christina', 'Cori', 'Elizabeth', 'Fionnie', 'Hunter', 'Ilana', 'Janaki', 'Jen', 'Kamaile', 'Katherine', 'Kieva', 'Liv', 'May', 'Nan', 'Trew', 'Paresa', 'Rachael', 'Rachel', 'Tamara', 'Vicki', 'Yvonne']

pair_list = []
# 
# print(range[0:25])
#
# def all_pairs(cohort):
#     if len(cohort) % 2 == 1:
#         # Handles odd class size:
#         for i in range(len(cohort)):
#             for result in all_pairs(cohort[:i] + cohort[i+1:]):
#                 pair_list.append(result)
#                 print(pair_list)
#     else:
#         a = cohort[0]
#         for x in range(1,len(cohort)):
#             pair = (a,cohort[x])
#             for rest in all_pairs(cohort[1:x]+cohort[x+1:]):
#                 yield [pair] + rest
#
# for n in all_pairs(cohort):
#     print(n)



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
