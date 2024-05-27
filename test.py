from integrations.gps_trackit.endpoints import UnitEndpoint

equipment = UnitEndpoint()

location = equipment.all(device_id=55444)

print(location)