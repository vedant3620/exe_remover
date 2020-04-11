import sys
import os

directory = 'C://Users//Vedant//Desktop'
test = os.listdir( directory )
for item in test:
    if item.endswith(".exe"):
        os.remove( os.path.join( directory, item ) )
