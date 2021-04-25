# -*- coding: utf-8 -*-
import asyncio
import os
import time
from datetime import datetime

import discord
from discord.ext import commands

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # проверка на отправку сообщений
    if message.author == client.user:
        return

    # стартовое сообщение
    if message.content.startswith('start'):
        await message.channel.send(
            'set timer - установка таймера по заданному времени (пример записи: set timer 0 30)' + '\n' + \
            'timer40 - таймер по заданному времени для тренировки ВП40' + '\n' + \
            'timer60 - таймер по заданному времени для тренировки ВП60' + '\n' + '' + '\n' + \
            'tr40 - запись результата тренировки ВП40 (пример записи: tr40 90 89 92 95)' \
            + '\n' + \
            'tr60 - запись результата тренировки ВП60 (пример записи: tr40 90 89 92 95 91 93)' \
            + '\n' + \
            'com40 - запись результата соревнований ВП40 (пример записи: tr40 90 89 92 95)' \
            + '\n' + \
            'com60 - запись результата соревнований ВП60 (пример записи: tr40 90 89 92 95 91 93)' \
            + '\n' + '' + '\n' + \
            'all tr40 - просмотр всех записей результатов тренировки ВП40' + '\n' + \
            'all tr60 - просмотр всех записей результатов тренировки ВП60' + '\n' + \
            'all com40 - просмотр всех записей результатов соревнований ВП40' + '\n' + \
            'all com60 - просмотр всех записей результатов соревнований ВП60' + '\n' + '' \
            + '\n' \
              'scatt - запись результата на тренажере SCATT (пример записи: tr40 90 89 92 95)' \
            + '\n' + \
            'all scatt - просмотр всех записей результатов на тренажере SCATT' + \
            '\n' + '' + '\n' + \
            'remind - event-календарь или напоминалка о грядущих соревнованиях (пример записи: remind 2021 05 24 Москва)' + '\n' + \
            'all remind - просмотр всех event-напоминалок' + '\n' + '' + '\n' \
                                                                         'theory - запись теории для спортсмена (пример записи: theory нельзя волноваться)' + '\n' + \
            'all theory - просмотр теории' + '\n' + 'picture - фотоальбом')

    # установка таймера пользователем
    if message.content.startswith('set timer'):
        h = message.content.split()[2]
        m = message.content.split()[3]
        await message.channel.send(f'Тренировка закончится через {h} часов и {m} минут.')
        await asyncio.sleep(int(h) * 3600 + int(m) * 60)
        await message.channel.send("Тренировка окончена")

    # фиксированное время 1 час
    if message.content.startswith('timer40'):
        h = 1
        m = 0
        await message.channel.send(f'Тренировка закончится через {h} час и {m} минут.')
        await asyncio.sleep(int(h) * 3600 + int(m) * 60)
        await message.channel.send("Тренировка окончена")

    # фиксированное время 1 час 15 минут
    if message.content.startswith('timer60'):
        h = 1
        m = 15
        await message.channel.send(f'Тренировка закончится через {h} час и {m} минут.')
        await asyncio.sleep(int(h) * 3600 + int(m) * 60)
        await message.channel.send("Тренировка окончена")

    # запись результата тренировки 40 выстрелов
    if message.content.startswith('tr40'):
        summ = 0
        k = 0
        al = message.content.split()
        al = al[1:]
        for i in al:
            if i == '98':
                k = 1
            elif i == '99':
                k = 2
            elif i == '100':
                k = 3
            summ += int(i)
        stroka = str(datetime.now().date()) + ': ' + str(message.content[5:]) + ' (' + str(summ) + ')'
        f = open('40t.txt', 'a')
        f.write(stroka + '\n')
        if k == 1:
            await message.channel.send('98 в серии - это сильно!')
        if k == 2:
            await message.channel.send('99 в серии - это сильно!')
        if k == 3:
            await message.channel.send('100 в серии - это сильно!')
        await message.channel.send('Запиcан результат тренировки(40 выстрелов): ' + stroka)
        f.close()

    # просмотр всех записей результатов тренировки 40 выстрелов
    if message.content.startswith('all tr40'):
        f = open("40t.txt", 'r')
        await message.channel.send(f.read())
        f.close()

    # запись результата тренировки 60 выстрелов
    if message.content.startswith('tr60'):
        summ = 0
        k = 0
        al = message.content.split()
        al = al[1:]
        for i in al:
            if int(i) == 98:
                k = 1
            if int(i) == 99:
                k = 2
            if int(i) == 100:
                k = 3
            summ += int(i)
        stroka = str(datetime.now().date()) + ': ' + str(message.content[5:]) + ' (' + str(summ) + ')'
        f1 = open('60t.txt', 'a')
        print(f1.write(stroka + '\n'))
        if k == 1:
            await message.channel.send('98 в серии - это сильно!')
        if k == 2:
            await message.channel.send('99 в серии - это сильно!')
        if k == 3:
            await message.channel.send('100 в серии - это сильно!')
        await message.channel.send('Запиcан результат тренировки(60 выстрелов): ' + stroka)
        f1.close()

    # просмотр всех записей результатов тренировки 60 выстрелов
    if message.content.startswith('all tr60'):
        f1 = open("60t.txt", 'r')
        await message.channel.send(f1.read())
        f1.close()

    # запись результата соревнований 40 выстрелов
    if message.content.startswith('com40'):
        summ = 0
        k = 0
        al = message.content.split()
        al = al[1:]
        for i in al:
            if int(i) == 98:
                k = 1
            if int(i) == 99:
                k = 2
            if int(i) == 100:
                k = 3
            summ += int(i)
        stroka = str(datetime.now().date()) + ': ' + str(message.content[5:]) + ' (' + str(summ) + ')'
        f2 = open('40c.txt', 'a')
        print(f2.write(stroka + '\n'))
        if k == 1:
            await message.channel.send('98 в серии - это сильно!')
        if k == 2:
            await message.channel.send('99 в серии - это сильно!')
        if k == 3:
            await message.channel.send('100 в серии - это сильно!')
        await message.channel.send('Запиcан результат соревнований (40 выстрелов): ' + stroka)
        f2.close()

    # просмотр всех записей результатов соревнований 40 выстрелов
    if message.content.startswith('all com40'):
        f2 = open("40c.txt", 'r')
        await message.channel.send(f2.read())
        f2.close()

    # запись результата соревнований 60 выстрелов
    if message.content.startswith('com60'):
        summ = 0
        k = 0
        al = message.content.split()
        al = al[1:]
        for i in al:
            if int(i) == 98:
                k = 1
            if int(i) == 99:
                k = 2
            if int(i) == 100:
                k = 3
            summ += int(i)
        stroka = str(datetime.now().date()) + ': ' + str(message.content[5:]) + ' (' + str(summ) + ')'
        f3 = open('60c.txt', 'a')
        print(f3.write(stroka + '\n'))
        if k == 1:
            await message.channel.send('98 в серии - это сильно!')
        if k == 2:
            await message.channel.send('99 в серии - это сильно!')
        if k == 3:
            await message.channel.send('100 в серии - это сильно!')
        await message.channel.send('Запиcан результат соревнований (60 выстрелов): ' + stroka)
        f3.close()

    # просмотр всех записей результатов соревнований 60 выстрелов
    if message.content.startswith('all com60'):
        f3 = open("60c.txt", 'r')
        await message.channel.send(f3.read())
        f3.close()

    # запись результата на тренажере SCATT
    if message.content.startswith('scatt'):
        summ = 0
        k = 0
        al = message.content.split()
        al = al[1:]
        for i in al:
            if int(i) == 98:
                k = 1
            if int(i) == 99:
                k = 2
            if int(i) == 100:
                k = 3
            summ += int(i)
        stroka = str(datetime.now().date()) + ': ' + str(message.content[5:]) + ' (' + str(summ) + ') '
        f5 = open('scatt.txt', 'a')
        print(f5.write(stroka + '\n'))
        if k == 1:
            await message.channel.send('98 в серии - это сильно!')
        if k == 2:
            await message.channel.send('99 в серии - это сильно!')
        if k == 3:
            await message.channel.send('100 в серии - это сильно!')
        await message.channel.send('Запиcан результат тренировки (SCATT): ' + stroka)
        f5.close()

    # просмотр всех записей результатов тренажера SCATT
    if message.content.startswith('all scatt'):
        f5 = open("scatt.txt", 'r')
        await message.channel.send(f5.read())
        f5.close()

    # event-календарь или напоминалка о грядущих соревнованиях
    if message.content.startswith('remind'):
        year = str(datetime.now().date()).split('-')[0]
        mon = str(datetime.now().date()).split('-')[1]
        day = str(datetime.now().date()).split('-')[2]
        y = message.content.split()[1]
        m = message.content.split()[2]
        d = message.content.split()[3]
        com = str(message.content.split()[4])

        f4 = open('event.txt', 'a', encoding="utf-8")
        f4.write(message.content[7:] + '\n')
        await message.channel.send('Запиcано мероприятие: ' + message.content[7:])
        f4.close()
        if int(d) - int(day) > 5:
            r = int(d) - int(day) - 5

        else:
            r = 1
        if mon == m:
            await message.channel.send(
                'Напоминание сработает через ' + str(r) + ' дней ' + ' (за 5 дней до мероприятия)')
            await asyncio.sleep(r * 86400)
            await message.channel.send('Напоминаю о мероприятии: ' + com)
        if mon != m:
            if int(m) - int(mon) == 1:
                rr = 30 - int(day) + int(d) - 5
                await message.channel.send(
                    'Напоминание сработает через ' + str(rr) + ' дней' + '(за 5 дней до мероприятия)')
                await asyncio.sleep(rr * 86400)
                await message.channel.send('Напоминаю о мероприятии: ' + com)
            if int(m) - int(mon) > 1:
                rrr = 30 * (int(m) - int(mon) - 1) + 30 - int(day) + int(d) - 5
                await message.channel.send(
                    'Напоминание сработает через ' + str(rrr) + ' дней' + '(за 5 дней до мероприятия)')
                await asyncio.sleep(rrr * 86400)
                await message.channel.send('Напоминаю о мероприятии: ' + com)

    # просмотр всех записей event-напоминалок
    if message.content.startswith('all remind'):
        f4 = open("event.txt", encoding="utf-8")
        await message.channel.send(f4.read())
        f4.close()

    # запись теории для спортсмена
    if message.content.startswith('theory'):
        f6 = open('theory.txt', 'a', encoding="utf-8")
        print(f6.write(message.content[6:] + '\n'))
        await message.channel.send('Теория записана!')
        f6.close()

    # просмотр всей записанной теории
    if message.content.startswith('all theory'):
        f6 = open("theory.txt", encoding="utf-8")
        await message.channel.send(f6.read())
        f6.close()

    # просмотр фотографий
    if message.content.startswith('picture'):
        with open('b-iPxZpEiJo.jpg', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(picture)


client.run('')
