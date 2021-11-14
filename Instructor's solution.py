def print_2Dlist(my_list):
    first_d = len(my_list)
    for row_ind in range(first_d):
        second_d = len(my_list[row_ind])
        for col_ind in range(second_d):
            print(my_list[row_ind][col_ind], end='')
        print()


def print_separator():
    s = "-" * 72
    print(s)


x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

game_board = []
player_row = []

for i in range(x):
    row = []
    for j in range(y):
        row.append('*')
    game_board.append(row)

for k in range(g):
    empty = []
    for j in range(y):
        empty.append(' ')
    game_board.append(empty)

single = []
for j in range(y):
    if(y % 2 == 0):
        if(y // 2 == j + 1):
            single.append('@')
        else:
            single.append(' ')
    else:
        if (y // 2 == j):
            single.append('@')
        else:
            single.append(' ')
player_row.append(single)

iteration = 0
while(True):

    WIN_FLAG = True
    for row in game_board:
        for elem in row:
            if (elem == '*'):
                WIN_FLAG = False
    if (WIN_FLAG):
        print("YOU WON!")
        break

    print_2Dlist(game_board)
    print_2Dlist(player_row)
    print_separator()

    action = input("Choose your action!\n")
    action = action.lower()
    if(action == "exit"):
        break
    elif(action == "left"):
        ship_ind = player_row[0].index('@')
        if(ship_ind != 0):
            player_row[0][ship_ind-1] = '@'
            player_row[0][ship_ind] = ' '
        else:
            pass
    elif(action == "right"):
        ship_ind = player_row[0].index('@')
        if (ship_ind != len(player_row[0]) - 1):
            player_row[0][ship_ind + 1] = '@'
            player_row[0][ship_ind] = ' '
        else:
            pass
    elif(action == 'fire'):
        ship_ind = player_row[0].index('@')
        line = len(game_board) - 1
        for i in range(line, -1, -1):
            if(game_board[i][ship_ind] == '*'):
                line = i
                break
        else:
            line = -1
        for from_back in range(0, len(game_board) - 1 - line):
            game_board[len(game_board) - 1 - from_back][ship_ind] = '|'
            print_2Dlist(game_board)
            print_2Dlist(player_row)
            print_separator()
            game_board[len(game_board) - 1 - from_back][ship_ind] = ' '
        for i in range(len(game_board) - 1, -1, -1):
            if(game_board[i][ship_ind] == '*'):
                game_board[i][ship_ind] = ' '
                break
            else:
                pass
    else:
        pass

    iteration = iteration + 1

    if(iteration % 5 == 0):
        if (game_board[-1].count('*') != 0):
            print('GAME OVER')
            break

        last = game_board[-1]
        rest = game_board[:-1]
        updated = []
        for i in range(len(game_board)):
            if(i == 0):
                updated.append(last)
            else:
                updated.append(rest[i-1])
        game_board = updated

print_2Dlist(game_board)
print_2Dlist(player_row)
print_separator()

score = 0
for row in game_board:
    score += row.count('*')

print("YOUR SCORE:", x*y - score)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
