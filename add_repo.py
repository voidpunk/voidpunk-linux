import shutil

def add_repo():
    with open('/etc/pacman.conf', 'r') as f:
        conf = f.readlines()
    if '[xerolinux_repo]' in conf:
        print('Repo already present')
        return True
    backup = shutil.copyfile('/etc/pacman.conf', '/etc/pacman.conf.bak')
    with open('/etc/pacman.conf', 'a') as f:
        f.writeline('[xerolinux_repo]')
        f.writeline('SigLevel = Optional TrustAll')
        f.writeline('Server = https://xerolinux.github.io/$repo/$arch')
    return True, backup
