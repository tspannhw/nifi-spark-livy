from pyHS100 import SmartPlug, SmartBulb
#from pprint import pformat as pf
import json
import datetime


plug = SmartPlug("192.168.1.203")

row = { }

emeterdaily = plug.get_emeter_daily(year=2017, month=12)
for k, v in emeterdaily.items():
     row["day%s" % k] = v


emeterdaily = plug.get_emeter_daily(year=2018, month=1)
for k, v in emeterdaily.items():
     row["day%s" % k] = v


emeterdaily = plug.get_emeter_daily(year=2018, month=2)
for k, v in emeterdaily.items():
     row["day%s" % k] = v


hwinfo = plug.hw_info
for k, v in hwinfo.items():
     row["%s" % k] = v


sysinfo = plug.get_sysinfo()
for k, v in sysinfo.items():
     row["%s" % k] = v


timezone = plug.timezone
for k, v in timezone.items():
     row["%s" % k] = v


emetermonthly =  plug.get_emeter_monthly(year=2018)
for k, v in emetermonthly.items():
     row["month%s" % k] = v


realtime = plug.get_emeter_realtime()
for k, v in realtime.items():
     row["%s" % k] = v


row['alias'] = plug.alias
row['time'] =  plug.time.strftime('%m/%d/%Y %H:%M:%S')
row['ledon'] =  plug.led
row['systemtime'] = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
json_string = json.dumps(row)
print(json_string)
