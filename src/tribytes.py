#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# tribytes.py
# -----------
# Reads a file and check how many instances in the file there is
# of the pattern of three equal bytes with one byte between the
# two first. Very specific.
#
#
# Author: Joachim Strömbergson
# Copyright (c) 2014, Secworks Sweden AB
#
# Redistribution and use in source and binary forms, with or
# without modification, are permitted provided that the following
# conditions are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys
import os


#-------------------------------------------------------------------
# Defines
#-------------------------------------------------------------------
VERBOSE = False
PRINT_PATTERNS = True


#-------------------------------------------------------------------
# main()
#
# Parse any arguments and run the tests.
#-------------------------------------------------------------------
def main():
    file_name = sys.argv[1]

    with open(file_name, 'rb') as my_file:
        byte_array = [0x00] * 4
        curr_byte = my_file.read(1)
        found_patterns = 0
        total_bytes = 0

        while curr_byte:
            if VERBOSE:
                print(byte_array)
            total_bytes += 1
            if ((byte_array[0] != byte_array[1]) and
                (byte_array[0] == byte_array[2]) and
                (byte_array[0] == byte_array[3])):
                found_patterns += 1

#                if PRINT_PATTERNS:
#                    print("Found: [0x%02x, 0x%02x, 0x%02x, 0x%02x]" %
#                          int(byte_array[0]), int(byte_array[1]),
#                          int(byte_array[2]), int(byte_array[3]))

            curr_byte = my_file.read(1)
            byte_array = byte_array[1 : 4] + [curr_byte]

    print("Analyzed file: %s" % (file_name))
    print("Total number of bytes: %d" % (total_bytes))
    print("Number of patterns:    %d" % (found_patterns))
    print("Frequency in file:     %f" % (float(found_patterns) / total_bytes))


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())


#=======================================================================
# EOF eqbytes.py
#=======================================================================
