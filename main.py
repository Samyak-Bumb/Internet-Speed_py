# Best # speedtest-cli --simple
# Help # speedtest-cli -h

# import speedtest

# test = speedtest.Speedtest()

# print("Wait Server is Loading")
# test.get_servers()  # Get list of servers

# print("Chosing best fucking Server")
# best = test.get_best_server()  # Choosing best Server

# print(best)


import speedtest
st = speedtest.Speedtest()
wifi = speedtest.Speedtest()

print("Wifi Download Speed is ", wifi.download())
print("Wifi Upload Speed is ", wifi.upload())

servernames = []

st.get_servers(servernames)

print(st.results.ping)
