class Device:
    def __init__(self, name):
        self.name = name
        self.connections = []

class Network:
    def __init__(self):
        self.devices = {}

    def add_device(self, device):
        self.devices[device.name] = device

    def add_connection(self, device1, device2):
        self.devices[device1].connections.append(device2)
        self.devices[device2].connections.append(device1)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.devices:
            return None
        for device in self.devices[start].connections:
            if device not in path:
                new_path = self.find_path(device, end, path)
                if new_path:
                    return new_path
        return None

network = Network()

# def print_req():
#     print("1.Add computer")
#     print("2.ADD repeaters")
#     print("3.Add connection")
#     print("4.Find path")
#     print("5.Exit")
#     a = int(input("Enter the option: "))
#     return a

flag = True

while flag == True:
    command = input()
    if "ADD" in command:
        val = 1
    elif "CONNECT" in command:
        val = 2
    elif "INFO_ROUTE" in command:
        val = 3
    elif "SET_DEVICE_STRENGTH" in command:
        val = 4
    else:
        print("Error: Invalid command syntax.")

    if val == 1:
        # name = input("Enter the name:")
        name = command.replace('ADD ', '')
        if name == "":
            print("Error: Invalid command syntax.")
        else:
            device1 = Device(name)
            network.add_device(device1)
            print("Successfully added ", name, "!")
    elif val == 2:
        # dev1 = input("Enter the name of the device 1:")
        # dev2 = input("Enter the name of the device 2:")
        ls = command.replace("CONNECT ", '').split()
        if len(ls) == 2:

            a,b = ls[0],ls[1]

            a,b  = Device(a), Device(b)
            network.add_connection(a.name, b.name)
            print("Successfully connected")
        else:
            print("Error: Invalid command syntax.")

    elif val == 3:
        # dev1 = input("Enter the name of the device 1:")
        # dev2 = input("Enter the name of the device 2:")
        ls = command.replace("INFO_ROUTE ", '').split()
        if len(ls) == 2:

            a,b = ls[0],ls[1]
            a,b  = Device(a), Device(b)
            print(network.find_path(a.name, b.name))
        else:
            print("Error: Invalid command syntax.")
    else:
        break
    
    



