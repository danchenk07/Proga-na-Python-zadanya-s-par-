n = int(input('Введите количество людей: '))
d=[]
for _ in range(1,n+1):
    i = int(input(f'Ввдите возраст {_}-ого человека: '))
    d.append(i)
print(f"Средний возраст всех людей: {sum(d)//len(d)}")