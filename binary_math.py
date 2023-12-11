"""
binary math tool
"""
import binary_decimal, decimal_binary

def invalid():
    print("\ninvalid option!")   


##########################################################
"""
Main menu for binary math tool
Current options:
(1) Binary to Decimal conversion
(2) Decimal to Binary conversion
(x) Exit 
"""
#print("\n>> BINARY MATH TOOL <<")
while True:
    print("""
>> BINARY MATH TOOL <<
          
(1) Binary to Decimal conversion
(2) Decimal to Binary conversion
(x) Exit """)
    option = str(input("Select an option: "))
    if option == "x":
        exit()
        
    elif option == "1":   
        binary_input = input("\nEnter binary number: ")
        binary_decimal.binary_decimal(binary_input)
        
    elif option == "2":
        decimal_input = int(input("\nEnter decimal number: "))
        decimal_binary.decimal_binary(decimal_input)
    else:
        invalid()

##########################################################