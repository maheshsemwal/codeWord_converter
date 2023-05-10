import random
def code():
    sen = input("Enter a sentence to Code: ")              
    sen = sen.split()
    print("Coded Sentence: ",end="")
    for i in sen:
            lis = list(i)
            if len(lis)<=2:
                lis.append(lis[0])
                lis.remove(lis[0])
                for i in lis:
                    print(i, end="")
            elif len(lis)>2:
                lis.append(lis[0])
                lis.remove(lis[0])
                alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                random_letters=random.sample(alphabets,3)
                lis[:0]=random_letters
                lis.extend(random_letters)
                for i in lis:
                    print(i, end="")              
            print(end = " ")    

            
            
def deCode():
    sen = input("Enter a sentence to DeCode: ")              
    sen = sen.split()
    print("DeCoded Sentence: ",end="")
    for i in sen:
            lis = list(i)
            if len(lis)<=2:
                lis.append(lis[0])
                lis.remove(lis[0])
                for i in lis:
                    print(i, end="")
            
            if len(lis)>2:
                lis = lis[3:-3]
                lis.insert(0,lis[len(lis)-1])
                lis.pop()
                for i in lis:
                    print(i,end="")
            print(end=" ")

                           


print("\t\t\t..............Codeword Converter...............")
print('''Choose corrosponding Number to Code or DeCode:
      1. Code
      2. Decode''')
a = int(input("Enter Option: "))
match a:
    case 1:
        code()
    case 2:
        deCode()