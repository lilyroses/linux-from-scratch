import subprocess
import re


MINIMUM_VERSIONS = {
    'bash': '3.2',
    'binutils': ['2.13.1', '2.40'],
    'bison': '2.7',
    'coreutils': '6.9',
    'diffutils': '2.8.1',
    'findutils': '4.2.31',
    'gawk': '4.0.1',
    'gcc': ['5.1', '12.2.0'],
    'grep': '2.5.1a',
    'gzip': '1.3.12',
    'linux kernel': '3.2',
    'm4': '1.4.10',
    'make': '4.0',
    'patch': '2.5.4',
    'perl': '5.8.8',
    'python': '3.4',
    'sed': '4.1.5',
    'tar': '1.22',
    'texinfo': '4.7',
    'xz': '5.0.0'
}

SYMLINKS = {
    '/bin/sh': '/usr/bin/bash',
    '/usr/bin/yacc': '/usr/bin/bison',
    '/usr/bin/awk': '/usr/bin/gawk',
}

VERSION_NUMBER_REGEX = r"""\d{1,3}\.\d{1,3}\.{0,1}\d{0,3}"""

current_version_numbers = {}


# find bash version
bash_current_version = subprocess.getoutput('bash --version')
current_version_numbers['bash'] = subprocess.getoutput(
        'bash --version | head -n1 | cut -d " " -f2-4'
    ).split()[2][0:6]

if current_version_numbers['bash'] >= MINIMUM_VERSIONS['bash']:
    print(
        f"\nBash version OK (current: {current_version_numbers['bash']}, \
        minimum: {MINIMUM_VERSIONS['bash']})"
    )
else:
    print(f"\nERROR: Bash version not OK (current: {current_version_numbers['bash']}, minimum: {MINIMUM_VERSIONS['bash']})")
    
# check that /bin/sh points to /usr/bin/bash
bin_sh_symlink = subprocess.getoutput(f'readlink -f /bin/sh')
if bin_sh_symlink == SYMLINKS['/bin/sh']:
    print(f"Bash symlink OK: /bin/sh points to {bin_sh_symlink})")
else:
    print(f"ERROR: /bin/sh does not point to {SYMLINKS['/bin/sh']} (points to {bin_sh_symlink})")
    
  
# binutils version
current_version_numbers['binutils'] = subprocess.getoutput('echo -n "Binutils: "; ld --version | head -n1 | cut -d " " -f3-').split()[5]

if MINIMUM_VERSIONS['binutils'][0] <= (current_version_numbers['binutils']) and (current_version_numbers['binutils'] <= MINIMUM_VERSIONS['binutils'][1]):
    print(f"\nBinutils version OK (current: {current_version_numbers['binutils']}, minimum: {MINIMUM_VERSIONS['binutils'][0]}, maximum: {MINIMUM_VERSIONS['binutils'][1]})")
else:
    print(f"\nERROR: Binutils version not OK (current: {current_version_numbers['binutils']}, minimum: {MINIMUM_VERSIONS['binutils'][0]}, maximum: {MINIMUM_VERSIONS['binutils'][1]}")
    

# check bison version
current_version_numbers['bison'] = subprocess.getoutput('bison --version | head -n1').split()[3]
if MINIMUM_VERSIONS['bison'] <= current_version_numbers['bison']:
    print(f"\nBison version OK (current: {current_version_numbers['bison']}, minimum: {MINIMUM_VERSIONS['bison']})")
else:
    print(f"\nERROR: Bison version not OK (current: {current_version_numbers['bison']}, minimum: {MINIMUM_VERSIONS['bison']})")


# check yacc version
try:
    current_version_numbers['yacc'] = subprocess.getoutput(
        '/usr/bin/yacc --version'
    )
except IndexError:
    print("\nERROR: Yacc not found")
else:
    print(f"\nYacc found ({current_version_numbers['yacc']})")
# check yacc symlink
yacc_symlink = subprocess.getoutput('readlink -f /usr/bin/yacc')
if SYMLINKS['/usr/bin/yacc'] in yacc_symlink:
    print(f"Yacc symlink OK ({yacc_symlink})")
else:
    print(f"ERROR: Yacc symlink fail ({yacc_symlink}), should point to {SYMLINKS['/usr/bin/yacc']}")
    

# coreutils version
current_version_numbers['coreutils'] = subprocess.getoutput('chown --version | head -n1 | cut -d ")" -f2')
if MINIMUM_VERSIONS['coreutils'] <= current_version_numbers['coreutils']:
    print(f"\nCoreutils version OK (current: {current_version_numbers['coreutils']}, minimum: {MINIMUM_VERSIONS['coreutils']})")
else:
    print(f"\nERROR: Coreutils version not OK (current: {current_version_numbers['coreutils']}, minimum: {MINIMUM_VERSIONS['coreutils']})")