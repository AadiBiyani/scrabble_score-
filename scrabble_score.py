one_point = ["A", "E", "I", "0", "U", "L", "N", "R", "S", "T"]
two_point = ["D", "G"]
three_point = ["B", "C", "M", "P"]
four_point = ["F", "H", "V", "W", "Y"]
five_point = "K"
eight_point = ["J", "K"]
ten_point = ["Q", "Z"]
word = input("Enter a word:")

def score(word):
    index = 0
    score = 0
    for i in range(len(word)):
        if word[index] == one_point[index]:
            score = score + 1
            index = index + 1
        elif word[index] == two_point[index]:
            score = score + 2
            index = index + 1
        elif word[index] == three_point[index]:
            score = score + 3
            index = index + 1
        elif word[index] == four_point[index]:
            score = score + 4
            index = index + 1
        elif word[index] == five_point:
            score = score + 5
            index = index + 1
        elif word[index] == eight_point[index]:
            score = score + 8
            index = index + 1
        elif word[index] == ten_point[index]:
            score = score + 10
            index = index + 1
        else:
            index = index + 1
    print (score)
    pass

score(word)
