import speedtest
import time
wifi  = speedtest.Speedtest()
print("Wifi Download Speed is ", wifi.download()//10**6, "mbps")
print("Wifi Upload Speed is ", wifi.upload()//10**6, "mbps")
print("Wifi Ping is ", wifi.results.ping , "ms")
print("Wifi Share is ", wifi.results.share())
