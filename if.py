price = 1000000

has_good_credet = False
has_bad_credet  = False

if has_good_credet:
    down_pyment = 0.1 * price
    print(down_pyment)
elif has_bad_credet:
    down_pyment = 0.2 *price
    print(down_pyment)
else:
    down_pyment = 0.15 *price
    print(down_pyment)


    has_good_credet = True
    has_hight_income= False
    has_criminal_record = False

    if has_good_credet and has_hight_income:
        print("Eligible for loan")

    if has_good_credet or has_hight_income:
        print("Not Eligible for Loan")

    if has_good_credet and not has_criminal_record:
        print("Eligable for loan becasue don't have criminal record")



    name = input("Write your good name please?")

    if len(name) < 3 :
        print("Name must be at least 3 characters")
    elif len(name) > 10:
        print("name can be a maximum of 10 characters")
    else:
        print("Your Good Name is ", name)
