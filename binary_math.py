import binary_decimal, decimal_binary, os


def clear_screen():
    """
    clears screen for all operating systems
    """
    if os.name == 'nt': # 'nt' == windows
        os.system('cls')    # if os = windows:
    else:
        os.system('clear')  # if os = linux/unix:

def _invalid():
    """invalid if user input is not accepted"""
    print("\n!! invalid option !!\nplease try again...\n")


# Main menu for binary math tool
while True:
    clear_screen()
    print("""
>> BINARY MATH TOOL <<\n          
(1) Binary to Decimal conversion
(2) Decimal to Binary conversion
(q) Exit """)
    option = str(input("Select an option: "))
    if option == "q" or option == "Q":
        exit()     
    elif option == "1":   
        while True:
            clear_screen()
            binary_input = input("\nEnter binary number: ")
            binary_decimal.binary_decimal(binary_input)
            opt = str(input("\nreturn to previous menu? (y/N): "))
            if opt == "n" or opt == "N":
                continue
            elif opt == "y" or opt == "Y":
                break        
    elif option == "2":
        while True:
            clear_screen()
            decimal_input = int(input("\nEnter decimal number: "))
            decimal_binary.decimal_binary(decimal_input)
            opt = str(input("\nreturn to previous menu? (y/N): "))
            if opt == "n" or opt == "N":
                continue
            elif opt == "y" or opt == "Y":
                break
    else:
        _invalid()