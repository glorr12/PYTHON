from collections import Counter
text = "Programming is fun!".lower()
letter = [t for t in text if t.isalpha()]
print(dict(Counter(letter)))



# ----------------------------------------------------
from collections import defaultdict
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def group_students(data):
    sort_group = defaultdict(list)
    for class_name,student_name in data:
        sort_group[class_name].append(student_name)
    return dict(sort_group)
print(group_students(students))



