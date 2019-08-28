import zipfile
import os , glob 
import datetime as dt
import os.path, time
import pandas as pd #pip install pandas

fileMonthPrev = dt.datetime.now() - dt.timedelta(days=30)
start_date = dt.datetime.now() - dt.timedelta(days=120)
start_date.strftime("%Y.%m.%d")
end_date = fileMonthPrev - dt.timedelta(days=30)
end_date.strftime("%Y.%m.%d")
pd_range = (pd.date_range(start_date, end_date).strftime("%Y.%m.%d"))
pd = (str(pd_range))

temp=0
try:
    for name in glob.glob("*.log"):
        temp = temp+1
        for i in range (len(pd_range)):
            if str(pd_range[i]) in name: 
                zip_name = zipfile.ZipFile("C:\\Users\Quinn-Laptop\Documents\python\Compress\localhost_access_log."+str(pd_range[i])+".zip", "w") #Convert to Zip 
                zip_name.write("localhost_access_log."+str(pd_range[i])+".log", compress_type=zipfile.ZIP_DEFLATED) #file to be converted
                os.remove("localhost_access_log."+str(pd_range[i])+".log") # Delete Initial File
                zip_name.close() 
except: 
    print("It Died :(")  
