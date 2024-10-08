from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:
    def __init__(self, path_id: int, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        self.path_id: int = path_id
        self.species: str = species
        self.duration: Optional[int] = duration
        self.start_location: Habitat = start_location
        self.destination: Habitat = destination


    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass
    def get_migration_path_details(self, path_id) -> dict:
        pass
    