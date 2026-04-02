"""
Global path configuration module
Automatically detects runtime environment based on current working directory and configures data paths
"""

from pathlib import Path
import os


class GlobalConfig:
    """Global configuration class that automatically configures paths based on runtime environment"""
    
    def __init__(self):
        self.working_dir = Path.cwd().__str__()
        self._setup_paths()
    
    def _setup_paths(self):
        """Setup paths based on working directory"""
        self.data_base_dir = os.environ.get("DATA_BASE_DIR", "./data")
        self.project_base_dir = os.environ.get("PROJECT_BASE_DIR", ".")
    
        self.averitec_data_dir = os.path.join(self.data_base_dir, "AVeriTeC")
        self.hero_data_dir = os.path.join(self.data_base_dir, "HerO", "data_store", "baseline")
        
        self.result_base_dir = os.path.join(self.working_dir, "output")
        os.makedirs(self.result_base_dir, exist_ok=True)


global_config = GlobalConfig()
