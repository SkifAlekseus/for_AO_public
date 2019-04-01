from re import findall
from time import time, localtime
from urllib.request import urlopen
from datetime import datetime, timedelta
from tkinter import *

# Лезем в ИнЬтернет за "правильным" времинем
res = urlopen('http://just-the-time.appspot.com/')
result = res.read().strip()
result_str = result.decode('utf-8')

Y = int(findall(r'\d{4}', result_str)[0]) # Год сейчас по GMT
M = int(findall(r'\d{2}', result_str)[2]) # Месяц сейчас по GMT
D = int(findall(r'\d{2}', result_str)[3]) # День сейчас по GMT
h = int(findall(r'\d{2}', result_str)[4]) # Час сейчас по GMT
m = int(findall(r'\d{2}', result_str)[5]) # Минута сейчас по GMT
s = int(findall(r'\d{2}', result_str)[6]) # Секунда сейчас по GMT

time_gmt = datetime(Y, M, D, h, m, s) # Время сейчас по GMT

# Локальное время
a = localtime(time())
local_time = datetime(a[0], a[1], a[2], a[3], a[4], a[5])

gmt = local_time - time_gmt # Отклонение от GMT

def gmt_time(gmt=gmt):
    '''
    Возвращает время GMT
    '''
    a = localtime(time())
    local_time = datetime(a[0], a[1], a[2], a[3], a[4], a[5])
    gmt_time = local_time - gmt
    return gmt_time

def what_next_raid():
    '''
    Возвращает - tuple(назване события,  локация, время до него)
    '''

    now_time = gmt_time()
    Y = int(now_time.strftime("%Y"))
    M = int(now_time.strftime("%m"))
    D = int(now_time.strftime("%d"))

    str_p = 'Праховей'
    str_loc_p = 'Погост'
    str_z = 'Спорные земли'
    str_loc_z = 'Заречье'

    
    # Спорные земли 00-00 мск
    min_time = datetime(Y, M, D, 19, 40, 0)
    max_time = datetime(Y, M, D, 21, 0, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 1-20 мск
    min_time = datetime(Y, M, D, 21, 0, 0)
    max_time = datetime(Y, M, D, 22, 20, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 2-40 мск

    min_time = datetime(Y, M, D, 22, 20, 0)
    max_time = datetime(Y, M, D, 23, 40, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 4-00 мск NEED_TEST
    if datetime(Y, M, D, 23, 40, 0) <= now_time < datetime(Y, M, D, 23, 59, 59):
        min_time = datetime(Y, M, D, 23, 40, 0)
        max_time = datetime(Y, M, D, 1, 0, 0) + timedelta(days=1)
        if min_time <= now_time < max_time:
            return (str_p, str_loc_p, str(max_time - now_time))

    if datetime(Y, M, D, 0, 0, 0) <= now_time < datetime(Y, M, D, 1, 0, 0):
        min_time = datetime(Y, M, D, 23, 40, 0) - timedelta(days=1)
        max_time = datetime(Y, M, D, 1, 0, 0)
        if min_time <= now_time < max_time:
            return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 5-20 мск
    min_time = datetime(Y, M, D, 1, 0, 0)
    max_time = datetime(Y, M, D, 2, 20, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 6-40 мск
    min_time = datetime(Y, M, D, 2, 20, 0)
    max_time = datetime(Y, M, D, 3, 40, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 8-00 мск
    min_time = datetime(Y, M, D, 3, 40, 0)
    max_time = datetime(Y, M, D, 5, 0, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 9-20 мск
    min_time = datetime(Y, M, D, 5, 0, 0)
    max_time = datetime(Y, M, D, 6, 20, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 10-40 мск
    min_time = datetime(Y, M, D, 6, 20, 0)
    max_time = datetime(Y, M, D, 7, 40, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 12-00 мск
    min_time = datetime(Y, M, D, 7, 40, 0)
    max_time = datetime(Y, M, D, 9, 0, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 13-20 мск
    min_time = datetime(Y, M, D, 9, 0, 0)
    max_time = datetime(Y, M, D, 10, 20, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 14-40 мск
    min_time = datetime(Y, M, D, 10, 20, 0)
    max_time = datetime(Y, M, D, 11, 40, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 16-00 мск
    min_time = datetime(Y, M, D, 11, 40, 0)
    max_time = datetime(Y, M, D, 13, 0, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 17-20 мск
    min_time = datetime(Y, M, D, 13, 0, 0)
    max_time = datetime(Y, M, D, 14, 20, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 18-40 мск
    min_time = datetime(Y, M, D, 14, 20, 0)
    max_time = datetime(Y, M, D, 15, 40, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 20-00 мск
    min_time = datetime(Y, M, D, 15, 40, 0)
    max_time = datetime(Y, M, D, 17, 0, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

    # Спорные земли 21-20 мск
    min_time = datetime(Y, M, D, 17, 0, 0)
    max_time = datetime(Y, M, D, 18, 20, 0)
    if min_time <= now_time < max_time:
        return (str_z, str_loc_z, str(max_time - now_time))

    # Праховей 22-40 мск
    min_time = datetime(Y, M, D, 18, 20, 0)
    max_time = datetime(Y, M, D, 19, 40, 0)
    if min_time <= now_time < max_time:
        return (str_p, str_loc_p, str(max_time - now_time))

def what_next_raid_boss():
    '''
    Возвращает - tuple(назване босса, локация, время до него)
    
    '''

    now_time = gmt_time()
    Y = int(now_time.strftime("%Y"))
    M = int(now_time.strftime("%m"))
    D = int(now_time.strftime("%d"))

    str_e = 'Злая Воля'
    str_loc_e = 'Схрон - Шахты'
    str_o = 'Око'
    str_loc_o = 'Погост - Руины Кургана'
    
    # Элементаль 2-00 мск
    min_time = datetime(Y, M, D, 19, 0, 0)
    max_time = datetime(Y, M, D, 23, 0, 0)
    if min_time <= now_time < max_time:
        return(str_e, str_loc_e, str(max_time - now_time))

    # Око 6-00 мск NEED_TEST
    if datetime(Y, M, D, 23, 0, 0) <= now_time < datetime(Y, M, D, 23, 59, 59):
        min_time = datetime(Y, M, D, 23, 00, 0)
        max_time = datetime(Y, M, D, 3, 0, 0) + timedelta(days=1)
        if min_time <= now_time < max_time:
            return(str_o, str_loc_o, str(max_time - now_time))

    if datetime(Y, M, D, 0, 0, 0) <= now_time < datetime(Y, M, D, 3, 0, 0):
        min_time = datetime(Y, M, D, 23, 00, 0) - timedelta(days=1)
        max_time = datetime(Y, M, D, 3, 0, 0)
        if min_time <= now_time < max_time:
            return(str_o, str_loc_o, str(max_time - now_time))

    # Элементаль 10-00 мск
    min_time = datetime(Y, M, D, 3, 0, 0)
    max_time = datetime(Y, M, D, 7, 0, 0)
    if min_time <= now_time < max_time:
        return(str_e, str_loc_e, str(max_time - now_time))

    # Око 14-00 мск
    min_time = datetime(Y, M, D, 7, 0, 0)
    max_time = datetime(Y, M, D, 11, 0, 0)
    if min_time <= now_time < max_time:
        return(str_o, str_loc_o, str(max_time - now_time))

    # Элементаль 18-00 мск
    min_time = datetime(Y, M, D, 11, 0, 0)
    max_time = datetime(Y, M, D, 15, 0, 0)
    if min_time <= now_time < max_time:
        return(str_e, str_loc_e, str(max_time - now_time))

    # Око 22-00 мск
    min_time = datetime(Y, M, D, 15, 0, 0)
    max_time = datetime(Y, M, D, 19, 0, 0)
    if min_time <= now_time < max_time:
        return(str_o, str_loc_o, str(max_time - now_time))

def update():
    '''
    Отрисовка фрейма раз в 5 секунду
    '''
    Label(frame, text=' {: <10s} '.format(what_next_raid()[0]), font=('', 16)).grid(row=0,column=0,sticky=W)
    Label(frame, text=' {: <16s} '.format(what_next_raid()[1]), font=('', 10)).grid(row=0,column=1,sticky=W)
    Label(frame, text=' {: ^7s} '.format(what_next_raid()[2]), font=('', 16)).grid(row=0,column=2,sticky=W)

    Label(frame, text=' {: <10s} '.format(what_next_raid_boss()[0]), font=('', 16)).grid(row=1,column=0,sticky=W)
    Label(frame, text=' {: <16s} '.format(what_next_raid_boss()[1]), font=('', 10)).grid(row=1,column=1,sticky=W)
    Label(frame, text=' {: ^7s} '.format(what_next_raid_boss()[2]), font=('', 16)).grid(row=1,column=2,sticky=W)

    window.after(5000, update)

# Отрисовка окна
window = Tk()
window.title('АО"КМ" - Шо бУит ?')
window.minsize(380,40)
window.resizable(width=False, height=False)
frame = Frame(window)
frame.grid()

update()

window.mainloop()