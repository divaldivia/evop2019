#!/usr/bin/env python3

import re	                                            # Import regular expressions

seq_read = open("sequence_data.txt", "r")	            # Open the file
genes = {}	                                          # Create your -empty- dictionary

for line in seq_read:		                              # Read the file line by line
	line = line.rstrip()	                              # Remove "end of line" (\n) from the line
	id,seq = line.split()	                              # Split the line in gene name (id) and its sequence (seq)
	reformatted_seq = re.sub(r"ATG", "-M-", seq)	      # Find the ATG pattern in seq and replace them with "-M-"
	print(id,"\t", reformatted_seq)	                    # Print the gene name and the new sequence

seq_read.close()	                                    # Always close your file
