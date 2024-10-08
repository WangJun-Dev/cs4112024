from typing import Any, Optional, List

from .animal import Animal


class Animal:
 
    def __init__(self, animal_id: int, species: str, health_status: Optional[str] = None, age: Optional[int] = None) -> None:
        self.animal_id: int = animal_id
        self.species: str = species
        
        
        self.age: Optional[int] = age
        
        self.health_status: Optional[str] = health_status
        
    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass

    def get_animal_details(self, animal_id: int) -> dict[str, Any]:
       pass
   
    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
       pass
   