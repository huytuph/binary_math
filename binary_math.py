"""
binary math tool
"""
import binary_decimal, decimal_binary  
    
def _invalid():
    """invalid if user input is not accepted"""
    print("\n!! invalid option !!\nplease try again...\n")

def _return():
    """ return to previous menu"""
    while True:
        opt = str(input("\n'r' to return to previous menu: "))
        if opt == "r":
            break
        else:
            _invalid()
            continue

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
        _invalid()

##########################################################