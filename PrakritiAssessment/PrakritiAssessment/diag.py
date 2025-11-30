import os
import pprint
from cffi import FFI

print("--- DIAGNOSTIC SCRIPT RUNNING ---")

# 1. Print the PATH environment variable as Python sees it
print("\n[1] Current System PATH variable:")
try:
    path_variable = os.environ.get('PATH', 'PATH variable not found!')
    # Print each path on a new line for readability
    pprint.pprint(path_variable.split(os.pathsep))
except Exception as e:
    print(f"Could not read PATH variable. Error: {e}")

# 2. Check if the required directory is in the PATH
print("\n[2] Checking for MSYS2 directory in PATH...")
msys_path = r'D:\msys64\ucrt64\bin'
if 'path_variable' in locals() and msys_path in path_variable:
    print(f"SUCCESS: Found '{msys_path}' in PATH.")
else:
    print(f"FAILURE: Did NOT find '{msys_path}' in PATH.")

# 3. Attempt to load the library directly
print("\n[3] Attempting to load the DLL directly...")
ffi = FFI()
try:
    # This is what WeasyPrint tries to do internally
    lib = ffi.dlopen('libgobject-2.0-0.dll')
    print("SUCCESS: The library 'libgobject-2.0-0.dll' was loaded successfully!")
    print("This means the PATH is working and the issue may be with WeasyPrint itself.")
except Exception as e:
    print("FAILURE: Failed to load the library.")
    print(f"Error details: {e}")

print("\n--- DIAGNOSTIC SCRIPT FINISHED ---")