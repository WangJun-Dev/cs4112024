from typing import Any, Dict, Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_management.migration_path import MigrationPath

class Migration:
    def __init__(self, migration_id: int, migration_path: MigrationPath, start_date: str, current_date: str, current_location: str, status: str = "Scheduled",) -> None:
        self.migration_id: int = migration_id
        self.migration_path: MigrationPath = migration_path
        self.start_date: str = start_date
        self.status: str = status
        self.current_date: str = current_date
        self.current_location: str = current_location
        
        
    def get_migration_details(self, migration_id: int) -> dict[str, Any]:

        pass
    
    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:

        pass
