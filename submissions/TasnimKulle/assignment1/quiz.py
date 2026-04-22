# Quiz yar
print("welcome to my easy quiz!")
score=0
name=input("what is your name?")
print("welcome",name ,"!")
print (name + ", lets start the quiz!")
print("Q1: waa maxay python?")
answer1=input("jawaab taadu waa: ")
if answer1 == "programming language":
    print("sax")
    score += 1
else:
    print("Qalad")
print("Q2: Waa maxay extansionka file python ah ?")
answer2 = input ("Jawaabtu waa: ")
if answer2 == ".py":
    print("sax")
    score += 1
else:
    print("waa Qalad")
print ("Q3: waxad ku soo koob taa Muhimada python hal Eray?")
answer3= input("jawaabtu waa: ")
if answer3=="easy":
    print("sax")
    score += 1
else:
    print("waa Qalad")
print(name,"!" + " waxaad Heshay " ,score ,"dhibcood" )
