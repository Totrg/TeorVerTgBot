# -*- coding: utf-8 -*-
import telebot
import random
from quest_generator import *
import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


def remember_id(user_id: int, rating: int):
    try:
        cursor.execute('INSERT INTO Core (user_id, rating) VALUES (?, ?)', (user_id, rating))
        conn.commit()
    except Exception as e:
        print("Id had already wroten. Skipping...")


def db_find(user_id: int):
    try:
        cursor.execute(f"select * from Core WHERE user_id = {user_id}")
        rez = []
        rows = cursor.fetchall()
        for row in rows[0]:
            rez.append(row)
        print("From db_find():", rez)
        return rez
    except Exception as e:
        print("db_find() FAILED!")


def db_update(user_id: int, column_name: str, val):
    try:
        cursor.executescript(f"update Core set {column_name} = {val} WHERE user_id = {user_id};")
        conn.commit()
    except Exception:
        print(f"db_update() FAILED! from id: {user_id}")


bot = telebot.TeleBot('5021080606:AAEd3fJtWcuDAFqoDGe84s3GmA5wvuSvf0E')


@bot.message_handler(commands=['start'])
def start(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        bot.send_message(message.from_user.id,
                         'Приветствуем! Это бот, главная задача которого - помочь вам отработать вашу технику решения базовых задач по теме теории вероятностей. Чтобы получить список доступных команд напишите /help')


@bot.message_handler(commands=['help'])
def help(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        bot.send_message(message.from_user.id,
                         "Список команд:\n/start - знакомство\n/help - список доступных команд\n/problem - решить случайную задачу\n/rating - статистика пользователя и его рейтинг\n/themes - список всех тем")


@bot.message_handler(commands=['problem'])
def problem(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem()
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")


@bot.message_handler(commands=['rating'])
def get_rating(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        flag = True
        for i in range(4, 20):
            if data[i]==None:
                flag = False
        if flag == True:
            tmp1 = str(int((sum(data[4:20]) / 16) * 100))+"%"
        else:
            tmp1 = "не все типы задач решались пользователем"
        if data[4]!=None and data[5]!=None:
            tmp2 = str(int((sum(data[4:6]) / 2) * 100))+"%"
        else:
            tmp2 = "не все типы задачи решались пользователем"
        if data[6]!=None and data[7]!=None:
            tmp3 = str(int((sum(data[6:8]) / 2) * 100))+"%"
        else:
            tmp3 = "не все типы задачи решались пользователем"
        if data[8]!=None and data[9]!=None:
            tmp4 = str(int((sum(data[8:10]) / 2) * 100))+"%"
        else:
            tmp4 = "не все типы задачи решались пользователем"
        if data[10]!=None and data[11]!=None and data[12]!=None:
            tmp5 = str(int((sum(data[10:13]) / 3) * 100))+"%"
        else:
            tmp5 = "не все типы задачи решались пользователем"
        if data[13]!=None and data[14]!=None and data[15]!=None:
            tmp6 = str(int((sum(data[13:16]) / 3) * 100))+"%"
        else:
            tmp6 = "не все типы задачи решались пользователем"
        if data[16]!=None and data[17]!=None:
            tmp7 = str(int((sum(data[16:18]) / 2) * 100))+"%"
        else:
            tmp7 = "не все типы задачи решались пользователем"
        if data[18] != None:
            tmp8 = str(int((data[18]) * 100))+"%"
        else:
            tmp8 = "еще не решались пользователем"
        if data[19] != None:
            tmp9 = str(int((data[19]) * 100))+"%"
        else:
            tmp9 = "еще не решались пользователем"
        bot.send_message(message.from_user.id,
                         f"Ваша статистика:\nЛичный рейтинг: {data[2]} \nОбщий процент решения задач: {tmp1} \nПроцент решения задачи по теме 'Комбинаторика - перестановки': {tmp2} \nПроцент решения задач по теме 'Комбинаторика - сочетания': {tmp3} \nПроцент решения задач по теме 'Комбинаторика - размещения': {tmp4} \nПроцент решения задач по теме 'Комбинаторика - правило сложения': {tmp5} \nПроцент решения задач по теме 'Комбинаторика - правило произведения': {tmp6} \nПроцент решения задач по теме 'Формула классического определения вероятности': {tmp7} \nПроцент решения задач по теме 'Правило произведения вероятностей для независимых событий': {tmp8} \nПроцент решения задач по теме 'Формула Бернулли': {tmp9} \n\nМожете вводить следующую команду. (список доступных команд: /help )")


@bot.message_handler(commands=['themes'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        bot.send_message(message.from_user.id, "Список тем:\n\nКомбинаторика:\n1.Простые перестановки (/CombinatoricsPermutationsEasy - задача на эту тему)\n2. Сложные перестановки (/CombinatoricsPermutationsHard )\n3. Обычные сочетания (/CombinatoricsCombinations )\n4. Сочетания с повторениями (/CombinatoricsCombinationsP )\n5. Обычные размещения (/CombinatoricsAllocations )\n6. Размещения с повторениями (/CombinatoricsAllocationsP )\n7. Правило суммы (/CombinatoricsSummation )\n8. Правило произведения (/CombinatoricsProduction )\n\nТеория вероятностей:\n1. Классическое определение вероятности - простейшие задачи (/TeorVerMainEasy )\n2. Классическое определение вероятности - сложные задачи (/TeorVerMainHard )\n3. Правило произведения вероятностей для независимых событий (/TeorVerProduction )\n4. Формула Бернулли (/TeorVerBernulli )\n\nМожете вводить следующую команду. (список доступных команд: /help )")


@bot.message_handler(commands=['CombinatoricsPermutationsEasy'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(0)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsPermutationsHard'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(1)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsCombinations'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(2)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")


@bot.message_handler(commands=['CombinatoricsCombinationsP'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(3)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsAllocations'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(4)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsAllocationsP'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(5)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsSummation'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(r.randint(6, 8))
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['CombinatoricsProduction'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(r.randint(9, 11))
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['TeorVerMainEasy'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(12)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['TeorVerMainHard'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(13)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['TeorVerProduction'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(14)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(commands=['TeorVerBernulli'])
def themes(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] != 0:
        bot.send_message(message.from_user.id,
                         "Вы не можете использовать какие-либо команды, пока бот ждёт от вас ответа на задачу.")
    else:
        seq = random_problem(15)
        bot.send_message(message.from_user.id, seq[0])
        db_update(us_id, "waiting", 1)
        db_update(us_id, "in_progress_answer", "'" + str(seq[1]) + "'")
        db_update(us_id, "in_progress_solution", "'" + str(seq[2]) + "'")
        db_update(us_id, "in_progress_rating", "'" + str(seq[3]) + "'")
        db_update(us_id, "in_progress_theme", "'" + str(seq[4]) + "'")
        db_update(us_id, "in_progress_index", "'" + str(seq[5]) + "'")

@bot.message_handler(content_types=['text'])
def get_answer_from_user(message):
    us_id = message.from_user.id
    remember_id(user_id=us_id, rating=0)
    data = db_find(message.from_user.id)
    if data[3] == 0:
        bot.send_message(message.from_user.id,
                         "Вы ввели команду некорректно. Попробуйте еще раз.")
    else:
        user_answer = str(message.text)
        if data[-5] == user_answer:
            prate = int(data[-3])
            bot.send_message(message.from_user.id,
                             f"Абсолютно верно! Изменение вашего рейтинга: +{prate}. Можете вводить следующую команду. (список доступных команд: /help )")
            db_update(us_id, "rating", int(data[2]) + prate)
            db_update(us_id, "waiting", 0)
            if data[data[-1]] == None:
                db_update(us_id, data[-2], 1)
            else:
                db_update(us_id, data[-2], float(toFixed((float(data[data[-1]]) + 1) / 2, 10)))
        else:
            prate = int(data[-3])
            bot.send_message(message.from_user.id,
                             f"Неверно. Изменение вашего рейтинга: -{prate}.\nРешение:\n{data[-4]}\nМожете вводить следующую команду. (список доступных команд: /help )")
            db_update(us_id, "rating", int(data[2]) - prate)
            db_update(us_id, "waiting", 0)
            if data[data[-1]] == None:
                db_update(us_id, data[-2], 0)
            else:
                db_update(us_id, data[-2], float(toFixed((float(data[data[-1]]) + 1) / 2, 10)))


bot.polling(none_stop=True, interval=0)
