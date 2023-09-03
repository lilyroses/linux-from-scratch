import subprocess
import re

results = []


# CHECK BASH
# Check bash version
def check_bash_version():
    minimum_version = '3.2'
    # get first full string of bash version info
    version_info = subprocess.getoutput('bash --version | head -n1 | cut -d " " -f2-4')
    # cut out relevant info (version number)
    current_version = version_info.split()[2][0:6]
    # compare version strings
    if current_version >= minimum_version:
        check = 'OK'
    else:
        check = 'ERROR'
    # save results to formatted string
    result =  f'Bash version: {check} (current {current_version}; min {minimum_version})'
    # results
    results.append(result)


# Check bash symlink
def check_bash_symlink():
    required_symlink = '/usr/bin/bash'
    current_symlink = subprocess.getoutput('readlink -f /bin/sh')
    if current_symlink == required_symlink:
        check = 'OK'
    else:
        check = 'ERROR'
    result = f'Bash symlink: {check} (current {current_symlink}; required {required_symlink})'
    results.append(result)
    

# CHECK BINUTILS VERSION
def check_binutils_version():
    minimum_version = '2.13.1'
    maximum_version = '2.40'
    version_info = subprocess.getoutput('ld --version | head -n1 | cut -d " " -f3-')
    current_version = version_info.split()[4]
    if (current_version >= minimum_version) and (current_version <= maximum_version):
        check = 'OK'
    else:
        check = 'ERROR'
    result = f'Binutils version: {check} (current {current_version}; min {minimum_version}, max {maximum_version})'
    results.append(result)


# CHECK BISON VERSION
def check_bison_version():
    minimum_version = '2.7'


if __name__ == "__main__":
    check_bash_version()
    check_bash_symlink()
    check_binutils_version()
    for result in results:
        print(result)