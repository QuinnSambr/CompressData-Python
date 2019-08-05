import zipfile
import os 
import datetime as dt
import os.path, time
import pandas as pd #pip install pandas

fileMonthPrev = dt.datetime.now() - dt.timedelta(days=30)
fileMonthFormat =fileMonthPrev.strftime("%Y.%m.%d")
start_date = dt.datetime.now() - dt.timedelta(days=120)
start_date.strftime("%Y.%m.%d")
end_date = fileMonthPrev - dt.timedelta(days=30)
end_date.strftime("%Y.%m.%d")
try: 
    while end_date == fileFormat :
        pd_range = pd.date_range(start_date, end_date)
        pd_range.strftime("%Y.%m.%d")
        fileCreated =dt.datetime.fromtimestamp(os.path.getctime("C:/Users/Quinn-Laptop/Documents/python/Compress/localhost_access_log."+pd_range+".log")) #File Location 
        fileMinus = fileCreated - dt.timedelta(days=30)
        fileFormat =fileMinus.strftime("%Y.%m.%d")
        if (fileCreated >=  fileMinus):
            zip_name = zipfile.ZipFile("localhost_access_log."+pd_range+".zip", "w") #Convert to Zip 
            zip_name.write("localhost_access_log."+pd_range+".log", compress_type=zipfile.ZIP_DEFLATED) #file to be converted
            os.remove("localhost_access_log."+pd_range+".log") # Delete Initial File
            zip_name.close()
            print("File Successfully Compressed")

except: 
    print("File is Not One(1) Month Old \n or")
    print("File Location Cannot Be Found")
