import sys
import os

directory = os.getcwd()
test = os.listdir( directory )
for item in test:
    if item.endswith(".exe"):
        os.remove( os.path.join( directory, item ) )
for item in test:
    if item.endswith(".o"):
        os.remove( os.path.join( directory, item ) )
