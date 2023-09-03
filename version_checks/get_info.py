"""Get info from user about packages required to build LFS 12"""
PROGRAM_INFO = {}


def get_info():
    """Get program info from the user."""
    program_name = input('Program name: ')
    program_alias = input('Program alias: ')
    min_version = input('Minimum required version: ')
    max_version = input('Maximum required version: ')
    current_version = ''
    symlinks = []
    program_path = input('Program path: ')
    symlink_to = input('Symlink that program points to: ')
    symlinks.append(program_path, symlink_to)

    PROGRAM_INFO['name'] = program_name
    PROGRAM_INFO['alias'] = program_alias
    PROGRAM_INFO['min_version'] = min_version
    PROGRAM_INFO['max_version'] = max_version
    PROGRAM_INFO['current_version'] = current_version
    PROGRAM_INFO['symlinks'] = symlinks


get_info()
