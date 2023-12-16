""" 
usable host per subnet

"""
subm_in = input("enter subnet mask: ") # user input
subm = subm_in.split('.') # octet list w/out '.'
subnet = [] # octet list as int
hosts = 1 # total host available on network
for x in subm:
    subnet.append(int(x)) # add to subnet list as int
for octet in subnet:
    if 255 - octet != 0:
        hosts *= 256
    else:
        continue
        
        
print(subm)
print(f'''
total host: {hosts}
usable hosts: {hosts-2}
''')
        