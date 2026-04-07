from vehicle_Info import VehicleInfo

class VehicleDatabase:

    def __init__(self):
        self._vehicle_info = VehicleInfo()

    def query_vehicle(self, validate_plate):
        # Se Simula la respuesta de uno query a base de datos de la polícía
        self._vehicle_info = VehicleInfo(validate_plate, False, 8, "04-06-1997", "TESLA")
        return self._vehicle_info

