import os
import shutil

def set_kde_os_info(config_os_path, distro, version, website):
    logo_path = os.path.join(config_os_path, "gfx/voidpunk_logo.png")
    with open(os.path.join(config_os_path, 'kcm-about-distrorc'), 'w') as f:
        f.write('[General]' + '\n')
        f.write(f'Name={distro}' + '\n')
        f.write(f'LogoPath={logo_path}' + '\n')
        f.write(f'Website={website}' + '\n')
        f.write(f'Version={version}' + '\n')
        # f.write('Variant=<todo?>')
    return True

def unset_kde_os_info(config_os_path, config_backup_path):
    if os.path.exists(config_backup_path, 'kcm-about-distrorc'):
        shutil.copytree(
            os.path.join(config_backup_path, 'kcm-about-distrorc'),
            os.path.join(config_os_path, 'kcm-about-distrorc'),
            dirs_exist_ok=True
        )
    else:
        shutil.rmtree(os.path.join(config_os_path, 'kcm-about-distrorc'))
    return True