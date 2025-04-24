def main():

    where0 = input()
    where1 = input()
    where2 = input()
    where3 = input()
    where4 = input()

    # print('=================')

    # print(where0)
    # print(where1)
    # print(where2)
    # print(where3)
    # print(where4)

    # print('=================')

    find0 = where0.find('o')
    find1 = where1.find('o')
    find2 = where2.find('o')
    find3 = where3.find('o')
    find4 = where4.find('o')

    # print(find0)
    # print(find1)
    # print(find2)
    # print(find3)
    # print(find4)

    icon = -1
    jcon = -1
    # เดี๋ยวอาจจะมีค่า icon is null แต่ไว้ก่อน

    if find0 != -1:
        icon = 0
        # jcon = find0

        word = where0.split()
        jcon = word.index('o')

    
    if find1 != -1:
        icon = 1
        # jcon = find1

        word = where1.split()
        jcon = word.index('o')


    if find2 != -1:
        icon = 2
        # jcon = find2

        word = where2.split()
        jcon = word.index('o')


    if find3 != -1:
        icon = 3
        # jcon = find3

        word = where3.split()
        jcon = word.index('o')


    if find4 != -1:
        icon = 4
        # jcon = find4

        word = where4.split()
        jcon = word.index('o')





    output = ''

    # direction = input()

    # print('icon:', icon)
    # print('jcon:', jcon)

    while(True):
        if icon == -1 and jcon == -1:
            # print('Not in Area!!!')
            output += 'Not in Area!!!'
            return output
            

        direction = input()
        
        if direction == '-1':
            # print('Stop')
            output += 'Stop'
            return output
            
        
        # print('not -1')
        
        if direction == 'U':
            # print('u')
            icon -= 1

        elif direction == 'D':
            # print('d')
            icon += 1

        elif direction == 'L':
            # print('l')
            jcon -= 1

        elif direction == 'R':
            # print('r')
            jcon += 1

        elif direction == '-1':
            # print('Stop')
            output += 'Stop'
            return output
            
        
        # print('==== ijcon after ====')
        # print('icon:', icon)
        # print('jcon:', jcon)
        # print('====  ====')

        


        for i in range(5): # จำนวนบรรทัด
            # print('*', end='')
            
            for j in range(5):
                # print('x', end=' ')
                if icon >= 5 or jcon >= 5:
                    # print('Not in Area!!!')
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += '\n'
                    
                    output += 'Not in Area!!!'
                    return output
                    
            
                if icon != -1 and jcon != -1:
                    if i == icon and j == jcon:
                        # print('o', end=' ')
                        output += 'o '
                    else:
                        # print('x', end=' ')
                        output += 'x '
                else:
                    # print('Not in Area!!!')
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += 'x x x x x'
                    output += '\n'
                    output += '\n'

                    output += 'Not in Area!!!'
                    return output
                    
            # print()
            output += '\n'
        output += '\n'

    # return output




# main()


print(main())
