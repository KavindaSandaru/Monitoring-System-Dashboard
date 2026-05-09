server_name = input("Enter server name: ")

cpu = int(input("Enter CPU usage (%): "))
ram = int(input("Enter RAM usage (%): "))
disk = int(input("Enter Disk usage (%): "))

status = "HEALTHY"

if cpu >= 90 or ram >= 90 or disk >= 90:
    status = "CRITICAL"

elif cpu >= 70 or ram >= 70 or disk >= 70:
    status = "WARNING"

print("\nSYSTEM STATUS")
print("-------------")
print("Server:", server_name)
print("CPU:", str(cpu) + "%")
print("RAM:", str(ram) + "%")
print("DISK:", str(disk) + "%")
print("STATUS:", status)