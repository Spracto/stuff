def grade(x):
    if x >= 60 and x <=69:
        return "Your grade is a D"
    elif x >= 70 and x <= 79:
        return "Your grade is a C"
    elif x >= 80 and x <= 89:
        return "Your grade is a B"
    elif x>= 90:
        return "Your grade is an A"
    else:
        return "Your grade is an F"

y = 1
scores = []

while len(scores) < 10:
    print "What is your test score for test", y
    z = input()
    scores.append(z)
    y = y + 1

w = 0

while w < 10:
    print "Score: "+ str(scores[w]) + ";", grade(scores[w])
    w = w + 1
