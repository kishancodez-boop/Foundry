A = input("Enter your name: ")
print("Welcome to Become a Korodpati,", A)
print("Please answer these 3 questions")
print("Each question carries 10,000 rs")
Q = ["What's the other name of 10th standard?","Name any one interpreted programming language?","What is the full form of HTML?"]
A = ["SSLC", "python", "Hyper Text Markup Language"]
score = 0
print(Q[0])
ans = input("Your answer: ")
if ans.strip().lower() == A[0].lower():
    print("Your answer is correct")
    score += 10000
else:
    print("Your answer is wrong")
print("Your current score is:", score)
print(Q[1])
ans = input("Your answer: ")
if ans.strip().lower() == A[1].lower():
    print("Your answer is correct")
    score += 10000
else:
    print("Your answer is wrong")
print("Your current score is:", score)
print(Q[2])
ans = input("Your answer: ")
if ans.strip().lower() == A[2].lower():
    print("Your answer is correct")
    score += 10000
else:
    print("Your answer is wrong")
print("Your current score is:", score)
print("🎉 Your TOTAL SCORE is:", score)
