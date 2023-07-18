#!/opt/homebrew/bin/python3

subnets = ['10.0.0.0/24','10.0.1.0/24','172.0.0.0/24','192.168.0.0/24','1.1.1.0/24']

created_subnets = {}
def create_subnet(num:int, subnet:str):
    if subnet in created_subnets.values():
        raise ValueError(f"subnet {subnet} has already been created")
    print(f"Created subnet {num}, network {subnet}")
    created_subnets[num] = subnet

for num in range(0, len(subnets)):
    breakpoint()
    create_subnet(num, subnets[num])

