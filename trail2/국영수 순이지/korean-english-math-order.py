n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.

student = [(name[i], korean[i], english[i], math[i]) for i in range(n)]

student.sort(key = lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
    name = student[i][0]; kor = student[i][1]; eng = student[i][2]; math = student[i][3]
    print(name, kor, eng, math)