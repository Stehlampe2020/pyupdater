#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########
# CONFIG #
##########

# Insert your settings into the below dict:
conf = {
    'ver_url': 'https://raw.githubusercontent.com/Stehlampe2020/pyupdater/main/versions.json',
    'upd_type': 'zip', # others may later get implemented
    'progress': True, # Wether a progress animation should be shown
    'prefer_stable': True # If set to False the version with the highest number will be preferred
                          # regardless of wether it's stable or not
}

# DO NOT EDIT THE FILE PAST THIS LINE!

#############
# PYUPDATER #
#############

import subprocess, sys, json

try:
    import clint
except Exception as e1:
    print(f'{type(e1).__name__}: {e1}')
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'clint'])
    try:
        import clint
    except Exception as e2:
        print(f'{type(e2).__name__}: {e2}')
        sys.exit(-1)



print('Pyupdater isn\'t implemented yet!')
sys.exit(0)