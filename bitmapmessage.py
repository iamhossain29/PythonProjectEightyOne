import sys


bitmap = """
....................................................................
**************   *   ***  **  *  ******************************
*********************  **  **  *  *  ****************************** *
**  *****************  ******************************
************* ** * **** ** ************** *
********* ******* **************** * *
******** *************************** *
* * **** *** *************** ****** ** *
**** * *************** *** *** *
****** ************* ** ** *
******** ************* * ** ***
******** ******** * *** ****
********* ****** * **** ** * **
********* ****** * * *** * *
****** ***** ** ***** *
***** **** * ********
***** **** *********
**** ** ******* *
*** * *
** * *
...................................................................."""

print('Bitmap Message')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    #print()

######################################################################################################

# 1. What happens if the player enters a blank string for the message? it will still run the program
# 2. Does it matter what the nonspace characters are in the bitmap variable’s string? yes, it matters. we are splitting this string using space
# 3. What does the i variable created on line 45 represent? It represents the character to print
# 4. What bug happens if you delete or comment out print() on line 52? it will print everything in one line
