def assign():
    #Assigning the matrix
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']

    return row1, row2, row3


def position(i):
    #Linking the list positions with their common names
    row_posn = ['row1[0]', 'row1[1]', 'row1[2]', 'row2[0]', 'row2[1]', 'row2[2]', 'row3[0]', 'row3[1]', 'row3[2]']
    p_posn = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    index = row_posn.index(i)

    return p_posn[index]


def info():
    #Just to print some statements and take the 1st move-choice
    print()
    print("The box names (for entering) are as follows:-")
    print()
    print(['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'], sep = '\n')
    print()
    print("Your character will be X while machine's character will be O")
    print()
    print("Enter 1 if you want machine to move first")
    print("Else 2 to move first")
    print()
    choice = int(input("Choice: "))

    return choice


def check_result():
    #Checking for 3 in a row, column or diagonal
    #To be done after every move

    result = None

    ask_result = -1
    for winner in ['O', 'X']:
        #Running a loop to check for both ('0' or 'X')        

        if row1.count(winner) == 3 or row2.count(winner) == 3 or row3.count(winner) == 3:
            #Checking for the row count
            result, ask_result = terminate(winner)
            if result != None: #If game doesn't end here... (Done in every condition)
                break

        elif row1[0] == row2[1] == row3[2] == winner or row1[2] == row2[1] == row3[0] == winner:
            #Checking for the diagonal count
            result, ask_result = terminate(winner)
            if result != None:
                break

        elif row1.count(' ') == 0 and row2.count(' ') == 0 and row3.count(' ') == 0:
            #Checking for full board no result (Draw!)
            result, ask_result = terminate(0) #Draw --> terminate(0)
            if result != None:
                break

        else:
            for j in range(3):
                if row1[j] == row2[j] == row3[j] == winner:
                    #Checking for column count (Loop to check all 3 columns)
                    result, ask_result = terminate(winner)
                    if result != None:
                        break

    return result, ask_result


def terminate(winner):
    #Determine the result
    print()
    if winner == 'X':
        print("Congo! You won the game.")
        result = 1
    elif winner == 'O':
        print("Alas! You lost the game.")
        result = -1
    elif winner == 0: #Used for the Draw case
        print("A draw!")
        result = 0

    print("Would u like to try again?")
    ask_result = -1 #Asking for once more (to be an infinite loop)
                    #Kept -1 till the game ends (not asked yet)
    ask_result = int(input("Yes(1)/ No(0): "))

    return result, ask_result


def marking(turn, posn):
    #Marking the user's choice in the matrix
    
    turn_all = 'OX'
    for sign in turn_all:
        if turn == sign:
            continue
        opponent_turn = sign #Identifying user's and machine's playing sign

    posn_all = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    if posn in posn_all: 
        index = posn_all.index(posn)
        if index < 3: #If the posn. is in first row
            if row1[index] == ' ': #The opted posn. is vacant
                row1[index] = turn #Putting the sign
                return 1 #If sign placed successfully --> return 1
            else: #The opted posn. isn't vacant
                if turn == 'X': #If its user's move (Done in every condition)
                    print("Already Occupied") 
                return 0 #If sign wasn't placed successfully --> return 1
        elif index >= 3 and index < 6: #If the posn. is in second row
            if row2[index - 3] == ' ':
                row2[index - 3] = turn
                return 1
            else:
                if turn == 'X':
                    print("Already Occupied") 
                return 0
        elif index >= 6: #If the posn. is in third row
            if row3[index - 6] == ' ':
                row3[index - 6] = turn
                return 1
            else:
                if turn == 'X':
                    print("Already Occupied")
                return 0
    else: #Invalid posn. entered
        print("Incorrect position")
        return -1 #If mark posn. incorrect --> return -1


def macalg_corfil1(move, posn, sub_case):
    import random
    while True:
        row1_str = ['row1[0]', 'row1[1]', 'row1[2]']
        row2_str = ['row2[0]', 'row2[1]', 'row2[2]']
        row3_str = ['row3[0]', 'row3[1]', 'row3[2]']

        column1 = [row1[0], row2[0], row3[0]]
        column1_str = ['row1[0]', 'row2[0]', 'row3[0]']
        column2 = [row1[1], row2[1], row3[1]]
        column2_str = ['row1[1]', 'row2[1]', 'row3[1]']
        column3 = [row1[2], row2[2], row3[2]]
        column3_str = ['row1[2]', 'row2[2]', 'row3[2]']

        if move == 1:
            if posn != None and row2[1] == ' ':
                posn = 'b2'
                sub_case = 0
            else:
                row = chr(random.randrange(97, 100, 2))
                column = str(random.randrange(1, 4, 2))
                posn = row + column
        elif move == 2:
            if sub_case == 0:
                p_posn = ('a2', 'b1', 'b3', 'c2')
                random_posn_index = random.randrange(4)
                posn = p_posn[random_posn_index]
            else:
                if posn in ('a2', 'b1', 'b3', 'c2'):
                    for group in (row1, row3, column1, column3):
                        if 'X' in group:
                            if group == row1:
                                a_s = row3
                                s = row3_str
                            elif group == row3:
                                a_s = row1
                                s = row1_str
                            elif group == column1:
                                a_s = column3
                                s = column3_str
                            elif group == column3:
                                a_s = column1
                                s = column1_str

                            if 'O' in group:
                                index = group.index(' ')
                                sub_case = 1
                            else:
                                index = a_s.index('O')

                            if index == 0:
                                j = 2
                            elif index == 2:
                                j = 0
                            posn = position(s[j])

                else:
                    a = chr(random.randrange(97, 100, 2))
                    n = str(random.randrange(1, 4, 2))
                    posn = a + n
        elif move == 3:
            if sub_case == 1:
                for group in (row1, row3, column1, column3):
                    if group.count('O') == 2:
                        if group == row1:
                            a = row3
                            s = row3_s
                        elif group == row3:
                            a = row1
                            s = row1_s
                        elif group == column1:
                            a = column3
                            s = column3_s
                        elif group == column3:
                            a == column1
                            s = column1_s

                for group in (row1, row3, column1, column3):
                    if group.count(' ') == 1:
                        index = group.index(' ')
                posn = position(s[index])

            else:
                a = chr(random.randrange(97, 100, 2))
                n = str(random.randrange(1, 4, 2))
                posn = a + n

        else:
            a = chr(random.randrange(97, 100, 2))
            n = str(random.randrange(1, 4, 2))
            posn = a + n

        if marking('O', posn) == 1:
            t = marking('O', posn)
            move += 1
            print()
            print("Machine's move position:", posn)
            print(row1, row2, row3, sep='\n')
            break

    return move, sub_case


def macalg_linup2():
    diagonal1 = [row1[0], row2[1], row3[2]]
    diagonal2 = [row1[2], row2[1], row3[0]]

    placement = 0
    for playr_symb in ('O', 'X'):
        if placement == 0:
            if row1.count(playr_symb) == 2 and row1.count(' ') == 1:
                index = row1.index(' ')
                row1[index] = 'O'
                posn = 'a' + str(index + 1)
                placement = 1
            elif row2.count(playr_symb) == 2 and row2.count(' ') == 1:
                index = row2.index(' ')
                row2[index] = 'O'
                posn = 'b' + str(index + 1)
                placement = 1
            elif row3.count(playr_symb) == 2 and row3.count(' ') == 1:
                index = row3.index(' ')
                row3[index] = 'O'
                posn = 'c' + str(index + 1)
                placement = 1

            elif diagonal1.count(playr_symb) == 2 and diagonal1.count(' ') == 1:
                index = diagonal1.index(' ')
                if index == 0:
                    row1[0] = 'O'
                    posn = 'a1'
                    placement = 1
                elif index == 1:
                    row2[1] = 'O'
                    posn = 'b2'
                    placement = 1
                else:
                    row3[2] = 'O'
                    posn = 'c3'
                    placement = 1
            elif diagonal2.count(playr_symb) == 2 and diagonal2.count(' ') == 1:
                index = diagonal2.index(' ')
                if index == 0:
                    row1[2] = 'O'
                    posn = 'a3'
                    placement = 1
                elif index == 1:
                    row2[1] = 'O'
                    posn = 'b2'
                    placement = 1
                else:
                    row3[0] = 'O'
                    posn = 'c1'
                    placement = 1

            else:
                for index in range(3):
                    column = [row1[index], row2[index], row3[index]]
                    if column.count(playr_symb) == 2 and column.count(' ') == 1:
                        ix = column.index(' ')
                        if ix == 0:
                            row1[index] = 'O'
                            posn = 'a' + str(ix + 1)
                        elif ix == 1:
                            row2[index] = 'O'
                            posn = 'b' + str(ix + 1)
                        else:
                            row3[index] = 'O'
                            posn = 'c' + str(ix + 1)
                        placement = 1
                        break
    if placement == 1:
        print()
        print("Machine's move position:", posn)
        print(row1, row2, row3, sep='\n')
    return placement


# ==========================================================================

a, game = 1, 1
while a == 1:
    move, sub_case = 1, None
    row1, row2, row3 = assign()
    c = info()
    result = None
    if c == 1:
        move, sub_case = macalg_corfil1(move, None, sub_case)

    while result == None:
        print()
        m = 0
        posn = input("Enter your move position: ")
        if marking('X', posn) == 1:
            m = 1
            print(row1, row2, row3, sep='\n')
            result, a = check_result()
            if a != -1:
                game += a
                break
        else:
            continue
        if result == None and m == 1:
            t = macalg_linup2()
            if t != 1:
                move, sub_case = macalg_corfil1(move, posn, sub_case)
            result, a = check_result()
            if a != -1:
                game += a
                break
            if row1.count(' ') + row2.count(' ') + row3.count(' ') == 1:
                for group in (row1, row2, row3):
                    if group.count(' ') == 1:
                        index = group.index(' ')
                        if group == row1:
                            str_group = 'row1'
                        elif group == row2:
                            str_group = 'row2'
                        elif group == row3:
                            str_group = 'row3'
                        display_posn = position(str_group + '[' + str(index) + ']')
                        print()
                        print("Your obvious move position:", display_posn)
                        group[index] = 'X'
                        print(row1, row2, row3, sep='\n')
                result, a = terminate(0)
                game += a
else:
    print()
    print("Games played:", game)
    print("Thank you")
