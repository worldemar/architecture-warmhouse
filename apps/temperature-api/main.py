from fastapi import FastAPI
import time
import random

app = FastAPI()

class SensorInstallations:
    def __init__(self):
        self._sensor_ids = [0, 1, 2, 3]
        self._locations = ["Unknown", "Living Room", "Bedroom", "Kitchen"]
    def get_sensor_id(self, location):
        _location = location if location in self._locations else self._locations[0]
        return self._sensor_ids[self._locations.index(_location)]
    def get_location(self, sensor_id):
        _sensor_id = sensor_id if sensor_id in self._sensor_ids else 0
        return self._locations[self._sensor_ids.index(_sensor_id)]

sensor_installations = SensorInstallations()

def generate_temperature_data(location: str, sensor_id: int):
    if location is None:
        _sensor_id = sensor_id
        _location = sensor_installations.get_location(_sensor_id)
    if sensor_id is None:
        _sensor_id = sensor_installations.get_sensor_id(location)
        _location = location
    return {
        "value": random.uniform(18, 30),
        "unit": "°C",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "location": _location,
        "status": "active",
        "sensor_id": f"{_sensor_id}",
        "sensor_type": "temperature}",
        "description": f"Temperature sensor in {_location}"
    }
 

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/temperature")
async def get_temperature_by_location(location: str):
    return generate_temperature_data(location, None)

@app.get("/temperature/{sensor_id}")
async def get_temperature_by_id(sensor_id: int):
    return generate_temperature_data(None, sensor_id)
