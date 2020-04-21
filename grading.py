def gradingStudents(grades):
    final=list()
    for i in grades:
        if (i>=38) and (i%5)>=3:
            final.append((i+5)-(i%5))
        else:
            final.append(i)
    return final
