import os
import hashlib


_default_extensions = [
    '.jpg', '.jpeg', '.png', '.gif', '.ico',
    '.css', '.less', '.sass',
    '.js',
    '.eot', '.svg', '.ttf', '.woff',
]


def generate_hash(directory, extensions=None):
    extensions = extensions or _default_extensions
    md5 = hashlib.md5()

    for curdir, subdirs, files in os.walk(directory):
        # we can ignore subdirs as the contents shows up later from os.walk
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    break
            else:
                continue
            filepath = os.path.join(curdir, filename)
            with open(filepath, 'rb') as f:
                while True:
                    data = f.read(8192)
                    if not data:
                        break
                    md5.update(data)

    return md5.hexdigest()