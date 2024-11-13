import shutil
import os
from datetime import datetime

def backup_folder(source_dir, backup_dir):
    # Check if the backup directory exists, create it if it doesn't
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Generate a unique backup name with a timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    
    # Copy the entire folder
    shutil.copytree(source_dir, backup_path)
    print(f'Backup created at {backup_path}')

if __name__ == "__main__":
    # Replace 'flutter_assignment1' with the actual folder on your Desktop
    source = os.path.expanduser('~/Desktop/css_plp')
    # Set the backup destination to Documents/Backups
    backup = os.path.expanduser('~/Documents/Backups')
    
    backup_folder(source, backup)
