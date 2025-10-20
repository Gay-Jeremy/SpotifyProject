from spotify import dataset
lstPaysDevice = {}
for record in dataset :
    country = record["country"]
    deviceType = record["device_type"]
    if country not in lstPaysDevice :
        lstPaysDevice[country] = {deviceType : 1}
    if country in lstPaysDevice and deviceType not in lstPaysDevice[country] :
        lstPaysDevice[country][deviceType] = 1
    if country in lstPaysDevice and deviceType in lstPaysDevice[country] :
        lstPaysDevice[country][deviceType] += 1

for pays, device in lstPaysDevice.items() :
        for dev, val in device.items() :
            maxDevice = max(device.values())
        print(f"Pour le pays {pays} le device le plus utilisé est {dev} ({maxDevice})")


