s = input('Введите код цвета: ').strip().lower()
d=[]
kr = int(s[:2],16)
zl = int(s[2:4],16)
bl = int(s[4:6],16)
if s=='ffffff':
    print("Введенный цвет - белый")
elif s=='000000':
    print("Введенный цвет - черный")
elif kr==zl==bl and s!='ffffff' and s!='000000':
    print("Введенный цвет - серый")
elif kr>zl and kr>bl:
    print("Введенный цвет ближе к красному")
elif zl>kr and zl>bl:
    print("Введенный цвет ближе к зеленому")
elif bl>zl and bl>kr:
    print("Введенный цвет ближе к синему")
