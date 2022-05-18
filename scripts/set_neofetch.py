import os
import shutil

def set_neofetch(config_os_path, username, distro):
    if not os.path.exists(os.path.join(config_os_path, 'neofetch')):
        return False
    with open(os.path.join(config_os_path, 'neofetch/voidpunk.conf'), 'a') as f:
        f.write(f'\n\nusername={username}')
        f.write(f'\ndistro={distro}')
    return True

def unset_neofetch(config_os_path, config_backup_path):
    shutil.copytree(
        os.path.join(config_backup_path, 'neofetch'),
        os.path.join(config_os_path, 'neofetch'),
        dirs_exist_ok=True
    )
    return True
