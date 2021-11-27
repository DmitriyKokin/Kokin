def usererror():
    print(f"USER Error")
    exit()

pnt = [int(0),int(0)]
step = input(f'Введите направление, куда вы хотите пойти: "up" "down" "left" "right"\nсейчас вы находитесь в точке {pnt[0]}:{pnt[1]}\n"finish" для окончания\n')
if step != 'up' and step != 'down' and step != 'left' and step != 'right' and step != 'finish':
    usererror()
if step == 'finish':
    print(f'see you again :)\n')
try:
    distance = int(input('Введите условное расстояние, которое вы преодолеете\n'))
except:
   usererror()
flag = False
while step != 'finish':
    if flag:
        step = input(f'Направление (или "finish"): ')
        if step == 'finish':
            print(f"see you again :)\nx={pnt[0]} y={pnt[1]}")
            break
        try:
            distance = int(input(f'шаг, на сколько вы пойдете (int) :'))
        except:
             usererror()
    flag=True
    if step == 'up':
        pnt[1]+=distance
    elif step == 'down':
        pnt[1]-=distance
    elif step == 'left':
        pnt[0]-=distance
    elif step == 'right':
        pnt[0]+=distance
    else:
        print(f"incorrect command\nx={pnt[0]} y={pnt[1]}")
        exit()
    print (f'x={pnt[0]} y={pnt[1]}')