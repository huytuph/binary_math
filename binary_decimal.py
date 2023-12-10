# BINARY MATH TOOL
# binary > decimal converter can do up to 8 binary digits


# binary to decimal conversion
def binary_decimal():
    octet = [128,64,32,16,8,4,2,1]
    binary = []
    decimal = []
    decimal_total = 0
    binary_input = input("Enter binary number(max 8digits): ")
    
    if len(binary_input) <= 8:
        for num in binary_input:
            binary.append(int(num))
        count = 0
        while count != 8:
            for x in binary:
                if x != 0:
                    decimal.append(octet[count])
                    count += 1
                else:
                    decimal.append(0) 
                    count += 1
        for dec in decimal:
            decimal_total += dec
        print(f"Decimal number: {decimal_total}")    
    else:
        print("invalid")
       

# decimal to binary conversion
def decimal_binary():
    octet = [128,64,32,16,8,4,2,1]
    binary = []
    decimal_input = int(input("enter decimal number: "))
    octet_count = 8
    count = 0

    while octet_count != 0:
        if decimal_input//octet[count] == 1:
            binary.append(1)
            decimal_input -= octet[count]
            count += 1
            octet_count -=1
        else:
            binary.append(0)
            count += 1
            octet_count -= 1
    print(f"Binary number: {binary}")
    
binary_decimal()
