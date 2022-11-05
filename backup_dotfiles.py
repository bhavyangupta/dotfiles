#!/usr/bin/python3

import socket
import os
import git

file_list = {"~/.tmux.conf" : "tmux_config",
             "~/.config/i3/config" : "i3_config",
             "~/.bashrc" : "bashrc"
            }
target_directory = os.curdir
hostname = socket.gethostname()
print ("Hostname: {}".format(hostname))
for src in file_list:
    dst = os.path.join(os.curdir, file_list[src])
    print ("Copying: {} to {}".format(src, dst))

repo = git.Repo('.')
print("Repo bare: {}".format(repo.bare))

print("Staging changes.. ")
repo.git.add('.')

commit_msg = "Backup from: {}".format(hostname)
print ("Committing with commit msg: {}".format(commit_msg))
repo.git.commit('-m', commit_msg)



