import zipfile
import os 
import datetime as dt
import os.path, time

fileMonthPrev = dt.datetime.now() - dt.timedelta(days=30)
fileMonthFormat =fileMonthPrev.strftime("%Y.%m.%d")
fileCreated =dt.datetime.fromtimestamp(os.path.getctime("C:/Users/Quinn-Laptop/Documents/python/Compress/localhost_access_log."+fileMonthFormat+".log")) #File Location 
fileMinus = fileCreated - dt.timedelta(days=30)
fileFormat =fileMinus.strftime("%Y.%m.%d")
if (fileCreated >=  fileMinus):
    zip_name = zipfile.ZipFile("localhost_access_log.2019.06.24.zip", "w") #Convert to Zip 
    zip_name.write("localhost_access_log."+fileFormat+".log", compress_type=zipfile.ZIP_DEFLATED) #file to be converted
    os.remove("localhost_access_log."+fileFormat+".log") # Delete Initial File
    zip_name.close()