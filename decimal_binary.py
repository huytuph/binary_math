def decimal_binary(decimal_input):
    """
    decimal to binary converter
    """
    octet = [128,64,32,16,8,4,2,1]
    binary = ''
    octet_count = 8
    count = 0

    while octet_count != 0:
        if decimal_input//octet[count] == 1:
            binary += str(1)
            decimal_input -= octet[count]
            count += 1
            octet_count -=1
        else:
            binary += str(0)
            count += 1
            octet_count -= 1
    print(f"Binary number: {binary}\n")