#a) Добавьте игру против бота
# Здесь бот ходит почти рандомно, у него можно легко выиграть, если не тупить.
import random

def WhoPlaysFirst ():
    player = str(input('Добрый день!\nБот уже готов сразиться с вами.\nЧто выбираете: орел или решка? Ответ: '))
    bot = ''
    if player == 'орел':
        bot = 'решка'
    elif player == 'решка':
        bot = 'орел'

    orel = [0,'орел']
    reshka = [1,'решка']
    a = random.randrange(0,2)
    print('*Подкидываем воображаемую монетку*')
    if a == orel[0]:
        if orel[1] == player:
            answer = 'Ура, орел! Вы ходите первым'
        if orel[1] == bot:
            answer = 'Упс, орел! Первым ходит бот'

    if a == reshka[0]:
        if reshka[1] == player:
            answer = 'Ура, решка! Вы ходите первым'
        if reshka[1] == bot:
            answer = 'Упс, решка! Первым ходит бот'
    return answer

def Play(res):
  first =  "Ура" in res
  all_in_all = 2021
  player = 0
  bot = 0
  print(f'\nПриступим!\nНа столе лежит 2021 конфета.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.\n ')
  while all_in_all > 0:
    if first == True:
        print("Что ж, делайте ход.")
        step1 = GetNumber(1)
        player+=step1
        all_in_all -=step1
        print(f'\nИтого: {all_in_all}\nИгрок:{player}\nБот:{bot}')
        first = False
    else:
        print("Теперь ходит бот.")
        step2 = BotStep()
        print(f'Бот выбрал {step2}')
        bot+=step2
        all_in_all-=step2
        print(f'\nИтого: {all_in_all}\nИгрок:{player}\nБот:{bot}')
        first = True
    if 0 < all_in_all < 29 and first == False:
        step2 = all_in_all
        all_in_all-=step2
        bot+=step2
        print(f'\nБот выбрал {step2}')
        first = True

    if all_in_all == 0:
        if first == True:
            player = 0
            print(f'\nУвы! Вы проиграли...\nИтоговый счет:{player}')
        if first == False:
            player+=bot
            print(f'\nПоздравляем! Вы выиграли :)\nИтоговый счет:{player}')

def GetNumber(x): 
    num = 0
    for i in range (x):
        smt = False
        while not smt:
            try:
                number = int(input("Выберите число от 1 до 28: "))
                num = number
                smt = True
                if number < 1 or number > 28:
                    smt = False
                    print("Выберите число от 1 до 28!")
            except ValueError:
                print("Вы ошиблись. Введите число!")
    return num

def BotStep():
    num = random.randrange(1,29)
    return num

res = WhoPlaysFirst()
print(res)
Play(res)