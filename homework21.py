text = "Programming is fun!".lower()

def count_func(text):
    new_dict = {}
    for t in text:
        if t.isalpha():
            if t not in new_dict:
                new_dict[t] = 1
            else:
                new_dict[t] += 1
    return new_dict
print(count_func(text))

# ----------------------------------------------------

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

def group_students(data):
    sort_group = {}
    for class_name,student_name in data:
        if class_name not in sort_group:
            sort_group[class_name] = []
        sort_group[class_name].append(student_name)
    return sort_group
print(group_students(students))