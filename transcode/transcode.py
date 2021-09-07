#!/usr/bin/python3

import os
import shutil
import sys

# arg 1: input path
# arg 2: output path

from_root = sys.argv[1]
to_root = sys.argv[2]

def get_files(root):
    files = []
    dirs = [root]
    for (dir_path, dir_names, file_names) in os.walk(dirs.pop()):
        dirs.extend(dir_names)
        files.extend(map(lambda n: os.path.join(*n), zip([dir_path] * len(file_names), file_names)))
    return list(map(lambda p: os.path.relpath(p, root), files))

def path_is_flac(path):
    return path.endswith('.flac')

def get_to_path(from_path):
    if not path_is_flac(from_path):
        return from_path
    
    from_prefix, _ = os.path.splitext(from_path)
    return from_prefix + '.opus'

def paths_match(from_path, to_path):
    return get_to_path(from_path) == to_path

def get_transfer_paths(from_paths, to_paths):
    for from_path in from_paths:
        if get_to_path(from_path) not in to_paths:
            yield from_path

def get_delete_paths(from_paths, to_paths):
    get_to_paths = [ get_to_path(f) for f in from_paths ]
    for to_path in to_paths:
        if to_path not in get_to_paths:
            yield to_path

def transfer(path, from_root, to_root):
    from_path = os.path.join(from_root, path)
    to_path = os.path.join(to_root, get_to_path(path))
    os.makedirs(os.path.dirname(to_path), exist_ok=True)
    
    if path_is_flac(path):
        print(f'Transcoding {path}')
        os.system(f'ffmpeg -i "{from_path}" -c:a libopus -b:a 128k -vbr on -compression_level 10 -frame_duration 60 "{to_path}"')
    else:
        print(f'Copying {path}')
        shutil.copyfile(from_path, to_path)

def delete(path, to_root):
    print(f'Deleting {path}')
    full_path = os.path.join(to_root, path)
    os.remove(full_path)

from_paths = get_files(from_root)
to_paths = get_files(to_root)

# If in "from" but not in "to", copy
transfer_paths = list(get_transfer_paths(from_paths, to_paths))
print(f'{len(transfer_paths)} files to transfer.')
for path in transfer_paths:
    transfer(path, from_root, to_root)

# If not in "from" but in "to", delete
delete_paths = list(get_delete_paths(from_paths, to_paths))
print(f'{len(delete_paths)} files to delete.')
for path in delete_paths:
    delete(path, to_root)