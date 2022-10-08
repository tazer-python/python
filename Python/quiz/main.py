from _class import quiz;

def ask(arr):
    correct = 0
    for i in arr:
        print(i.getQuestion())
        ans = input("Enter answer: ").lower()
        if ans == i.getAns():
            correct += 1
        else:
            pass
    print("You got " + str(correct) + "/" + str(len(arr)))

def main():
    q1 = quiz("What color is a banana", "yellow")
    q2 = quiz("What color is a apple", "red")
    q3 = quiz("What color is a dragonfruit", "pink")
    arr = [q1,q2,q3]
    ask(arr)

if __name__ == "__main__":
    main()