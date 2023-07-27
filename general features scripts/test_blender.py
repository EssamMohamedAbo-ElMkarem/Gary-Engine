import os
from sys import argv
argv = argv[argv.index("--") + 1:]

# format specific options... change as you like
args_fbx = dict(
    # global_scale=1.0,
    )

args_obj = dict(
    # use_image_search=False,
    )

args_3ds = dict(
    # constrain_size=0.0,
    )

import bpy
for f in argv:
    ext = os.path.splitext(f)[1].lower()

    if ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=f, **args_fbx)
    elif ext == ".obj":
        bpy.ops.import_scene.obj(filepath=f, **args_obj)
    elif ext == ".3ds":
        bpy.ops.import_scene.autodesk_3ds(filepath=f, **args_3ds)
    else:
        print("Extension %r is not known!" % ext)
if not argv:
    print("No files passed")