print("==== Temperature Converter====")
print("1 Celsius to Fahrenheit")
print("2 Fahrenheit to Celsius")
print("3 Celsius to kelvin")

choice=input("Enter your choice:")
temp=float(input("Enter temperature:"))

if choice=="1":
    result=(temp*9/5)+32
    print("Temperature in Fahrenheit:",round(result,2))

elif choice=="2":
    result=(temp-32)*5/9
    print("Temperatre in Celsius:",round(result,2))

elif choice=="3":
    result=temp+273.15
    print("Temperature in kelvin:",round(result,2),"K")

else:
    print("Invalid choice!")