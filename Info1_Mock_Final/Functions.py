def stats(students):
    stud = {}
    subj = {}
    for key in students:
        grade_sum = 0.0
        grades = 0.0
        for topic in students[key]:
            grade_sum += topic[1]
            grades += 1
            subject = topic[0]
            if subject not in subj:
                subj.update({subject: (topic[1], 1.0)})
            else:
                tup = subj.get(subject)
                var_one = tup[0] + topic[1]
                var_two = tup[1] + 1
                subj.update({subject: (var_one, var_two)})
        stud[key] = round(grade_sum / grades, 2)

    final_sub = {}
    for key in subj:
        final_sub[key] = round(subj.get(key)[0] / subj.get(key)[1], 2)
    return (stud, final_sub)

    # DO NOT SUBMIT THE LINES BELOW!


raw = {"12-345-678": [("Math", 5.5), ("Biology", 5.75), ("Latin", 4.25)],
       "09-876-543": [("Latin", 3.5), ("Biology", 4.5)],
       "01-111-111": [("Latin", 4.5), ("Biology", 4.75), ("French", 3.00)],
       }
students, subjects = stats(raw)
assert (len(students) == 3)
assert (len(subjects) == 4)
assert (students["12-345-678"] == 5.17)
assert (subjects["Latin"] == 4.08)
print("bruh")