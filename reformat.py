###--- IMPORTS ---###


###--- FUNCTIONS ---###
def break_into_paragraphs():
    '''
     splits text of 5k words into sentences,
     then creates paragraphs of 3 sentences each,
     and saves result to new document
    '''
    # read text file
    text = open('5k_words_in_1_paragraph.txt', 'r')

    tex_reader = text.read()

    for sentence in tex_reader.split('.'):
        print(sentence)


###--- DRIVER CODE ---###
if __name__ == '__main__':
    break_into_paragraphs()
