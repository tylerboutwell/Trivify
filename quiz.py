
def run_quiz(question_list):
        score = 0
        for question in question_list.values():
            print(question["question"])
            for option in question["options"]:
                print(option)
            answer = input("Enter your answer: (A, B, or C): ").upper()
            if answer == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")
        print(f"You got {score} correct out of {len(question_list)} questions.")