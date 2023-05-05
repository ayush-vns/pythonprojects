questions = [{"question": "1- Which one of these is a Sattabaz ?", "opta": "Sachin", "optb": "Anand", "optc": "Rohit",
              "optd": "All of these", "answer": 4},
             {
                 "question": "2- Jimmy's father has three sons- Paul I and Paul II. Can you guess the name of the third "
                             "son?", "opta": "Paul III", "optb": "Jerin", "optc": "Jimmy", "optd": "None", "answer": 3},
             {"question": "3- How many days in one week ?", "opta": "four", "optb": "three", "optc": "seven",
              "optd": "nine", "answer": 3}
    , {"question": "4- How many finger in one hand?", "opta": "3", "optb": "6", "optc": "7", "optd": "5", "answer": 4}]

qno = 0
score = 0
n = len(questions)
while True:
    if qno >= n:
        if score == 4:
            print("excellent")
        if score == 3:
            print("qualify")
        print("test over", "score = ", score, "/", n)
        break
    question = questions[qno]
    print(question["question"])
    print(" 1-", (question["opta"]), "2-", (question["optb"]), "3-", (question["optc"]), "4-", (question["optd"]))
    answer = int(input("1,2,3,4\n", ))
    if answer == question["answer"]:
        print("right")
        score += 1
    else:
        print("Wrong")
    qno += 1
