import struct
import datetime

tdx_dir = "D:/programfiles/gjty/vipdoc/"
dst_dir = "D:/programing/python/stock/tdxdata/"
stock_id = "sh999999"
#stock_id = "sh600519"



def stock_csv(filepath, name):
    data = []
    with open(filepath, 'rb') as f:
        file_object_path = dst_dir + name +'.csv'
        file_object = open(file_object_path, 'w+')
        while True:
            stock_date = f.read(4)
            stock_open = f.read(4)
            stock_high = f.read(4)
            stock_low= f.read(4)
            stock_close = f.read(4)
            stock_amount = f.read(4)
            stock_vol = f.read(4)
            stock_reservation = f.read(4)

            # date,open,high,low,close,amount,vol,reservation

            if not stock_date:
                break
            stock_date = struct.unpack("l", stock_date)     # 4Bytes , 20091229
            stock_open = struct.unpack("l", stock_open)     #open*100
            stock_high = struct.unpack("l", stock_high)     #high*100
            stock_low= struct.unpack("l", stock_low)        #low*100
            stock_close = struct.unpack("l", stock_close)   #close*100
            stock_amount = struct.unpack("f", stock_amount) #turn vol
            stock_vol = struct.unpack("l", stock_vol)       #vol
            stock_reservation = struct.unpack("l", stock_reservation) #reserv

            date_format = datetime.datetime.strptime(str(stock_date[0]),'%Y%M%d') # format date
            list= date_format.strftime('%Y-%M-%d')+","+str(stock_open[0]/100.0)+","+str(stock_high[0]/100.0)+","+str(stock_low[0]/100.0)+","+str(stock_close[0]/100.0)+","+str(stock_vol[0])+","+str(stock_reservation)+"\r\n"
            file_object.writelines(list)
        file_object.close()

path = tdx_dir + stock_id[0:2] + "/lday/" + stock_id + ".day"

stock_csv(path, stock_id)






