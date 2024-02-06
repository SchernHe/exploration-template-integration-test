from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]
"""Root path of this project"""

DATA_ROOT_DIR = PROJECT_ROOT / "data"
"""Parent directory for all data artifacts"""

RAW_DATA_FILE = DATA_ROOT_DIR / "raw/AmesHousing.csv"
"""Path to the raw data file"""
