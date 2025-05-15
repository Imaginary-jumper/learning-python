default="abcdefghijklmnopqrstuvwxyz"
text_1 = str(input("please enter your 1st string:"))
text_2 = str(input("please enter your 2nd string:"))

print("lenghth of text 1 =", len(text_1))
print("lenghth of text 2 =", len(text_2))

print("we provide following services:")
print("1) Mocking SpongeBob case")
print("2) Matching words")
print("3) Addition to index of words")
print("4) merge words")
print("5) exit")

def choose():
    choice = int(input("please choose the s.no. of the service you would like to opt for:"))
    if choice == 1:
        choice2= int(input("which string 1st or 2nd:"))
        if choice2 == 1:
            new_text = text_1
            ask1(new_text)
        if choice2== 2:
            new_text = text_2
            ask1(new_text)
        else:
            print("please choose from 1 or 2 only")
            choose()
    elif choice ==2:
        match()
    elif choice ==3:
        fun_add()
    elif choice ==4:
        merge()
    elif choice ==5:
        exit()
    else:
        print("please choose a valid service")
        choose()
        
#trial section 1:
def match():
    for i in text_2:
        A=text_1.find(i)
        if A==-1:
            print("Match Not Found for this word :",i)
        else:
            b= A+1
            print(i ,":", b)
    choose()
    
# trial section 2:
def fun_add():
    shift = int(input("please enter the addition to each digit you desire:"))
    new_text=""
    for i in text_1.lower():
        index= default.find(i)
        if index==-1:
            new_text += " "
        else:
            index = (index + shift) % len(default)
            new_text += default[index]
    new_text += " "

    for i in text_2.lower():
        index= default.find(i)
        if index==-1:
            new_text += " "
        else:
            index = (index + shift) % len(default)
            new_text += default[index]
    print(new_text)
    choose()
    
# section 3:
def ask1(new_text):
    index=-1
    new_text2 = ""
    for j in new_text:
        index = (index + 1) % len(new_text)
        if index % 2 == 0:
            new_text2= new_text2 + new_text[index].upper()
        else:
            new_text2= new_text2 + new_text[index]
    print(new_text2)
    choose()
    
def merge():
    print (text_1 , " ", text_2)
    choose()
choose()
