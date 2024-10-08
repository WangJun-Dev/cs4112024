from typing import Optional, List, Dict, Any, self

from wildlife_tracker.habitat_management.habitat import Habitat



class HabitatManager:
    def __init__(self) -> None:
        self.habitats: Dict[int, Habitat] = {}
        
        
  

    def get_habitat_by_id(self, habitat_id: int) -> Habitat:
        pass

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass
    
    def get_habitats_by_type(self, environment_type: str) -> List[Habitat]:
        pass
    
  
    def remove_habitat(self, habitat_id: int) -> None:
        pass

   


    def get_habitats_by_geographic_area(self, geographic_area: str) -> List[Habitat]:
        pass
    

    def get_habitats_by_size(self, size: int) -> List[Habitat]:
        pass

  
   