import shutil
du = shutil.disk_usage("/")
used = (du.free/du.total)*100
print(used)
if used>80:
    print("Free Disk Space")
else:
    print("Everything is fine")
