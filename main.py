from scripts.set_kde_os_info import set_kde_os_info
from scripts.set_neofetch import set_neofetch
from config import *
import os, shutil, errno

config_os_path = os.path.join(os.environ['HOME'], '.config')
config_data_path = os.path.join(os.getcwd(), 'data', 'config')
config_backup_path = os.path.join(os.environ['HOME'], '.config-backup')

def voidpunk_linuxer(config_os_path, config_data_path):
    if os.path.exists(config_os_path):
        alert = input('A previous installation has been found, overwrite? [y/n]')
        if alert == 'y' or alert == 'Y':
            pass
        else:
            print('Aborting.')
            return False
    for el in os.listdir(config_data_path):
        shutil.copytree(
            os.path.join(config_data_path, el),
            os.path.join(config_os_path, el),
            dirs_exist_ok=True
        )
    set_kde_os_info(config_os_path, distro, version, website)
    username = input('What is your name?')
    set_neofetch(config_os_path, username, distro)

if __name__ == '__main__':
    voidpunk_linuxer(config_os_path, config_data_path)