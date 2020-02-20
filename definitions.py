"""
This program uses an number of paths and directories to store information that needs to be written and read. This
file is a repository for those locations.
"""

from pathlib import Path
import os

# This sets our root directory as the project directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
root_dir = Path(ROOT_DIR)

# DIRECTORIES
dirs = {
    "logs": root_dir / "logs",  # main dir for log-related files
    "logs_output": root_dir / "logs/output",  # logging subdir for generated logs
    "scraped": root_dir / "scraped",
    "pdfs": root_dir / "scraped/pdfs/"
}

# PATHS
# Many of our filenames are generated dynamically during runtime (eg. downloaded PDFs are in format {docketnum}.pdf,
# however the following are files with static filenames:
paths = {
    "logs_config": dirs["logs"] / "config/logging.yaml",
    "logs_config_test": dirs["logs"] / "config/logging_test.yaml",
    "master_list": dirs["scraped"] / "FinancialDisclosureMasterList.csv"
}