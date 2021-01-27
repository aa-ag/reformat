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
        split = [sentence.lstrip().rjust(100)
                 for sentence in text_reader.split('.')]
        paragraph = '.\n\n'.join('.\n'.join(
            split[i:i+4]) for i in range(0, len(split), 4))

        reformatted.write(paragraph)

        reformatted.close()


###--- DRIVER CODE ---###
if __name__ == '__main__':
    break_into_paragraphs()
