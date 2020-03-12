"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Paul Murff
Date: Dec 11 2019
"""

import currency



src = input('3-letter code for original currency: ') 
dst = input('3-letter code for the new currency: ')
amt = float(input('Amount of the original currency: '))

amt_exchanged = currency.exchange(src,dst,amt)

print('You can exchange '+ str(amt) + ' ' + src + ' for '+ str(format(amt_exchanged, '.3f')) + ' ' + dst +'.')