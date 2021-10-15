def assign():
    r1 = [' ', ' ', ' ']
    r2 = [' ', ' ', ' ']
    r3 = [' ', ' ', ' ']
    return r1, r2, r3


def position(i):
    r_ps = ['r1[0]', 'r1[1]', 'r1[2]', 'r2[0]', 'r2[1]', 'r2[2]', 'r3[0]', 'r3[1]', 'r3[2]']
    p_ps = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    j = r_ps.index(i)
    e = -1
    for c in p_ps:
        e += 1
        if e == j:
            break
    return c


def info():
    print()
    print('    ', '1', '', '2', ' ', '3')
    print('a', '', r1)
    print('b', '', r2)
    print('c', '', r3)
    print()
    print("Use row name as a,b,c")
    print("Use column number as 1,2,3")
    print("For eg- a3, b1...")
    print()
    print("Your character will be X while machine's character will be O")
    print()
    print("Enter 1 if you want machine to move first")
    print("Else 2 to move first")
    print()
    c = int(input("Choice: "))
    return c


def terminate(w):
    print()
    if w == 'X':
        print("Congo! You won the game.")
        r = 1
    elif w == 'O':
        print("Alas! You lost the game.")
        r = -1
    elif w == 0:
        print("A draw!")
        r = 0

    print("Would u like to try again?")
    a = -1
    a = int(input("Yes(1)/ No(0): "))
    return r, a


def check_result():
    r = None

    a = -1
    for w in ['O', 'X']:
        p_1 = r1.count(w)
        p_2 = r2.count(w)
        p_3 = r3.count(w)

        if p_1 == 3 or p_2 == 3 or p_3 == 3:
            r, a = terminate(w)
            if r != None:
                break
        elif r1[0] == r2[1] == r3[2] == w or r1[2] == r2[1] == r3[0] == w:
            r, a = terminate(w)
            if r != None:
                break
        elif r1.count(' ') == 0:
            if r2.count(' ') == 0:
                if r3.count(' ') == 0:
                    r, a = terminate(0)
                    if r != None:
                        break
        else:
            for j in range(3):
                if r1[j] == r2[j] == r3[j] == w:
                    r, a = terminate(w)
                    if r != None:
                        break
    return r, a


def marking(t, ps):
    t_a = 'OX'
    for i in t_a:
        if i == t:
            continue
        o = i

    ps_a = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    if ps in ps_a:
        i = ps_a.index(ps)
        if i < 3:
            if r1[i] == ' ':
                r1[i] = t
                return 1
            else:
                if t == 'X':
                    print("Already Occupied")
                return 0
        elif i >= 3 and i < 6:
            if r2[i - 3] == ' ':
                r2[i - 3] = t
                return 1
            else:
                if t == 'X':
                    print("Already Occupied")
                return 0
        elif i >= 6:
            if r3[i - 6] == ' ':
                r3[i - 6] = t
                return 1
            else:
                if t == 'X':
                    print("Already Occupied")
                return 0
    else:
        print("Incorrect position")
        return -1


def macalg_corfil1(mv, ps, kmt):
    import random
    km = None
    while True:
        r1_s = ['r1[0]', 'r1[1]', 'r1[2]']
        r2_s = ['r2[0]', 'r2[1]', 'r2[2]']
        r3_s = ['r3[0]', 'r3[1]', 'r3[2]']

        c1 = [r1[0], r2[0], r3[0]]
        c1_s = ['r1[0]', 'r2[0]', 'r3[0]']
        c2 = [r1[1], r2[1], r3[1]]
        c2_s = ['r1[1]', 'r2[1]', 'r3[1]']
        c3 = [r1[2], r2[2], r3[2]]
        c3_s = ['r1[2]', 'r2[2]', 'r3[2]']

        if mv == 1:
            if ps != None and r2[1] == ' ':
                ps = 'b2'
                km = 0
            else:
                a = chr(random.randrange(97, 100, 2))
                n = str(random.randrange(1, 4, 2))
                ps = a + n
        elif mv == 2:
            if kmt == 0:
                p_ps = ('a2', 'b1', 'b3', 'c2')
                r = random.randrange(4)
                ps = p_ps[r]
            else:
                if ps in ('a2', 'b1', 'b3', 'c2'):
                    for f in (r1, r3, c1, c3):
                        if 'X' in f:
                            if f == r1:
                                a_s = r3
                                s = r3_s
                            elif f == r3:
                                a_s = r1
                                s = r1_s
                            elif f == c1:
                                a_s = c3
                                s = c3_s
                            elif f == c3:
                                a_s = c1
                                s = c1_s
                            if 'O' in f:
                                i = f.index(' ')
                                km = 1
                            else:
                                i = a_s.index('O')
                            if i == 0:
                                j = 2
                            elif i == 2:
                                j = 0
                            ps = position(s[j])

                else:
                    a = chr(random.randrange(97, 100, 2))
                    n = str(random.randrange(1, 4, 2))
                    ps = a + n
        elif mv == 3 and kmt == 1:
            for f in (r1, r2, r3, c1, c2, c3):
                if f.count('O') == 1:
                    if f == r1:
                        s = r1_s
                    elif f == r3:
                        s = r3_s
                    elif f == c1:
                        s = c1_s
                    elif f == c3:
                        s = c3_s
                    i = f.index('O')
                    if i == 0:
                        j = 2
                    elif i == 2:
                        j = 0
                    ps = position(s[j])
        else:
            a = chr(random.randrange(97, 100, 2))
            n = str(random.randrange(1, 4, 2))
            ps = a + n

        if marking('O', ps) == 1:
            t = marking('O', ps)
            mv += 1
            print()
            print("Machine's move position:", ps)
            print(r1, r2, r3, sep='\n')
            break

    return mv, km


def macalg_linup2():
    d1 = [r1[0], r2[1], r3[2]]
    d2 = [r1[2], r2[1], r3[0]]

    t = 0
    for p in ('O', 'X'):
        if t == 0:
            if r1.count(p) == 2 and r1.count(' ') == 1:
                i = r1.index(' ')
                r1[i] = 'O'
                ps = 'a' + str(i + 1)
                t = 1
            elif r2.count(p) == 2 and r2.count(' ') == 1:
                i = r2.index(' ')
                r2[i] = 'O'
                ps = 'b' + str(i + 1)
                t = 1
            elif r3.count(p) == 2 and r3.count(' ') == 1:
                i = r3.index(' ')
                r3[i] = 'O'
                ps = 'c' + str(i + 1)
                t = 1
            elif d1.count(p) == 2 and d1.count(' ') == 1:
                i = d1.index(' ')
                if i == 0:
                    r1[0] = 'O'
                    ps = 'a1'
                    t = 1
                elif i == 1:
                    r2[1] = 'O'
                    ps = 'b2'
                    t = 1
                else:
                    r3[2] = 'O'
                    ps = 'c3'
                    t = 1
            elif d2.count(p) == 2 and d2.count(' ') == 1:
                i = d2.index(' ')
                if i == 0:
                    r1[2] = 'O'
                    ps = 'a3'
                    t = 1
                elif i == 1:
                    r2[1] = 'O'
                    ps = 'b2'
                    t = 1
                else:
                    r3[0] = 'O'
                    ps = 'c1'
                    t = 1
            else:
                for i in range(3):
                    l = [r1[i], r2[i], r3[i]]
                    if l.count(p) == 2 and l.count(' ') == 1:
                        ix = l.index(' ')
                        if ix == 0:
                            r1[i] = 'O'
                            ps = 'a' + str(ix + 1)
                        elif ix == 1:
                            r2[i] = 'O'
                            ps = 'b' + str(ix + 1)
                        else:
                            r3[i] = 'O'
                            ps = 'c' + str(ix + 1)
                        t = 1
                        break
    if t == 1:
        print()
        print("Machine's move position:", ps)
        print(r1, r2, r3, sep='\n')
    return t


# ==========================================================================

a, g = 1, 1
while a == 1:
    mv, km = 1, None
    r1, r2, r3 = assign()
    c = info()
    r = None
    if c == 1:
        mv, km = macalg_corfil1(mv, None, km)

    while r == None:
        print()
        m = 0
        ps = input("Enter your move position: ")
        if marking('X', ps) == 1:
            m = 1
            print(r1, r2, r3, sep='\n')
            r, a = check_result()
            if a != -1:
                g += a
                break
        else:
            continue
        if r == None and m == 1:
            t = macalg_linup2()
            if t != 1:
                mv, km = macalg_corfil1(mv, ps, km)
            r, a = check_result()
            if a != -1:
                g += a
                break
            if r1.count(' ') + r2.count(' ') + r3.count(' ') == 1:
                for l in (r1, r2, r3):
                    if l.count(' ') == 1:
                        f = l.index(' ')
                        if l == r1:
                            s_l = 'r1'
                        elif l == r2:
                            s_l = 'r2'
                        elif l == r3:
                            s_l = 'r3'
                        p = position(s_l + '[' + str(f) + ']')
                        print()
                        print("Your obvious move position:", p)
                        l[f] = 'X'
                        print(r1, r2, r3, sep='\n')
                r, a = terminate(0)
                g += a
else:
    print()
    print("Games played:", g)
    print("Thank you")
