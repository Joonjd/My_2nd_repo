import shutil
du = shutil.disk_usage("/")
used = (du.free/du.total)*100
print(f'{used:.2f}')
with open("log.txt", "a") as file:
    if used>80:
        file.write(f'{used:.2f}. ALERT!!!\n')
    else:
        file.write(f'{used:.2f}. FINE!\n')

