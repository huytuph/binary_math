def ipv4_binary(ipv4_input):
    """
    ipv4 to binary converter
    Args:
        ipv4_input (_type_): _description_
    """
    ipv4_list = []
    dec1 = ''
    dec2 = ''
    dec3 = ''
    dec4 = ''
    
    for dec in ipv4_input:
        ipv4_list.append(dec)
    
    
    print(ipv4_list)
        


#ipv4_input = input("Enter ipv4 address: ")

ipv4_binary(ipv4_input= "192.168.1.1")