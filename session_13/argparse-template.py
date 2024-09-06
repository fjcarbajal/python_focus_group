#!/usr/bin/env python3

import argparse

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Description of program')

# Required argument(s)
parser.add_argument('--required_argument', required=True, type=str,
    metavar='<str>', help='Description of the argument')
    
# Optional argument(s)
parser.add_argument('--optional_argument', required=False, type=int, default = 5,
    metavar='<int>', help='Some optional argument that uses the default value [%(default)i]')
	
# Switch(es)
parser.add_argument('--switch1', action="store_true",
   help='An argparse switch that stores the value "True"')
   
# Finalization of argparse
arg = parser.parse_args()