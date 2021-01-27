###--- FUNCTIONS ---###
def break_into_paragraphs():
    '''
     splits text of 5k words into sentences,
     then creates paragraphs of 3 sentences each,
     and saves result to new document
    '''
    # read text file
    text = open('5k_words_in_1_paragraph.txt', 'r+')

    text_reader = text.read()

    # reformat into paragraphs of 4 sentences each
    # currently missing sentences that end in "!" or "?" etc.
    with open('reformatted_into_paragraphs.txt', 'w+') as reformatted:

        reformatted.write(
            '.\n\n'.join('.'.join(text_reader.split('.')[
                i:i+4]).lstrip() for i in range(0, len(text_reader.split('.')), 4)))

        reformatted.close()


###--- DRIVER CODE ---###
if __name__ == '__main__':
    break_into_paragraphs()
