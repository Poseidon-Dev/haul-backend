
class GPSUnitOld:

    def __init__(self, title, type, props):
        self.title = title
        self.type = type
        self.props = props

class GPSUnit:

    def __init__(
        self,
        account_id,
        device_id,
        unit_id,
        device_label,
        driver_id,
        engine_hours,
        engine_odometer,
        last_message_time,
        make,
        model,
        year,
        vin,
        latitude,
        longitude,
        unit_time,
        ignition_status='off',
        heading=0,
        speed=0,
        device_groups=None,
    ):
        self.account_id = account_id
        self.device_id = device_id
        self.unit_id = unit_id
        self.device_groups = device_groups
        self.device_label = device_label
        self.driver_id = driver_id
        self.engine_hours = engine_hours
        self.engine_odometer = engine_odometer
        self.last_message_time = last_message_time
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.latitude = latitude
        self.longitud = longitude
        self.ignition_status = ignition_status
        self.unit_time = unit_time
        self.heading = heading
        self.speed = speed

    def __str__(self):
        return str(self.device_id)
        
    def __repr__(self):
        return f'{self.device_id}: {self.device_label}'