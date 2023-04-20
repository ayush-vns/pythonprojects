questions = [{"question": "Is Python a Programming Language ?T/F", "answer": True}
    , {"question": "Is Bhojpuri a Programming Language ?T/F", "answer": False}
    , {"question": "An ostrich’s eye is bigger than its brain ?T/F", "answer": True}
    , {"question": "There are 9 planets in our Solar System ?T/F", "answer": False}]

qno = 0
score = 0
n = len(questions)
name = input("Enter your name =")
while True:
    if qno >= n:
        percentage = score * 100 / n
        print("name = ", name, "score = ", score, "/", n, "  percentage = ", percentage, "% Test Over")
        break
    question = questions[qno]
    print(question["question"])
    answer = int(input("1/0 = "))
    if answer == question["answer"]:
        print("Right")
        score += 1


    else:
        print("Wrong")
    qno += 1
