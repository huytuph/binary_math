def binary_decimal(binary_input):
    """
    Binary to decimal converter
    """
    bin_len = len(binary_input) # length of binary input
    bit_list = []
    bits = 1
    
    ##########################################################
    """
    bit count for binary input
    """
    while bin_len != 0:
        bit_list.append(bits)
        bits *= 2
        bin_len -= 1
        
    bit_list.reverse()
    
    ##########################################################
    """
    Binary to decimal conversion
    """
    binary = []
    decimal = []
    decimal_sum = 0 # result of binary to decimal conversion
    
    for num in binary_input:
        binary.append(int(num))
    count = 0
    while count != len(bit_list):
        for x in binary:
            if x != 0:
                decimal.append(bit_list[count])
                count += 1
            else:
                decimal.append(0)
                count += 1
        for dec in decimal:
            decimal_sum += dec
    print(f"Decimal number: {decimal_sum}")    
    
#binary_input = input("Enter binary number: ")
#binary_decimal(binary_input)
