import os
import shutil
from configparser import ConfigParser
from filecmp import dircmp

if os.path.exists("Config.ini"):
    config = ConfigParser()
    config.read("Config.ini")
    source = config["DEFAULT"]["source"]
    destination = config["DEFAULT"]["destination"]
    extension = config["DEFAULT"]["extension"]

else:
    source: str = input("Enter Source Path : ")
    destination: str = input("Enter Destination Path : ")
    extension: str = input("Enter File Format : ")


result = dircmp(source, destination)
var1 = result.left_list
var2 = result.right_list
diff = []

for filename in var2:
    if filename not in var1:
        diff.append(r"{}\{}".format(destination, filename))
print(diff)

if len(diff) != 0:
    for path in diff:
        os.remove(path)

for folders, subfolders, filenames in os.walk(source):
    for filename in filenames:
        if filename.endswith("{}".format(extension)):
            shutil.copy(os.path.join(folders, filename), destination)
