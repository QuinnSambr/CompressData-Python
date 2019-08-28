"""This Script is Used to Compress Zip ,
Compress and Delete Large Log Files Within A Range Of"""

import zipfile
import os , glob 
import datetime as dt
import os.path, time
import pandas as pd #pip install pandas

# Start Date Specifies the Date in which the range starts from.
start_date = dt.datetime.now() - dt.timedelta(days=60)  
start_date.strftime("%Y-%m-%d") # Formats the Date 
# FileMonthPrev Specifies the Date in which the range must end.
fileMonthPrev = dt.datetime.now() - dt.timedelta(days=30) 
# pd_range Spceifies the Range of Dates
pd_range = (pd.date_range(start_date, fileMonthPrev).strftime("%Y-%m-%d"))
pd = (str(pd_range))
try:
    for name in glob.glob("*.log"): #*.log specifies the file extension ( Can Change to .txt , .exe , .zip etc)
        for i in range (len(pd_range)):
            if str(pd_range[i]) in name:
                #The zipfile.ZiplFile is where you specify the path and the file name format. 
                zip_name = zipfile.ZipFile("\usr\local\fokuson\appserver\server\fokuson\log\localhost_access_log."+str(pd_range[i])+".zip", "w") #Convert to Zip 
                zip_name.write("localhost_access_log."+str(pd_range[i])+".log", compress_type=zipfile.ZIP_DEFLATED) #file to be converted
                os.remove("localhost_access_log."+str(pd_range[i])+".log") # Delete Initial File
                zip_name.close() 
except: 
    print("It Died :(")  
