sub1 = float(input("Enter markes in maths: "))
sub2 = float(input("Enter markes in science: "))
sub3 = float(input("Enter markes in kannada: "))

total = sub1 + sub2 +sub3
per1 = (sub1/100)*100
per2 = (sub2/100)*100
per3 = (sub3/100)*100

if per1>33 and per2>33 and per3>33:
    print("Youe are passed")
else:
    print("You are failed")    