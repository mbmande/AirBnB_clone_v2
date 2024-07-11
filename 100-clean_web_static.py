#!/usr/bin/python3
""" ++++++==="""
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']

def do_clean(number=0):
    """
    Delete out-of-date archives and old releases.
    
    Args:
        number (int): The number of archives to keep. Defaults to 0.
                      If 0 or 1, keeps only the most recent archive.
                      If 2, keeps the two most recent archives, and so on.
    """
    number = int(number)
    
    if number < 1:
        number = 1
    
    # Clean local archives
    with lcd("versions"):
        local_archives = sorted(os.listdir("."))
        archives_to_keep = local_archives[-number:]
        
        for archive in local_archives:
            if archive not in archives_to_keep:
                local("rm -f {}".format(archive))
    
    # Clean remote releases
    with cd("/data/web_static/releases"):
        releases = run("ls -tr").split()
        web_static_archives = [r for r in releases if r.startswith("web_static_")]
        releases_to_keep = web_static_archives[-number:]
        
        for release in web_static_archives:
            if release not in releases_to_keep:
                run("rm -rf {}".format(release))
