from typing import Any, Dict, Optional, List

from wildlife_tracker.animal_managment.animal import Animal

class AnimalManager:

    def __init__(self) -> None:
        self.animals: dict[int, Animal] = {}
        


    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass


    def remove_animal(animal_id: int) -> None:
        pass
    
    def register_animal(Animal) -> None:
        pass

  
    def assign_animals_to_habitat(animals: List[Animal]) -> None:
       pass
