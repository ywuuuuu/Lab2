def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI=weight/(height*height)

    print("Your BMI is " + str(BMI))

    if BMI<18.5:
        print("Under Weight")
        return -1
    elif 18.5<=BMI<=25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1

calculate_bmi(weight=57,height=1.73)