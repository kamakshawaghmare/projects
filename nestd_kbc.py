Question_list=["what is the capital of India?",
"what is our national fruit?",
"what is our national bird?"]
option=[["delhi","chennai","chandigarh","bhopal"],
["mango","apple","orange","grapes"],
["sparrow","peacock","crow","hen"]]
solution=[1,1,2]
option_list=[["1.delhi","4.bhopal"],["2.apple","1.mango"],["3.crow","2.peacock"]]
i=0
sum=0
count=0
while i<len(Question_list):
    print(Question_list[i])
    j=0
    k=1
    while j<=len(option):
        print(k,".",option[i][j])
        k=k+1
        j=j+1
    num=input("do you want to 50 50 life line")
    if num=="yes":
        print("50 50 life line")
        num1=int(input("enter the number"))
        if num1==solution[i]:
            sum=sum+1000
            print("your answer is currect")
            print(" you win Rs/-",sum)
        else:
            print("you allready use your lifeline")
            num2=int(input("enter the number"))
            if num2==solution[i]:
                print("your answer is right")
                sum=sum+2000
                print("you win Rs/-",sum)
            else:
                print("your answer is wrong")
                print("you win Rs/-",sum)
                break
        i=i+1