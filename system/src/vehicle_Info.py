
class VehicleInfo:

    def __init__(self, plate="", is_stolen=False, fines=0, itv="", brand=""):
        self._plate = plate                 # string
        self._is_stolen = is_stolen         # True / False
        self._fines = fines                 # Int
        self._itv = itv                     # fecha
        self._brand = brand                 # String

    def __str__(self):
        return (
            f"Plate: {self._plate}\n"
            f"Stolen: {'Yes' if self._is_stolen else 'No'}\n"
            f"Fines: {self._fines}\n"
            f"ITV: {self._itv}\n"
            f"Brand: {self._brand}"
        )