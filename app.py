## QUIZE GAME IN PYTHON 


questions = [
  ["Which language was to creat fb?", "python",
   "french","javascript","php","none",4],
  ["Which is the famous porgrammin lan2uage?", "python",
   "french","javascript","php","none",2],
  ["Which is easy to learn?", "python",
   "french","javascript","php","none",3],
  ["Which is used for backend?", "python",
   "french","javascript","php","none",1]
]
  
levels = [i for i in range(1000,32000,3000)]
# print(levels)

# w = 0
# for i in range(0,len(questions)):
#     question = questions[i]
#     print(f"_____Question for Rs. {levels[i]}_____")
#     print(question[0])
#     print(f"a.{question[1]}    b.{question[2]}")
#     print(f"c.{question[3]}   c.{question[4]}")
#     reply = int(input("Answer from 1-4: "))
#     try:
#         if reply == question[-1]:
#            print(f"correct answer, you have won Rs.{levels[i]}")
#            w += levels[i]    
#         else:
#             print("Wrong answer!\n")
#             break
#     except ValueError as e:
#             print("Oops! Invalid Input..")
#     finally:
#             print("This is finally keyword...")
       
# if w>0:
#     print(f"\nYou had won total Rs.{w}🎇(❁´◡`❁)")
#     print(f"Your current scores is Rs.{w}") 
# else:
#     print("\nopps! you missed out the opportunitis😢...")
#     print(f"Your current scores is Rs.{w}") 

# with open("quixe.txt", 'r') as f:
#     data = int(f.read()) 
#     # to print data from the file we must assing the value with variable 
#     print(data)
#     if data > w:
#         print(f"your high scores is Rs.{data}")
#         # print(f.read()) not display the result from the f file
#     else:
#         with open("quixe.txt" , 'w') as f1:
#             f1.write(str(w))
#             print(f"Congratulations! You made new highscores with Rs.{w}✌️😱\n")
  
# print(type(f))

w = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"_____Question for Rs. {levels[i]}_____")
    print(question[0])
    print(f"a.{question[1]}    b.{question[2]}")
    print(f"c.{question[3]}   c.{question[4]}")
    reply = int(input("Answer from 1-4: "))
    try:
        if reply == question[-1]:
            print(f"correct answer, you have won Rs.{levels[i]}")
            w += levels[i]    
        else:
            print("Wrong answer!\n")
            break
    except Exception as e:
        print("Oops! Invalid Input..")
    finally:
        print("This is finally keyword...")

if w > 0:
    print(f"\nYou had won total Rs.{w}🎇(❁´◡`❁)")
    print(f"Your current scores is Rs.{w}") 
else:
    print("\nopps! you missed out the opportunitis😢...")
    print(f"Your current scores is Rs.{w}") 

with open("quixe.txt", 'r') as f:
    data = int(f.read()) 
    print(data)
    if data > w:
        print(f"your high scores is Rs.{data}")
    else:
        with open("quixe.txt" , 'w') as f1:
            f1.write(str(w))
            print(f"Congratulations! You made new highscores with Rs.{w}✌️😱\n")