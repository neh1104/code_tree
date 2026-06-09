n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.

class Rltkd():
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

rltkd = [Rltkd(date[i], day[i], weather[i]) for i in range(n)]

Date = '3'
for i in range(n):
    if rltkd[i].weather == 'Rain' and rltkd[i].date < Date:
        Date = rltkd[i].date
        id = i

print(f'{rltkd[id].date} {rltkd[id].day} {rltkd[id].weather}')