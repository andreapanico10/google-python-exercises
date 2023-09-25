#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(dir):
  
  filenames = os.listdir(dir)
  file_absolute_paths = [os.path.abspath(filename) for filename in filenames if re.search("__\w+__",filename)]
  
  return file_absolute_paths

def copy_to(paths, dir): 
  '''given a list of paths, copies those files into the given directory'''
  if not os.path.exists(dir):
    os.makedirs(dir)

  for path in paths:
    shutil.copy(path, dir)
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    file_special_abs_paths = get_special_paths(dir)
    if todir != '':
      copy_to(file_special_abs_paths, todir)
    if tozip != '':
      try:
        file_to_zip = [f'"{file}"' for file in file_special_abs_paths] 
        cmd = f'zip .-j {tozip} {" ".join(file_to_zip)}'
        print(f'Command I\'m going to do:{cmd}')
        (status, output) = subprocess.getstatusoutput(cmd)

        if status:
          sys.stderr.write(output)
        
        print(output)
      except:
        sys.stderr.write("zip I/O error: No such file or directory")

    if todir == '' and tozip == '':
      print(file_special_abs_paths)

if __name__ == "__main__":
  main()
