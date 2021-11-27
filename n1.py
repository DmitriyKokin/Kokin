step = input(f'Введите направление, куда вы хотите пойти: "up" "down" "left" "right"\nсейчас вы находитесь в точке 0:0\n')
distance = int(input(f'\n а так же шаг, на сколько вы пойдете (int) :'))
pnt = [int(0),int(0)]
if step == 'up':
    pnt[1]+=distance
elif step == 'down':
    pnt[1]-=distance
elif step == 'left':
    pnt[0]-=distance
elif step == 'right':
    pnt[0]+=distance
else:
    print(f"error")
    exit()
print (f'{pnt}')