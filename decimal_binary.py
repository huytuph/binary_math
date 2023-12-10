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
