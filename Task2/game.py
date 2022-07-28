# Создайте программу для игры в ""Крестики-нолики"".
# Человек vs Человек

board = list(range(1,10))

def ShowBoard(board):
   print("-" * 13) # верхняя строка
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|") # заполнение строк от 1 до 9
      print("-" * 13) # разделительные строки

def GetStep(player_token):
   valid = False
   while not valid:
      PlayerStep = input("Куда поставим " + player_token+"? ")
      try:
         PlayerStep = int(PlayerStep) # checking int
      except:
         print("Некорректный ввод. Введите число!")
         continue
      if PlayerStep >= 1 and PlayerStep <= 9:
         if(str(board[PlayerStep-1]) not in "XO"): # check if a place is taken
            board[PlayerStep-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def Checking_3in_row(board):
   WinCombination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in WinCombination:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def Game(board):
    counter = 0
    win = False
    while not win:
        ShowBoard(board)
        if counter % 2 == 0:
           GetStep("X")
        else:
           GetStep("O")
        counter += 1
        if counter > 4:
           check = Checking_3in_row(board)
           if check:
              print(check, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    ShowBoard(board)

Game(board)
input("Нажмите Ctrl+C или Enter для выхода!")