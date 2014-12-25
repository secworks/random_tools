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
        eq_bytes = 0
        sum_bytes = 0
        num_bytes = 0

        while curr_byte:
            if VERBOSE:
                print(byte_array)

            byte_array = byte_array[1 : 4] + [curr_byte]
            sum_bytes += ord(curr_byte)
            num_bytes += 1

            # Equal bytes without preceeding equal byte one step away.
            if ((byte_array[0] != byte_array[2]) and
                (byte_array[2] == byte_array[3])):
                eq_bytes += 1

            # Equal bytes with preceeding equal byte one step away.
            if ((byte_array[0] != byte_array[1]) and
                (byte_array[0] == byte_array[2]) and
                (byte_array[0] == byte_array[3])):
                found_patterns += 1

            curr_byte = my_file.read(1)


    print("Analyzed file: %s" % (file_name))
    print("Total number of bytes: %d" % (num_bytes))
    print("Number of patterns:    %d" % (found_patterns))
    print("Pattern frequency:     %f" % (float(found_patterns) / num_bytes))
    print("Number byte pairs:     %d" % (eq_bytes))
    print("Pair frequency:        %f" % (float(eq_bytes) / num_bytes))
    print("Average byte value:    %f" % (float(sum_bytes / num_bytes)))


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
