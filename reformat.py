###--- FUNCTIONS ---###
import re


###--- GLOBAL ---###
class font_styles:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


###--- FUNCTIONS ---###
def break_into_paragraphs():
    '''
     splits text of 5k words into sentences,
     then creates paragraphs of 3 sentences each,
     and saves result to new document
    '''
    global font_styles

    # read text file
    text = open('5k_words_in_1_paragraph.txt', 'r+')

    text_reader = text.read()

    # reformat into paragraphs of 4 sentences each
    with open('reformatted_into_paragraphs.txt', 'w+') as reformatted:
        # using regex to split text anytime there is a whitespace followed by a Capital letter
        # which certainly means "start of sentence"
        sentences_as_list = re.split(
            r'[ ](?=[A-Z])', text_reader)

        split = [sentence.lstrip().center(100, '~')
                 for sentence in sentences_as_list]

        paragraph = '\n\n'.join('\n'.join(
            j.title() for j in split[i:i+4]) for i in range(0, len(split), 4))

        # BOLD in terminal
        # paragraph = font_styles.BOLD + '\n\n'.join('\n'.join(
        #     split[i:i+4]) for i in range(0, len(split), 4)) + font_styles.END

        reformatted.write(paragraph)

        reformatted.close()


###--- DRIVER CODE ---###
if __name__ == '__main__':
    break_into_paragraphs()
