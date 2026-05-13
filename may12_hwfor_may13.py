Jay = int(input("Enter Jay's Age: "))
Viru = int(input("Enter Viru's Age: "))
Gabbar = int(input("Enter Gabbar's Age: "))

if Jay > Viru and Jay > Gabbar:
    print ("Jay is the Oldest")

elif Viru > Jay and Viru > Gabbar:
    print("Viru is the Oldest")

elif Gabbar > Jay and Gabbar > Viru:
    print("Gabbar is the Oldest")

else:
    print("They all are same age")
