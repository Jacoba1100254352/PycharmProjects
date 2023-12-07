height = int(input("Enter the height you reached (in inches): "))

if height < 50:
    print("Sorry, you do not win a prize!")
elif height < 100:
    print("You win a small stuffed animal!")
elif height < 150:
    print("You win a frisbee!")
else:
    print("You win a large stuffed animal!")
