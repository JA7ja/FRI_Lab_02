def numList(x):
    for i in range(1, x+2):
        printStatement = ""
        for j in range(0,i):
            printStatement = printStatement + str(j)
        print(printStatement)

def numListPalindrome(x):
    for i in range(2, x+2):
        printStatement = ""
        for j in range(1,i):
            printStatement = printStatement + str(j)
        for k in range(i-2,0,-1):
            printStatement = printStatement + str(k)
        print(printStatement)

def fullTriangleDraw(x):
    for i in range(2*x - 1, 0, -2):
        for k in range(0, int(((2*x - 1) - i)/2)):
            print(' ',end='')
        for l in range(0, ((2*x - 1)) - ((2*x - 1) - i)):
            print('*',end='')
        for m in range(0, int(((2*x - 1) - i)/2)):
            print(' ',end='')
        print("")

def hollowTriangleDraw(x):
    for i in range(x-1,0,-1):
        print(' ',end='')
    print("*",end='')
    for j in range(x-1,0,-1):
        print(' ',end='')
    print('')
    for k in range(1, x-1):
        for l in range((x-1)-k,0,-1):
            print(' ',end='')
        print("*",end='')
        for m in range(0,(k*2)-1):
            print(" ",end='')
        print("*",end='')
        for n in range((x-1)-k,0,-1):
            print(' ',end='')
        print('')
    for o in range(0, 2*x-1):
        print('*',end='')
    print("")

def hollowBox(h,w):
    for i in range(0,w):
        print("~",end="")
    print("")
    for j in range(0,h-2):
        print("~",end="")
        for k in range(0,w-2):
            print(" ",end="")
        print("~")
    for i in range(0,w):
        print("~",end="")
    print("")

def tree(x):
    for i in range(0,5):
        num_Of_Space = 5-i
        print(' '*(x+2) + num_Of_Space*' ' + '* '*i)

    for i in range(2,(x+4)):
        num_Of_Space = (x+4)-i
        print(' '*3 + num_Of_Space*' ' + '* '*i)

    for i in range(4,(x+7)):
        num_Of_Space = (x+7)-i
        print(num_Of_Space*' ' + '* '*i)

    for i in range(0,4):
        num_Of_Space = (x+4)
        print(num_Of_Space*' ' + '######')

def fullTriangleDrawTEST(x):
    for h in range(0,x*2-1, 2):
        for i in range(1,2*x-1 , 2):
            for k in range(0, int((((2*x - 1) - i)/2 -1))):
                print(' ',end='')
            for l in range(0, ((2*x - 1)) - ((2*x - 1) - i)+h):
                print('*',end='')
            for m in range(0, int((((2*x - 1) - i)/2))):
                print(' ',end='')
            print("")
        x += 1

def fullHeart():
    for i in range(0,7):
        print((7-i)*' ' + "* "*(4+i) + (12-(2*i))*' ' + '* '*(4+i))

    for i in range(0,2):
        print('* '*21)

    for i in range(21, 0, -1):
        space_num = 21 - i
        print(space_num*' ' + '* '*i)

def main():
    print("Place Holder")
    #numList(5)
    #numList(3)
    #numList(7)
    #numListPalindrome(5)
    #numListPalindrome(7)
    #numListPalindrome(9)
    #fullTriangleDrawTEST(5)
    #fullHeart()
    tree(5)
    #fullTriangleDraw(10)
    #fullTriangleDraw(15)
    #hollowTriangleDraw(5)
    #hollowTriangleDraw(7)
    #hollowTriangleDraw(9)
    #hollowBox(20,40)
    #hollowBox(10,20)
    #hollowBox(20,10)


main()
