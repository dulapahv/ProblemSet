if __name__ != "assets.library":
    raise RuntimeError("This file must be imported as a module. Please run it from Nekoparaiten.py")

import subprocess
import sys

"""Check for read/write function"""
try:
    import assets.function.read_write as rw
except ImportError:
    raise RuntimeError("Required function 'read_write' is missing!, please re-install the program.")

"""Check for Pillow module"""
try:
    from PIL import ImageTk, Image
except ImportError:
    print("> 'Pillow' module is missing!\n" +
          "Trying to install required module: Pillow")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    print()

"""Check for Firebase module"""
try:
    from firebase_admin import initialize_app, credentials, db
except ImportError:
    print("> 'Firebase' module is missing!\n" +
          "Trying to install required module: Firebase")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "firebase-admin"])
    print()
