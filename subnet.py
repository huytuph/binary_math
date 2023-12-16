""" 
usable host per subnet

"""
subm_in = input("enter subnet mask: ")
subm = subm_in.split('.')
subnet = []
hosts = 1
rhosts = 0
for x in subm:
    subnet.append(int(x))
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
        