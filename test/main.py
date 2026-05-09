server_name = "Alpha"
cpu = 92

if cpu >= 90:
    status = "CRITICAL"
elif cpu >= 70:
    status = "WARNING"
else:
    status = "HEALTHY"

print("SYSTEM STATUS")
print("-------------")
print("Server:", server_name)
print("CPU:", str(cpu) + "%")
print("STATUS:", status)