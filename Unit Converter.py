print("Welcome to SHUNNO's Length and Time Unit Converter")
print("Only supports length and time.")
print("Type L for Length or type T for time.")
var1 = input("Enter your unit: ")
if var1 == "L":
    print("Okay you selected Length")
    print(
        "Type Kilo for Kilometer. "
        "Type Hecto for Hectometer. "
        "Type Deca for Decameter. "
        "Type Base for Meter. "
        "Type Deci for Decimeter. "
        "Type Centi for Centimeter. "
        "Type Mili for Milimeter."
    )
    var2 = input("Enter 1st unit: ")
    var3 = input("Enter 2nd unit: ")
    var4 = float(input("Enter the number of "+var2+" to convert to "+var3+": "))
    if var2 == "Kilo" and var3 == "Hecto":
        print(var4*10)
    if var2 == "Hecto" and var3 == "Kilo":
        print(var4/10)
    if var2 == "Kilo" and var3 == "Deca":
        print(var4*100)
    if var2 == "Deca" and var3 == "Kilo":
        print(var4/100)
    if var2 == "Kilo" and var3 == "Base":
        print(var4*1000)
    if var2 == "Base" and var3 == "Kilo":
        print(var4/1000)
    if var2 == "Kilo" and var3 == "Deci":
        print(var4*10000)
    if var2 == "Deci" and var3 == "Kilo":
        print(var4/10000)
    if var2 == "Kilo" and var3 == "Centi":
        print(var4*100000)
    if var2 == "Centi" and var3 == "Kilo":
        print(var4/100000)
    if var2 == "Kilo" and var3 == "Mili":
        print(var4*1000000)
    if var2 == "Mili" and var3 == "Kilo":
        print(var4/1000000)
    if var2 == "Hecto" and var3 == "Deca":
        print(var4*10)
    if var2 == "Deca" and var3 == "Hecto":
        print(var4/10)
    if var2 == "Hecto" and var3 == "Base":
        print(var4*100)
    if var2 == "Base" and var3 == "Hecto":
        print(var4/100)
    if var2 == "Hecto" and var3 == "Deci":
        print(var4*1000)
    if var2 == "Deci" and var3 == "Hecto":
        print(var4/1000)
    if var2 == "Hecto" and var3 == "Centi":
        print(var4*10000)
    if var2 == "Centi" and var3 == "Hecto":
        print(var4/10000)
    if var2 == "Hecto" and var3 == "Mili":
        print(var4*1000000)
    if var2 == "Mili" and var3 == "Hecto":
        print(var4/1000000)
    if var2 == "Deca" and var3 == "Base":
        print(var4*10)
    if var2 == "Base" and var3 == "Deca":
        print(var4/10)
    if var2 == "Deca" and var3 == "Deci":
        print(var4*100)
    if var2 == "Deci" and var3 == "Deca":
        print(var4/100)
    if var2 == "Deca" and var3 == "Centi":
        print(var4*1000)
    if var2 == "Centi" and var3 == "Deca":
        print(var4/1000)
    if var2 == "Deca" and var3 == "Mili":
        print(var4*10000)
    if var2 == "Mili" and var3 == "Deca":
        print(var4/10000)
    if var2 == "Base" and var3 == "Deci":
        print(var4*10)
    if var2 == "Deci" and var3 == "Base":
        print(var4/10)
    if var2 == "Base" and var3 == "Centi":
        print(var4*100)
    if var2 == "Centi" and var3 == "Base":
        print(var4/100)
    if var2 == "Base" and var3 == "Mili":
        print(var4*1000)
    if var2 == "Mili" and var3 == "Base":
        print(var4/1000)
    if var2 == "Deci" and var3 == "Centi":
        print(var4*10)
    if var2 == "Centi" and var3 == "Deci":
        print(var4/10)
    if var2 == "Deci" and var3 == "Mili":
        print(var4*100)
    if var2 == "Mili" and var3 == "Deci":
        print(var4/100)
    if var2 == "Centi" and var3 == "Mili":
        print(var4*10)
    if var2 == "Mili" and var3 == "Centi":
        print(var4/10)
elif var1 == "T":
    print("Okay you selected Time")
    print(
        "Type Sec for Second. "
        "Type Min for Minute. "
        "Type Hour for Hour. "
        "Type Day for Day. "
        "Type Week for Week. "
        "Type Mon for Month. "
        "Type Year for Year."
    )
    var5 = input("Enter 1st unit: ")
    var6 = input("Enter 2nd unit: ")
    var7 = float(input("Enter the number of "+var5+" to convert to "+var6+": "))
    if var5 == "Sec" and var6 == "Min":
        print(var7/60)
    if var5 == "Min" and var6 == "Sec":
        print(var7*60)
    if var5 == "Sec" and var6 == "Hour":
        print(var7/3600)
    if var5 == "Hour" and var6 == "Sec":
        print(var7*3600)
    if var5 == "Sec" and var6 == "Day":
        print(var7/86400)
    if var5 == "Day" and var6 == "Sec":
        print(var7*86400)
    if var5 == "Sec" and var6 == "Week":
        print(var7/604800)
    if var5 == "Week" and var6 == "Sec":
        print(var7*608400)
    if var5 == "Sec" and var6 == "Mon":
        print(var7/2592000)
    if var5 == "Mon" and var6 == "Sec":
        print(var7*2592000)
    if var5 == "Sec" and var6 == "Year":
        print(var7/31104000)
    if var5 == "Year" and var6 == "Sec":
        print(var7*31104000)
    if var5 == "Min" and var6 == "Hour":
        print(var7/60)
    if var5 == "Hour" and var6 == "Min":
        print(var7*60)
    if var5 == "Min" and var6 == "Day":
        print(var7/1440)
    if var5 == "Day" and var6 == "Min":
        print(var7*1440)
    if var5 == "Min" and var6 == "Week":
        print(var7/10080)
    if var5 == "Week" and var6 == "Min":
        print(var7*10080)
    if var5 == "Min" and var6 == "Mon":
        print(var7/43200)
    if var5 == "Mon" and var6 == "Min":
        print(var7*43200)
    if var5 == "Min" and var6 == "Year":
        print(var7/518400)
    if var5 == "Year" and var6 == "Min":
        print(var7*518400)
    if var5 == "Hour" and var6 == "Day":
        print(var7/24)
    if var5 == "Day" and var6 == "Hour":
        print(var7*24)
    if var5 == "Hour" and var6 == "Week":
        print(var7/168)
    if var5 == "Week" and var6 == "Hour":
        print(var7*168)
    if var5 == "Hour" and var6 == "Mon":
        print(var7/720)
    if var5 == "Mon" and var6 == "Hour":
        print(var7*720)
    if var5 == "Hour" and var6 == "Year":
        print(var7/8760)
    if var5 == "Year" and var6 == "Hour":
        print(var7*8760)
    if var5 == "Day" and var6 == "Week":
        print(var7/7)
    if var5 == "Week" and var6 == "Day":
        print(var7*7)
    if var5 == "Day" and var6 == "Mon":
        print(var7/30)
    if var5 == "Mon" and var6 == "Day":
        print(var7*30)
    if var5 == "Day" and var6 == "Year":
        print(var7/365)
    if var5 == "Year" and var6 == "Day":
        print(var7*365)
    if var5 == "Week" and var6 == "Mon":
        print(var7/4.28571429)
    if var5 == "Mon" and var6 == "Week":
        print(var7*4.28571429)
    if var5 == "Mon" and var6 == "Year":
        print(var7/12)
    if var5 == "Year" and var6 == "Mon":
        print(var7*12)
else:
    print("Something went wrong. Please try again.")