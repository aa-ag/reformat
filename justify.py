###--- IMPORTS ---###
from justifytext import justify


###--- GLOBAL VARIABLES ---###
text = open('justify_test.txt', 'r')
width = 20

###--- FROM DOCUMENTATION ---###

print(''.join(justify(text.read(), width)))
