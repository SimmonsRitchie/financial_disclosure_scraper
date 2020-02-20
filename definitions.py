"""
This file contains important project variables.
"""

from pathlib import Path
import os

# This sets our root directory as the project directory
ROOT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))  # This is your Project Root

# DIRECTORIES
DIR_LOGS = ROOT_DIR / "logs"  # main dir for log-related files
DIR_LOGS_OUTPUT = DIR_LOGS / "output"
DIR_LOGS_CONFIG = DIR_LOGS / "config"
DIR_DATA = ROOT_DIR / "data"
DIR_DATA_PDFS = DIR_DATA / "pdfs"

# PATHS
PATH_LOGS_CONFIG = DIR_LOGS_CONFIG / "logging.yaml"
PATH_LOGS_CONFIG_TEST = DIR_LOGS_CONFIG / "logging_test.yaml"
PATH_MASTER_LIST = DIR_DATA / "FinancialDisclosureMasterList.csv"
