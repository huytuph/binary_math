def ipv4_binary(ipv4_input):
    no_dot = []
    if '.' in ipv4_input:
        no_dot = ipv4_input.replace('.',' ')
    dec_list = no_dot.split()
    return(dec_list)