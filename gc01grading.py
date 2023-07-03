def getinput(prompt,max):
    v = float(input(prompt))
    while v<0 or v>max:
        print("Error: invalid range: 0-"+str(max))
        v = float(input(prompt))
    return v

print("Please fill out the form.")
a = getinput("คะแนนเก็บ: ",30)
b = getinput("คะแนนกลางภาค: ",30)
c = getinput("คะแนนปลายภาค: ",40)

sum = a+b+c

if sum<50:
    print("F")
elif sum>=80:
    print("A")
else:
    print(["D","D+","C","C+","B","B+"][int(sum/5-10)])