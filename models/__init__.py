#!/usr/bin/python3

"""
This script sets up a FileStorage instance for the application.

It imports the FileStorage class, creates an instance,
saves data, and reloads it.

Usage:
    - Modify models/__init__.py to include the following code snippet.
"""

from models.engine.file_storage import FileStorage

# Create a FileStorage instance for data storage
storage = FileStorage()

# Reload previously saved data
# (specific implementation depends on FileStorage)
storage.reload()
