#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import glob
import sys
import math
import time
#import numpy as np
import random
import string
import os
import re

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ']

year_line = 51
year_zero = 3 # 'D' start counting from zero
number_years = 25

inflation_cell = '$N$20'
cost_cell = '$N$17'
organic_premium = '$N$19'
replanting_cell = '$AA$9'

planted_line = 36
yield_line = 47
			
#=D36*F47*(1-$AA$9*(F51-$D$51)) + E36*E47*(1-$AA$9*(F51-$E$51))

def income_yield_age():
	f1=open("Excel_income_line_yield_age.txt", "w")
	line = ''
	column_count = 0
	cell = {}
	while column_count <= number_years:
		cell[column_count] = ''
		current_column = year_zero + column_count
		column_letter = alphabet[current_column]
		start = '=('
		start_column = year_zero
		while start_column <= current_column:
			x = alphabet[start_column]+str(planted_line)
			start = start+alphabet[start_column]+str(planted_line)+"*"+alphabet[year_zero+current_column-start_column]+str(yield_line)+"*IF("+str(replanting_cell)+"*("+alphabet[current_column]+str(year_line)+"-"+alphabet[start_column]+str(year_line)+")>1,0,1-"+str(replanting_cell)+"*("+alphabet[current_column]+str(year_line)+"-"+alphabet[start_column]+str(year_line)+")) + "
			#=(D36*E47*IF($AA$9*(E51-$D$51)>1, 0, 1-$AA$9*(E51-$D$51)) + E36*$D$47*IF($AA$9*(E51-$E$51)>1, 0, 1-$AA$9*(E51-$E$51)))*$N$17*(1+$N$19)*((1+$N$20)^E$51)
			#=(D36*E47*IF($AA$9*(E51-$D$51)>1, 0, 1-$AA$9*(E51-$D$51)) + E36*$D$47*IF($AA$9*(E51-$E$51)>1, 0, 1-$AA$9*(E51-$E$51)))*$N$17*(1+$N$19)*((1+$N$20)^E$51)
			start_column = start_column + 1
			#line = line.join("*"+str(cost_cell)+"*(1+"+str(organic_premium)+")*((1+"+str(inflation_cell)+")^"+str(column_letter)+"$"+str(year_line)+")\t")
		start = start[:len(start)-3]+")"
		end = "*"+str(cost_cell)+"*(1+"+str(organic_premium)+")*((1+"+str(inflation_cell)+")^"+str(column_letter)+"$"+str(year_line)+")\t"
		cell[column_count] = ''.join(start+end)
		print (cell[column_count])
		print (column_count)
		column_count = column_count + 1
		#=(D36*$D$47*IF($AA$9*(D51-$D$51)>1, 0, 1-$AA$9*(D51-$D$51)))
		f1.write(start+end)
	f1.close()
	
income_yield_age()

#print "\n%d Sequences containing %d codons were analysed\n%d Sequences excluded (details in *_excluded_sequences.txt)" %(sequence_count, total_codons, bad_sequence_count)
#symbols = {'Ala': 'A', 'Cys' : 'C', 'Asp' : 'D', 'Glu':'E', 'Phe':'F', 'Gly':'G', 'His': 'H', 'Ile': 'I', 'Lys':'K'}