"""
This is a simple script to get an insert statement from a selecct query input
run the script 
    > python from_select_to_insert.py 
    > Paste in stdin the query output and hit cnt+d 

"""

import sys


lines = sys.stdin.readlines()

for line in lines:
    columns = line.split()
    longitud = len(columns) - 1 

    if longitud == 3:
        
    
        for index,column in enumerate(columns):

            if index == 0:
                print(f"(",end='')
            try:
                int(column)
            except ValueError:
                print(f"\"{column}\"",end='')    
                
                if index < longitud:
                    print(f", ",end='')
                else:
                    print(f"), ")
            else:
                print(f"{column}" ,end='')
                if index < longitud:
                    print(f", ",end='')
                else:
                    print(f"), ")