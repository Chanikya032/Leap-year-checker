# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=int(year%4)
b=int(year%100)
c=int(year%400)
if a==0:
    if b==0:
        print(f"Not leap year.")
    elif c==0:
        print(f"Not leap year.")
    else:
        print(f"Leap year.")
else:
    print(f"Not leap year.")
