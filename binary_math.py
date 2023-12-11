"""
binary math tool
"""
import binary_decimal, decimal_binary, os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def _invalid():
    """invalid if user input is not accepted"""
    print("\n!! invalid option !!\nplease try again...\n")

##
##

"""
Main menu for binary math tool
Current options:
(1) Binary to Decimal conversion
(2) Decimal to Binary conversion
(x) Exit 
"""
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
        while True:
            binary_input = input("\nEnter binary number: ")
            binary_decimal.binary_decimal(binary_input)
            opt = str(input("\nreturn to previous menu? (y/N): "))
            if opt == "n" or opt == "N":
                continue
            elif opt == "y" or opt == "Y":
                break
        clear_screen()
        
    elif option == "2":
        while True:
            decimal_input = int(input("\nEnter decimal number: "))
            decimal_binary.decimal_binary(decimal_input)
            opt = str(input("\nreturn to previous menu? (y/N): "))
            if opt == "n" or opt == "N":
                continue
            elif opt == "y" or opt == "Y":
                break
        clear_screen()
    else:
        _invalid()

##
##