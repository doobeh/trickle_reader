from trickle import reader
from datetime import date
from datetime import timedelta, time, datetime

store_locations = {
    '001': r'\\10.0.0.229\c$\pcmaster\trickle\arc',
    '003': r'\\10.0.2.220\c$\pcmaster\trickle\archive',
}

dt = date(2014, 9, 23)

results = reader(location=store_locations.get('001'), dt=dt)

def sales(product, time, results=results, shop_time=15):
    origin = (datetime.combine(datetime.today(), time) + timedelta(minutes=shop_time)).time()
    for sale in results:
        if sale["product"] == product:
            if sale["time"] > origin:
                print sale


product = '0004000000627'
sales(product, time(8,0,0), results)
