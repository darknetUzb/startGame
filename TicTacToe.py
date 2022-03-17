import os, sys

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
		
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
    
    clearscreen()
os.system("termux-open-url https://t.me/termux_uz_private")


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("Sizning navbatingiz" + turn + ".qaysi joyga ko'chirasiz: ")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Bu joy allaqachon egallangan\nBoshqa joyga yuring:")
            continue

        
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " Yutdi. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin .\n")                
                print(" **** " +turn + " yutdi. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nO'yin tugadi.\n")                
                print(" **** " +turn + " yutdi. ****")
                break 

       
        if count == 9:
            print("\nO'yin tugadi.\n")                
            print("Durrang boldi!!")

        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    restart = input("Qayta o'ynashni hohlaysizmi?(h/y)")
    if restart == "h" or restart == "H":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()