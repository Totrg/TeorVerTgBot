import random as r
import math as m
from fractions import Fraction

names_set = ["Саша", "Вася", "Петя", "Дима", "Гоша", "Олег", "Маша", "Настя"]
colors_set = ["синие", "красные", "зеленые", "желтые", "оранжевые", "белые", "фиолетовые"]
problem, answer, solving = "", 0, ""


def CombinatoricsPermutationsEasy():
    rand1 = r.randint(0, len(names_set) - 1)
    rand2 = r.randint(0, len(names_set) - 1)
    count = r.randint(3, 8)
    word = "разных"
    if count <= 4:
        word = "разные"
    else:
        word = "разных"
    while rand1 == rand2:
        rand2 = r.randint(0, len(names_set) - 1)
    problemtmp = names_set[rand1] + " и " + names_set[
        rand2] + " играют в игру. " + str(
        count) + f" {word} игрушек стоят в ряд. Игроку за один ход нужно за ограниченное время переставить игрушки местами так, чтобы их порядок не повторялся. Сколько максимально уникальных перестановок сможет сделать игрок?"
    answertmp = m.factorial(count)
    solvingtmp = "Применим формулу числа перестановок n объектов:\nP = n!\nP = " + str(count) + "! = " + str(
        answertmp) + "\nОтвет: " + str(answertmp)
    return [problemtmp, answertmp, solvingtmp, 5]


def CombinatoricsPermutationsHard():
    rand1 = r.randint(0, len(names_set) - 1)
    rand2 = r.randint(0, len(names_set) - 1)
    rand3 = r.randint(0, len(colors_set) - 1)
    rand4 = r.randint(0, len(colors_set) - 1)
    count = r.randint(4, 9)
    split = r.randint(2, count - 2)
    word = "мяча"
    if count <= 4:
        word = "мяча"
    else:
        word = "мячей"
    while rand1 == rand2:
        rand2 = r.randint(0, len(names_set) - 1)
    while rand3 == rand4:
        rand4 = r.randint(0, len(colors_set) - 1)
    problemtmp = names_set[rand1] + " и " + names_set[
        rand2] + " играют в игру. " + str(
        count) + f" {word} разных цветов стоят в ряд, при чем " + str(count - split) + " из них " + colors_set[
                     rand3] + ", а " + str(split) + " - " + colors_set[
                     rand4] + ". Игроку за один ход нужно за ограниченное время переставить мячи местами так, чтобы их порядок не повторялся. Сколько максимально уникальных перестановок сможет сделать игрок?"
    answertmp = m.factorial(count) // (m.factorial(count - split) * m.factorial(split))
    solvingtmp = "Применим формулу числа перестановок n объектов\nP = n!\nНо важно учитывать, что не все объекты уникальны, а следовательно существуют перестановки между одним типом объектов, что не влияет на общий вид перестановки, а следовательно мы получаем лишние перестановки, чтобы их исключить, разделим на произведение количества перестановок между не уникальными объектами:\nP = (" + str(
        count) + "!) / (" + str(count - split) + "! * " + str(split) + "!) = " + str(answertmp) + "\nОтвет: " + str(
        answertmp)
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsCombinations():
    rand1 = r.randint(0, len(names_set) - 1)
    n = r.randint(3, 8)
    k = r.randint(2, n - 1)
    vil = r.randint(0, 1)
    if vil == 0:
        word = "фрукта"
        if k <= 4:
            word = "фрукта"
        else:
            word = "фруктов"
        problemtmp = names_set[rand1] + " складывает фрукты в ящик. В один ящик вмещается " + str(
            k) + f" {word}, а всего фруктов - " + str(n) + ". Сколькими способами " + names_set[
                         rand1] + " сможет сложить фрукты в ящик? (Подразумевается, что останутся лишние фрукты)"
        answertmp = m.factorial(n) // (m.factorial(n - k) * m.factorial(k))
        solvingtmp = "Применим формулу числа сочетаний по k из n объектов:\nC = (n!) / ((n-k)! * k!)\nC = (" + str(
            n) + f"!) / (({n}-{k})! * {k}!) = {answertmp}\nОтвет: {answertmp}"
        return [problemtmp, answertmp, solvingtmp, 10]
    else:
        word = "вещи"
        if k <= 4:
            word = "вещи"
        else:
            word = "вещей"
        problemtmp = f"{names_set[rand1]} торопится на прогулку, и хочет взять {k} {word}, чтобы похвастаться друзьям. Всего вещей дома - {n}. Сколькими способами {names_set[rand1]} сможет это сделать?"
        answertmp = m.factorial(n) // (m.factorial(n - k) * m.factorial(k))
        solvingtmp = "В данном случае нам не важен порядок сочетаний, следовательно применим формулу числа сочетаний по k из n объектов:\nC = (n!) / ((n-k)! * k!)\nC = (" + str(
            n) + f"!) / (({n}-{k})! * {k}!) = {answertmp}\nОтвет: {answertmp}"
        return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsCombinationsP():
    n = r.randint(4, 8)
    k = r.randint(3, n - 1)
    word1 = "друга"
    if k <= 4:
        word1 = "друга"
    else:
        word1 = "друзей"
    word2 = "кнопки"
    if n <= 4:
        word2 = "кнопки"
    else:
        word2 = "конопок"
    problemtmp = f"{k} {word1} хотят купить мороженого из автомата. У автомата есть {n} {word2}, по нажатию на каждую из которых автомат выдает мороженное с разными вкусами. Определите, сколькими способами друзья смогут купить мороженое, если каждый из них купил себе по одному."
    answertmp = m.factorial(n + k - 1) // (m.factorial(k) * m.factorial(n - 1))
    solvingtmp = f"Раз друзья могут выбрать мороженное одного вкуса, а также нам не важно кто конкретно из друзей какое мороженное выбрал (не важен порядок внутри сочетания), то для решения этой задачи следует применить формулу сочетаний с повторениями по k из n объектов:\nCr = (n+k-1)! / (k! * (n-1)!)\nCr = ({n}+{k}-1)! / ({k}! * ({n}-1)!) = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsAllocationsP():
    rand1 = r.randint(0, 5)
    n = r.randint(3, 8)
    k = r.randint(2, n - 1)
    word = "буквы"
    if n <= 4:
        word = "буквы"
    else:
        word = "букв"
    problemtmp = f"{names_set[rand1]} сочиняет собственный язык. Он придумал {n} {word}, и начал, перебирая их, составлять слова из {k} букв, выбирая эти буквы среди придуманных. Сколько разных слов может составить {names_set[rand1]}?"
    answertmp = n ** k
    solvingtmp = f"Заметим, что {names_set[rand1]} может составить слово из {k} одинаковых букв. В данном случае нам следует применить формулу размещений с повторениями из n по k объектов:\nAr = n**k (символы ** обозначают возведение в степень)\nAr = {n}**{k} = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsAllocations():
    rand1 = r.randint(0, 5)
    n = r.randint(3, 9)
    k = r.randint(2, n - 1)
    word1 = "ведра"
    if n <= 4:
        word1 = "ведра"
    else:
        word1 = "вёдер"
    word2 = "домика"
    if k <= 4:
        word2 = "домика"
    else:
        word2 = "домиков"
    problemtmp = f"{names_set[rand1]} хочет построить улицу из песка, в которой будет {k} {word2}. Перед ним также лежит {n} {word1}. Под улицей подразумевается ряд объектов, порядок которых также важен мальчику. Сколько разных улиц сможет построить {names_set[rand1]}, если он хочет, чтобы все домики были разной формы?"
    answertmp = m.factorial(n) // m.factorial(n - k)
    solvingtmp = f"Применим формулу размещений из n по k объектов:\nA = n! / (n-k)!\nA = {n}! / ({n}-{k})! = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsSummationEasy():
    rand1 = r.randint(0, len(names_set) - 1)
    rand2 = r.randint(0, len(names_set) - 1)
    n1 = r.randint(2, 8)
    n2 = r.randint(2, 8) + 1
    problemtmp = f"{names_set[rand1]} и {names_set[rand2]} играют в игру. У каждого есть куча разных уникальных камней - по {n1} и {n2} соответственно. Каждый игрок меняет порядок камней, при чем каждая получившаяся комбинация уникальна (не повторялась этим игроком). Сколько комбинаций суммарно смогут составить {names_set[rand1]} и {names_set[rand2]}?"
    answertmp = m.factorial(n1) + m.factorial(n2)
    solvingtmp = f"Заметим, что у нас имеется две независимые выборки, то есть какое бы действие не сделал первый игрок, для второго игрока ничего не поменяется, тогда мы можем применить правило суммы (P(общ) = P1+P2+...+Pn). Применим также формулу числа перестановок n объектов:\nP = n!\nP1 = {n1}! = {m.factorial(n1)}\nP2 = {n2}! = {m.factorial(n2)}\nP(общее) = P1 + P2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsSummationCombinations():
    n1 = r.randint(3, 8)
    n2 = r.randint(3, 8)
    k1 = r.randint(2, n1 - 1)
    k2 = r.randint(2, n2 - 1)
    problemtmp = f"Два студента тянут билеты на экзамене в разных аудиториях. Первый студент вытягивает из {n1} билетов {k1}, а второй из {n2} билетов вытягивает {k2}. Сколькими комбинациями суммарно студенты смогли бы вытянуть билеты?"
    C1 = (m.factorial(n1) // (m.factorial(n1 - k1) * m.factorial(k1)))
    C2 = (m.factorial(n2) // (m.factorial(n2 - k2) * m.factorial(k2)))
    answertmp = C1 + C2
    solvingtmp = f"Заметим, что у нас имеется две независимые выборки, то есть какие бы билеты не вытянул первый студент, для второго ничего не поменяется, тогда мы можем применить правило суммы (C(общ) = C1+C2+...+Cn). Применим также формулу числа сочетаний по k из n объектов:\nC = (n!) / ((n-k)! * k!)\nC1 = ({n1}!) / (({n1}-{k1})! * {k1}!) = {C1}\nC2 = ({n2}!) / (({n2}-{k2})! * {k2}!) = {C2}\nC(общ) = C1 + C2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 15]


def CombinatoricsSummationAllocationsP():
    rand1 = r.randint(0, 5)
    n = r.randint(4, 8)
    k1 = r.randint(2, n - 2)
    k2 = k1 + 1
    word1 = "фишки"
    word2 = "фишки"
    if k1 > 4:
        word1 = "фишек"
    if k2 > 4:
        word2 = "фишек"
    problemtmp = f"{names_set[rand1]} играет в монополию, и чтобы сделать ход, он должен сделать ставку - положить несколько фишек из собственного запаса на игровое поле. Всего в игре есть {n} типов фишек с разными рисунками на них. {names_set[rand1]} решил поставить ставку с закрытыми глазами - так интереснее. {names_set[rand1]} очень преуспел в этой игре, у него в запасе лежит неограниченное количество всех типов фишек, и при этом в руку у него помещается только от {k1} до {k2} фишек, и вытащить из своего запаса соответственно он может как {k1}, так и {k2}. Затем {names_set[rand1]} выкладывает фишки на игровое поле в линию. Укажите, сколько всевозможных комбинаций из фишек может лежать по итогу на поле (порядок также важен)?"
    answertmp = n ** k1 + n ** k2
    solvingtmp = f"Заметим, что {names_set[rand1]} может выложить на поле фишки таким образом, что они все будут одинакового типа. Также следует понимать, что от нас требуют количества исходов ЛИБО что выложены {k1} {word1}, ЛИБО что {k2} {word2}. В данном случае нам следует применить правило сложения (Ar(общ)=Ar1+Ar2+...+Arn), а также формулу размещений с повторениями из n по k объектов:\nAr = n**k (символы ** обозначают возведение в степень)\nAr1 = {n}**{k1} = {n ** k1}\nAr2 = {n}**{k2} = {n ** k2}\nAr(общ) = Ar1 + Ar2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 15]


def CombinatoricsProductEasy():
    n1 = r.randint(2, 7)
    n2 = n1 + r.randint(1, 3)
    problemtmp = f"Сошедший с ума исскуственный интеллект генерирует две строки из случайных уникальных символов. Первая строка состроит из {n1} символов, а вторая из {n2}. Сначала ИИ переставляет местами все буквы первой строчки, генерируя все возможные уникальные строки из этих символов, и потом к каждой такой строке присоединяет по очереди все возможные уникальные строки, состоящие из символов второй исходной строки. Сколько итоговых строк получится у исскуственного интеллекта?"
    answertmp = m.factorial(n1) * m.factorial(n2)
    solvingtmp = f"Заметим, что перебор символов второй строки мы совершаем каждый раз после перебора символов из первой строки, в таком случае мы должны применить правило произведения (P(общ) = P1*P2*...*Pn), а также применим формулу числа перестановок n объектов:\nP = n!\nP1 = {n1}! = {m.factorial(n1)}\nP2 = {n2}! = {m.factorial(n2)}\nP(общее) = P1 * P2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]


def CombinatoricsProductCombinationsP():
    rand1 = r.randint(0, 5)
    n1 = r.randint(6, 10)
    k1 = r.randint(2, n1 - 1)
    broken = 1
    n2 = n1 - broken
    k2 = r.randint(2, n2 - 1)
    word1 = "стакана"
    word2 = "стакана"
    if k1 > 4:
        word1 = "стаканов"
    if k2 > 4:
        word2 = "стаканов"
    problemtmp = f"В закусочной стоит автомат газировки {n1} разных вкусов на разлив. К этому автомату подходит {names_set[rand1]}, и наливает себе {k1} {word1} газировки. Затем к автомату подходит его друг, он замечает, что один из тех вкусов, что наливал {names_set[rand1]} закончился, ему пришлось налисть себе {k2} {word2} из оставшихся вкусов. Затем мальчики выставляют стаканы на стол, сколько возможных комбинаций из вкусов могли набрать мальчики?"
    Cr1 = m.factorial(n1 + k1 - 1) // (m.factorial(k1) * m.factorial(n1 - 1))
    Cr2 = m.factorial(n2 + k2 - 1) // (m.factorial(k2) * m.factorial(n2 - 1))
    answertmp = Cr1 * Cr2
    solvingtmp = f"Заметим, что каждый из мальчиков может налить себе во все свои стаканы одинаковый вкус. Также важно, что после первого мальчика выборка уменьшается, что влияет на выбор второго, следовательно, чтобы решить задачу, нам понадобится правило произведения (Cr(общ) = Cr1 * Cr2 * ... * Crn), а также формула сочетаний с повторениями по k из n объектов:\nCr = (n+k-1)! / (k! * (n-1)!)\nCr1 = ({n1}+{k1}-1)! / ({k1}! * ({n1}-1)!) = {Cr1}\nCr2 = ({n2}+{k2}-1)! / ({k2}! * ({n2}-1)!) = {Cr2}\nCr(общее) = Cr1 * Cr2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 15]


def CombinatoricsProductAllocations():
    n1 = r.randint(7, 10)
    k1 = r.randint(2, 4)
    n2 = n1 - k1
    k2 = r.randint(2, n2 - 1)
    problemtmp = f"Два игрока играют в игру - ведущий расставляет {n1} улиток с разноцветными панцирями в ряд в случайном порядке, затем первый игрок делает выбор {k1} улиток. После него второй игрок делает свой выбор. Он должен выбрать {k2} из оставшихся улиток. Затем игроки выставляют на дорожку своих улиток в том порядке, в котором они их выбирали. Затем они наблюдают, как они ползут. Игроки сделали свой выбор. Сколько возможных комбинаций из улиток может стоять на поле (порядок также важен)?"
    A1 = m.factorial(n1) // m.factorial(n1 - k1)
    A2 = m.factorial(n2) // m.factorial(n2 - k2)
    answertmp = A1 * A2
    solvingtmp = f"Заметим, что от выбора первого игрока зависит выбор другого, так как выборка для второго игрока сужается после выбора первого. Применим правило произведения (A(общ) = A1 * A2 * ... * An), а также формулу размещений из n по k объектов:\nA = n! / (n-k)!\nA1 = {n1}! / ({n1}-{k1})! = {A1}\nA2 = {n2}! / ({n2}-{k2})! = {A2}\nA(общ) = A1 * A2 = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 15]


def TeorVerMainEasy():
    rand1 = r.randint(0, len(names_set)-1)
    grain = r.randint(6, 30)
    num = r.randint(1, grain)
    problemtmp = f"{names_set[rand1]} бросает идеальный игральный кубик с {grain} гранями. На каждой грани написано число от 1 до {grain}. Определите вероятность выпадения числа {num}. Если получается не целое число, введите несократимую дробь в формате: m/n"
    answertmpcash = f"1/{grain}"
    answertmp = answertmpcash
    solvingtmp = f"Раз кубик идеальный, то вероятность выпадения любого числа остается неизменной. Воспользуемся формулой классического определения вероятности получения m благоприятных исходов из n возможных:\nP = m/n\nP = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 5]

def TeorVerMainHard():
    vil = r.randint(1, 3)
    vil = 3
    if vil == 1:
        n = r.randint(5, 9)
        k = r.randint(n+1, n+4)
        empty = r.randint(1, n-2)
        n2 = n-empty
        k2 = k-n2
        problemtmp = f"Робот заполняет лотерейные билеты. На каждом билете изначально записано не выигрышное число. Роботу дают {n} билетов, и на них случайным образом робот записывает выигрышные числа, при этом на одном билете может быть как несколько выигрышных чисел, так и не быть вовсе. Всего робот написал {k} выигрышных чисел. Найдите вероятность того, что среди этих {n} билетов {empty} окажутся не выигрышными, а все остальные - выигрышными. Если получается не целое число, введите несократимую дробь в формате: m/n"
        N = m.factorial(n + k - 1) // (m.factorial(k) * m.factorial(n - 1))
        M = m.factorial(n2 + k2 - 1) // (m.factorial(k2) * m.factorial(n2 - 1))
        coef = m.factorial(n) // (m.factorial(n - empty) * m.factorial(empty))
        answertmp = str(Fraction(coef*M, N))
        solvingtmp = f"Для решения этой задачи воспользуемся формулой классического определения вероятности получения m благоприятных исходов из n возможных:\nP = m/n\nСначала определим количество элементарных (всевозможных) исходов, так как у нас возможен исход, где в первом билете написаны все выигрышные числа (что в данном контексте является повторением), а порядок расставления чисел не важен, воспользуемся формулой сочетаний с повторениями по k из n объектов:\nCr = (n+k-1)! / (k! * (n-1)!)\nn = ({n}+{k}-1)! / ({k}! * ({n}-1)!) = {N}\nЗатем, раз мы имеем {n2} выигрышных, мы в них записываем минимум по одному выигрышному числу, следовательно выигршных чисел остается {k2}. Все остальные числа мы также можем записывать с повторениями. Опять применим формулу сочетаний с повторениями, но теперь уже для нахождения m, но получившееся количество сочетаний нам необходимо домножить еще на количество всевозможных способов выбрать билеты, на которых не будет выигрышных чисел (по формуле количества сочетаний C = n! / ((n-k)! * k!) = {coef}):\nm = {coef} * (({n2}+{k2}-1)! / ({k2}! * ({n2}-1)!)) = {M*coef}\nТогда:\nP=m/n={M*coef}/{N}={answertmp}\nОтвет: {answertmp}"
        return [problemtmp, answertmp, solvingtmp, 20]
    elif vil == 2:
        rand1 = r.randint(0, len(names_set)-1)
        s = []
        ch = 0
        for i in range(r.randint(9, 15)):
            tmp = r.randint(0, 9)
            if tmp%2 == 0:
                ch+=1
            s.append(tmp)
        if ch == len(s):
            s.append(3)
        problemtmp = f"В коробке лежат карточки с написанными на них цифрами {s}. {names_set[rand1]} вытаскивает 2 случайных карточки из корбки, и первая вытащенная карточка оказывается нечетной. Найдите вероятность того, что из этих карточек можно составить четное число. Если получается не целое число, введите несократимую дробь в формате: m/n"
        answertmp = str(Fraction(ch, len(s)-1))
        solvingtmp = f"Нас устраивает расклад, где {names_set[rand1]} вытаскивает хотя бы 1 четную цифру, чтобы удовлетворить условию четности. Четных цифр в коробке - {ch}. Воспользуемся формулой классического определения вероятности получения m благоприятных исходов из n возможных, где количество всевозможных исходов будет на 1 меньше, чем изначальное количество карточек в коробке:\nP = m/n\nP = {ch}/{len(s)-1} = {answertmp}\nОтвет: {answertmp}"
        return [problemtmp, answertmp, solvingtmp, 15]
    else:
        rand1 = r.randint(0, len(names_set)-1)
        s = []
        word = ""
        for i in range(97, r.randint(97+5, 97 + 8)):
            s.append(chr(i))
            word+=chr(i)
        letter = s[r.randint(0, len(s)-1)]
        word+=letter
        problemtmp = f"{names_set[rand1]} составляет слова из случайных комбинаций букв из заданного списка: {s}. Каждая буква в слове встречается ровно 1 раз, кроме буквы {letter}. Длинна полученного слова равна {len(s)+1}. Какова вероятность что полученным словом будет слово {word}? Если получается не целое число, введите несократимую дробь в формате: m/n"
        answertmp = "1/" + str(m.factorial(len(s)+1)//2)
        solvingtmp = f"Для решения этой задачи воспользуемся формулой классического определения вероятности получения m благоприятных исходов из n возможных:\nP = m/n\nКоличество благоприятных исходов, очевидно, равно 1. Количество всевозможных исходов вычислятся по формуле числа перестановок n объектов:\nP = n!\nВ данном случае у нас также получится 2 повторения для каждой уникальной перестановки, буквы {letter} будут меняться местами, чтобы исключить такие повторения, разделим общее число перестановок на 2.\nP(перестановки) = {len(s)+1}! / 2 = {m.factorial(len(s)+1)//2}\nP(вероятность) = {answertmp}\nОтвет: {answertmp}"
        return [problemtmp, answertmp, solvingtmp, 10]

def TeorVerProduction():
    rand1 = r.randint(0, len(colors_set)-1)
    rand2 = r.randint(0, len(colors_set) - 1)
    while rand1 == rand2:
        rand2 = r.randint(0, len(colors_set) - 1)
    a = r.randint(5, 15)
    b = r.randint(5, 15)
    problemtmp = f"В урне лежат {colors_set[rand1]} и {colors_set[rand2]} шары - по {a} и {b} соответственно. Первый игрок берет из урны случайным образом сначала один, а потом второй шар. Второй игрок делает то же самое. Определите вероятность, что оба игрока вытащили по 2 {colors_set[rand1][:-2]+'ых'} шара. Если получается не целое число, введите несократимую дробь в формате: m/n"
    answertmpch = 1
    answertmpz = 1
    for i in range(4):
        answertmpch *= (a-i)
        answertmpz *= (a+b-i)
        answertmp = str(Fraction(answertmpch, answertmpz))
    solvingtmp = f"Воспользуемся правилом произведения вероятностей для независимых событий, где m - число благоприятных исходов, а n - число элементарных исходов:\nP = (m/(n)) * ((m-1)/(n-1)) * ((m-2)/(n-2)) * ((m-3)*(n-3)) = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 10]

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def TeorVerBernulli():
    f = r.randint(100, 100000)
    v = r.choice([5, 10])
    n = r.randint(4, 6)
    p = 1/v
    k = r.randint(2, 4)
    problemtmp = f"На складе лежат {f} фонарей. Известно, что вероятность брака равна {p}. Определите вероятность того, что среди выбранных наудачу {n} фонариков окажется {k} бракованных. Выведите число с 10 знаками после запятой."
    answertmp = (m.factorial(n)//(m.factorial(k)*m.factorial(n-k)))*(p**k)*(1-p)**(n-k)
    answertmp = float(toFixed(answertmp, 10))
    solvingtmp = f"В этой задаче мы имеем ряд независимых испытаний с одинаковыми параметрами, применим формулу Бернулли для события, вероятность происхождения которого p, из n экспериментов, с k ожидаемыми результатов (символы ** обозачают возведение в степень):\nP = C * p**k * (1-p)**(n-k)\nC = n! / (k! * (n*k)!) = {m.factorial(n)//(m.factorial(k)*m.factorial(n-k))}\nP = {m.factorial(n)//(m.factorial(k)*m.factorial(n-k))} * {p}**{k} * (1 - {p})**({n}-{k}) = {answertmp}\nОтвет: {answertmp}"
    return [problemtmp, answertmp, solvingtmp, 15]

themes_list = [
    CombinatoricsPermutationsEasy(),
    CombinatoricsPermutationsHard(),
    CombinatoricsCombinations(),
    CombinatoricsCombinationsP(),
    CombinatoricsAllocations(),
    CombinatoricsAllocationsP(),
    CombinatoricsSummationEasy(),
    CombinatoricsSummationCombinations(),
    CombinatoricsSummationAllocationsP(),
    CombinatoricsProductEasy(),
    CombinatoricsProductAllocations(),
    CombinatoricsProductCombinationsP(),
    TeorVerMainEasy(),
    TeorVerMainHard(),
    TeorVerProduction(),
    TeorVerBernulli()]

def random_problem(n = None):
    if n != None:
        i = n
    else:
        i = r.randint(0, len(themes_list)-1)
    if i == 0:
        tmp = CombinatoricsPermutationsEasy()
        tmp.append("CPE")
    elif i == 1:
        tmp = CombinatoricsPermutationsHard()
        tmp.append("CPH")
    elif i == 2:
        tmp = CombinatoricsCombinations()
        tmp.append("CC")
    elif i == 3:
        tmp = CombinatoricsCombinationsP()
        tmp.append("CCP")
    elif i == 4:
        tmp = CombinatoricsAllocations()
        tmp.append("CA")
    elif i == 5:
        tmp = CombinatoricsAllocationsP()
        tmp.append("CAP")
    elif i == 6:
        tmp = CombinatoricsSummationEasy()
        tmp.append("CSE")
    elif i == 7:
        tmp = CombinatoricsSummationCombinations()
        tmp.append("CSC")
    elif i == 8:
        tmp = CombinatoricsSummationAllocationsP()
        tmp.append("CSAP")
    elif i == 9:
        tmp = CombinatoricsProductEasy()
        tmp.append("CoProdEasy")
    elif i == 10:
        tmp = CombinatoricsProductAllocations()
        tmp.append("CPA")
    elif i == 11:
        tmp = CombinatoricsProductCombinationsP()
        tmp.append("CPCP")
    elif i == 12:
        tmp = TeorVerMainEasy()
        tmp.append("TVME")
    elif i == 13:
        tmp = TeorVerMainHard()
        tmp.append("TVMH")
    elif i == 14:
        tmp = TeorVerProduction()
        tmp.append("TVP")
    else:
        tmp = TeorVerBernulli()
        tmp.append("TVB")
    tmp.append(i + 4)
    print(tmp)
    return tmp

