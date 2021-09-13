from functools import reduce

students = [
    {
        "name": 'Olawale',
        "age": 19,
        "sex": 'M',
        "dept": 'Computer Science'
    },
    {
        "name": 'Abdullhai',
        "age": 25,
        "sex": 'M',
        "dept": 'Chemistry'
    },
    {
        "name": 'Ahmed',
        "age": 19,
        "sex": 'M',
        "dept": 'Cisco guru'
    }
]


def avg_age(acc, student):
    acc += student["age"]
    return acc / len(students)


reduce(avg_age, students, 0)


def get_dept(item):
    return '{0} is in {1} department and he is {2}'.format(item['name'], item['dept'], 'cool' if item['dept'] == 'Computer Science' else 'lame')


for i in map(get_dept, students):
    print(i)


def get_cs(item):
    return item['dept'] == 'Computer Science'


print(filter(lambda student: student["dept"] == 'Computer Science', students))

# Square
my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

# List sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(lambda x: x[1])

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

new_list = list({char for char in some_list if some_list.count(char) > 1})
print(new_list)
