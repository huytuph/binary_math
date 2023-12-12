def ipv4_binary(ipv4_input):
    """
    ipv4 to binary converter
    Args:
        ipv4_input (_type_): _description_
    """
    ipv4_list = []
    ipv4_count = 0
    dec = ''
    dot_count = 0

    for x in ipv4_input:
        while ipv4_count != len(ipv4_input):
            if x != '.':           
                dec += str(x)
                ipv4_count += 1
                continue
            elif x == '.':
                ipv4_list.append(dec)
                dec == ''
                continue
    print(ipv4_list)
        


ipv4_input = "192.168.10.1"
ipv4_binary(ipv4_input)
#ipv4_binary(ipv4_input= "192.168.1.1")
