
"""def BMI(): #defines function

    weight = 0
    height = 0
    Height = 0
    BMI = 0
    target_bmi = 0
    weight = float(input("Enter your weight"))#tells user to enter their weight
    while 30<=weight or weight>=250:
        print("weight",weight,"is invalid enter a weight between 30 and 250")
        if weight<=30 or 250>=weight:
            break
        weight = float(input("Enter your weight"))
        if weight<=30 or 250>=weight:
            print(weight)
        height = float(input("Enter your height in cm"))#tells user to input their height
        if height>120 or height<=210:
            print(BMI)
        else:
            print("Height is invalid")
        Height = height/100#calculates in meteres
        Height_m = Height ** 2 #height in meteres squared
        BMI = weight/Height_m #divides weight by the height
        print(BMI) #prints BMI
        if BMI <18.5:
            print("you are underweight")
        elif BMI <= 18.5 or BMI <= 24.9:
            print("you are normal weight")
        elif BMI>=25 or BMI >=29.9:
            print("you are overweight")
        elif BMI >= 30:
            print("you are obese")
        target_bmi = 22#asks user what their target BMI is
        print(target_bmi) #prints the target BMI
        target_weight=target_bmi*(Height_m)
        print(target_weight)#prints target weight
        Weight_change=target_weight - weight
        if Weight_change > 0: #selection process
            print("If you would like to reach the BMI of",target_bmi,"you have to lose",target_weight,".")#prints whats in the bracket
        elif Weight_change<0:
            print("if you would like to reach the BMI of",target_bmi,"you have to gain",target_weight,".")#prints what in the brackets
    #BMR
def BMR(): #defines BMR
        weight = 0
        height = 0
        age = 0
        gender = 0
        weight = float(input("Enter your weight in Kg"))#tells user to enter the weight in kg
        height = float(input("Enter your height in cm"))#tells user to enter their height
        age = int(input("Enter your age"))#tells user to enter their age
        if age<=14 or age>=100:
            print("age is invalid")
        else:
            print("age is valid")
        gender = input("Are you a male or female?").lower() #asks user if they are a male or female
        if gender == "male": #if statement
            BMR = 88.362 + (13.397 * weight)+(4.799 * height)-(5.677 * age)#calculation for BMR
        elif gender == "female":
            BMR = 447.593 + (9.247 * weight)+(3.098 * height)-(4.330 * age)#BMR calculation
        else:
            BMR = None
            print("Gender entered is invalid")#prints error message
        print("BMR =", BMR)#prints BMR
    #solution selection BMI or BMR
def main(): #defines function
    calculate = input("Would you like to calculate BMI or BMR:").upper()
    if calculate == "BMI":
        BMI()
    elif calculate == "BMR":
        BMR()
main() #calls function"""

def BMI():  # Defines BMI function
    # Get valid weight input
    while True:
        try:
            weight = float(input("Enter your weight in kg (30–250): ")) #Tells user to enter a weight within their set parameters. If their weight is not within the set parameters the code will not run
            if 30 <= weight <= 250: #if the weight is less than or equal to 30 and 250 then the weight entered is valid
                break
            else: #if not
                print("Weight is invalid. Please enter a value between 30 and 250.") #Tells user to enter a valid weight within the set parameters
        except ValueError:
            print("Invalid input. Please enter a number.") #if the user has entered a letter or a special character on accident instead of a number in the set parameters, the programm will ask the user to re-enter a number

    # Get valid height input
    while True:
        try:
            height_cm = float(input("Enter your height in cm (120–210): ")) #asks user to enter their height in the set parameters
            if 120 <= height_cm <= 210: #if the height is less than or equal to 120 and 210 the height is valid 
                break
            else: #if not
                print("Height is invalid. Please enter a value between 120 and 210.")#The height entered is invalid and you must re-enter it
        except ValueError:
            print("Invalid input. Please enter a number.") #if the user has entered a letter or a special character on accident instead of a number in the set parameters, the programm will ask the user to re-enter a number

    # BMI calculation
    height_m = height_cm / 100 #height divided by100
    bmi = weight / (height_m ** 2) #bmi calculation is weight divided by height to the power of 2
    print(f"\nYour BMI is: {bmi:.2f}")

    # BMI category
    if bmi < 18.5:
        print("You are underweight.") #prints to the user their current weight status
    elif bmi <= 24.9:
        print("You are normal weight.") #prints to the user their current weight status
    elif bmi <= 29.9:
        print("You are overweight.") #prints to the user their current weight status
    else:
        print("You are obese.") #prints to the user their current weight status

    # Target BMI and weight change
    target_bmi = 22
    target_weight = target_bmi * (height_m ** 2)
    weight_change = target_weight - weight

    print(f"\nTo reach a BMI of {target_bmi}, your target weight should be: {target_weight:.2f} kg.") #prints what target weight should be
    if weight_change < 0:
        print(f"You need to lose {-weight_change:.2f} kg.") #prints what you should do from ypur current status
    elif weight_change > 0:
        print(f"You need to gain {weight_change:.2f} kg.") #prints what you should do from ypur current status
    else:
        print("You are already at your target BMI!") #prints that the user is in the best body weight


def BMR():  # Defines BMR function
    try:
        weight = float(input("Enter your weight in kg: ")) #asks user to enter their weight
        height = float(input("Enter your height in cm: ")) #asks user to enter their height
        age = int(input("Enter your age (14–100): ")) #asks user to enter their age

        if not (14 <= age <= 100): #if the age is not in the set parameters
            print("Age is invalid. Please enter a value between 14 and 100.") #prints the age entered is not valid
            return

        gender = input("Are you male or female? ").strip().lower() #asks the user for their gender

        if gender == "male": 
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age) #male calculations for BMR
        elif gender == "female":
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age) #Female calculation for BMR
        else:
            print("Gender entered is invalid.") #prints gender entered is invalid
            return

        print(f"\nYour BMR is: {bmr:.2f} calories/day")
    except ValueError:
        print("Invalid input. Please enter numerical values where appropriate.")


def main():  # Main menu
    choice = input("Would you like to calculate BMI or BMR? ").strip().upper()
    if choice == "BMI":
        BMI()
    elif choice == "BMR":
        BMR()
    else:
        print("Invalid choice. Please type 'BMI' or 'BMR'.")

# Call the main function
main()
