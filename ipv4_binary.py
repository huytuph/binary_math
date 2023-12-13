ipv4 = '192.168.1.1'
no_dot = []
count = 0
if '.' in ipv4:
    no_dot = ipv4.replace('.',' ')
    count += 1
    pass
dec_list = no_dot.split()

print(dec_list)