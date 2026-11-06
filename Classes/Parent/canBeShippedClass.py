from abc import ABC, abstractmethod

class canBeShippped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass