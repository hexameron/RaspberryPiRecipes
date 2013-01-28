#! /bin/bash

# This is a script that will install Python along with the libraries that are needed by the program

# Download and install Python via the package manager
apt-get install python python-dev

# Download the libraries that you will need
wget http://pypi.python.org/packages/source/s/simplejson/simplejson-3.0.7.tar.gz

# Extract the library 
tar -zxf simplejson-3.0.7.tar.gz

# Change to the directory that we just extracted
cd simplejson-3.0.7

# Install the library so that we can use it in our Python program
python setup.py install

# Print out a success message to the termninal
echo "Success: Python has been installed along with the necessary libraries"  
