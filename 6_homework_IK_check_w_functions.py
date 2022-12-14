#Define functions

def gender(ik):  #check gender from IK
    if int(ik[0]) % 2 == 0:  #если кратно двум, то женщина
        return('You are female')
    else:
        return('You are male')


def dob(ik):  #check date of birth
    if ik[0] in ['1', '2']:  # проверяем первое число из ИК, если ли оно среди значений в квадратных скобках 1 и 2
        bcent = '18'  # генерируем приставку столетия. Если в начале ИК 1 или 2 значит человек родился в 19 веке
    elif ik[0] in ['3', '4']:  #если первое число ряда содержит в себе элементы списка 3 или 4
        bcent = '19' # генерируем приставку столетия. Если в начале ИК 3 или 4 значит человек родился в 20 веке
    elif ik[0] in ['5', '6']:
        bcent = '20'
    elif ik[0] in ['7', '8']:
        bcent = '21'
    else:
        return('Cant determine your date of birth!')

    return(f'DOB is: {ik[5:7]}.{ik[3:5]}.{bcent}{ik[1:3]}')  #выводим индексами кусочки ИК, содержащие дату рождения


def birthplace(ik):  #check birth place
    bplace = (ik[7:10])  #проверяем три знака ИК, в которых закодировано место рождения
    if bplace > '0' and bplace < '011':
        return('Your birthplace is Kuressaare haigla')
    elif bplace > '010' and bplace < '020':
        return('Your birthplace is Tartu Ülikooli Naistekliinik')
    elif bplace > '020' and bplace < '151':
        return('Your birthplace is Tallinn >> Ida-Tallinna keskhaigla OR Pelgulinna sünnitusmaja')
    elif bplace > '150' and bplace < '161':
        return('Your birthplace is Keila haigla')
    elif bplace > '160' and bplace < '221':
        return('Your birthplace is Rapla haigla OR Loksa haigla OR Hiiumaa haigla (Kärdla)')
    elif bplace > '220' and bplace < '271':
        return('Your birthplace is Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
    elif bplace > '270' and bplace < '371':
        return('Your birthplace is Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
    elif bplace > '370' and bplace < '421':
        return('Your birthplace is Narva haigla')
    elif bplace > '420' and bplace < '471':
        return('Your birthplace is Pärnu haigla')
    elif bplace > '470' and bplace < '491':
        return('Your birthplace is Haapsalu haigla')
    elif bplace > '490' and bplace < '521':
        return('Your birthplace is Järvamaa haigla (Paide)')
    elif bplace > '520' and bplace < '571':
        return('Your birthplace is Rakvere haigla, Tapa haigla')
    elif bplace > '570' and bplace < '601':
        return('Your birthplace is Valga haigla')
    elif bplace > '600' and bplace < '651':
        return('Your birthplace is Viljandi haigla')
    elif bplace > '650' and bplace < '701':
        return('Your birthplace is Lõuna-Eesti haigla (Võru) OR Põlva haigla')
    else:
        return('Your birthplace is outside Estonia!')

def validity(ik):  #check if IK is valid using official method, described in Wiki.

    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]  #check number row 1
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]  #checj number row 2

    res = 0  # переменная для суммы
    for num in range(10):  # заряжаем диапазон счётчика - 10 итераций
        res += chk1[num] * int(ik[num])  #к результату РЕС будет прибавляться поочерёдно произведение от переменной ИК на первый проверочный ряд. С каждой
        #итерацией цикл ФОР подставит новый индекс и к результату будет прибавлено произведение от умножения следующей пары. Индексы от 0 до 9.
    if res % 11 < 10 and int(ik[-1]) == res % 11:  #здесь мы берём индекс от конца, поэтому первое число с конца будет -1.
        # Если остаток от деления меньше 10, то он проверочное число и должен быть равен первому числу от конца ИК.
        #остаток от деления будет округляться. Например 17.09 даст остаток 1, 10.17 - 2.
        return('Valid by 1 check!')

    else:  #если не прокатило, используем второй проверочный ряд
        res = 0  #в переменной есть значение, её надо обнулить
        for num in range(10):
            res += chk2[num] * int(ik[num])  #снова набиваем в переменнную сумму всех перемноженных между собой пар

        if res % 11 < 10 and int(ik[-1]) == res % 11:  # здесь мы берём индекс от конца, поэтому первое число с конца будет -1.
            # Если остаток от деления меньше 10, то он проверочное число и должен быть равен первому числу от конца ИК.
            return('Valid by 2 check!')
        elif res % 11 >= 10 and int(ik[-1]) == int(0): #если остаток от деления больше или равен 10, то проверочное число ноль.
            return('Valid by 2 check, last is zero!')
        else:
            return('IK is invalid!')  #если ничего не подошло, исикукоод левый


def enter_ik():  #define function that receive IK input from user, check if it is correct and return correct IK to main loop
    while True:  # без цикла While невозможно возвращаться к началу программы бесконечно, столько сколько нужно. Так мы делаем Main loop
        try:
            ik = input('Enter ID code')
            int(ik)  # смена типа переменной со строки на целое число
            if len(ik) != 11:  # if not equal 11
                raise UserWarning
        except ValueError:
            return('Code you entered is not numeric!')
        except UserWarning:
            if len(ik) > 11:
                return ('Code is longer then 11 digits')
            else:
                return('Code is shorter then 11 digits')
        else:
            return(ik)  #all correct, return IK value

#############################################################
#MAIN LOOP

#receive IK
ik = enter_ik()
print(ik)

#let user to choose what to do with entered IK
while True:

    user_choice = input(
        'Please choose:\n1.print gender\n2.Print date of birth\n3.Print Region\n4.Validate ID\n5.Change ID\n0.Exit\n-->')
    if user_choice == '1':
        print(gender(ik))
    if user_choice == '2':
        print(dob(ik))
    if user_choice == '3':
        print(birthplace(ik))
    if user_choice == '4':
        print(validity(ik))
    if user_choice == '5':
        ik = enter_ik()
        print(ik)
    if user_choice == '0':
        print('Bye!')
        quit()
#######################################################

#some existing IK to check
#  38803160272
#  38006180285
#  49103197011

