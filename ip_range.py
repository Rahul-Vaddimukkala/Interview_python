s="255.255.255.250"
ip_addresses_required=int(input("Enter the required no of hosts: "))

l=s.split(".")
count=0

for j in range(0,ip_addresses_required):
    l[3]=int(l[3])+1
    if l[3]>255:
        l[3]=0
        l[2]=int(l[2])+1
    if int(l[2])>255:
        l[2]=0
        l[1]=int(l[1])+1
    if int(l[1])>255:
        l[1]=0
        l[0]=int(l[0])+1
    if int(l[0])>255:
        print("No vaild ip addressess are available after 255.255.255.255")
        break
    print(f"{l[0]}.{l[1]}.{l[2]}.{l[3]}")
    count=count+1
    if count==ip_addresses_required:
        break
