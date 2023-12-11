def bits_list(usr_in):
    """
    bit count for binary input 
    """
    bin_len = len(usr_in)
    bits_num = []
    bits = 1
    while bin_len != 0:
        bits_num.append(bits)
        bits *= 2
        bin_len -= 1
    bits_num.reverse()
    print(bits_num)

usr_in = input("Enter binary number: ")
#bits_list(usr_in)