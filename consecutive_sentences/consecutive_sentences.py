'''
Original Source of Problem: http://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html

Objective:
    Write a program to find all the sentences, or consecutive sequence of sentences, in a text file where:  min <= length <= max.
    Assume that a sentence ends in a period, question mark, or exclamation point.
    In the special case of quoted sentences (that begin with quotes or an apostrophe), include the terminating quote mark or apostrophe.
    Count all blanks and punctuation, but assume only one blank between sentences. (All EOL characters should be converted to blanks).

Conditions:
    Precondition: Min and Max will be positive integers less than 1000, and Min <= Max.
    The name of the text file is to be provided as a command line argument (not read from Standard Input).

Example:
    For example, given this text:
    ''
    Black is white.  Day is night.  Understanding is ignorance.
    Truth is fiction.  Safety is danger.
    ''

    * If min = 15 max = 16 then the output is: ["Black is white."]
    * If min = 17 max = 18 then the output is ["Truth is fiction.","Safety is danger."]
    * If min = 30 and max = 37 then the output is: ["Truth is fiction. Safety is danger."]
    because the two sentences are consecutive sentences with the desired length.

'''

import re
from optparse import OptionParser


def cleanup_text(text):
    '''
        this function normalizes the input text by applying regular expressions to the input text string.
        It substitutes a single space for newlines, tabs, and multiple instances of spaces between sentences.
     '''

    text = re.sub(r'\n|\t', ' ',text) # substitute spaces for new lines, tabs
    text = re.sub(r'\.\s+', '. ',text) # remove multiple spaces between sentences
    text = re.sub(r'^\s+', '',text) # remove space from the beginning of the text
    return text

class SentenceCount:
    def __init__(self,textfile = None):
        ''' expects a full path to the input file to be parsed through '''
        if textfile != None:
            text_array = []
            with open(textfile,'r') as f:
                for line in f:
                    text_array.append(line)
            self.text = ' '.join(text_array)

    def find_sentences(self,min,max):
        ''' '''
        self.text = cleanup_text(self.text)

        '''
        Apply a regular expression to identify sentences ending in .|?|!.
        Use a nongreedy operator to prevent the regexp from considering multiple sentences as a single sentence instance
        Return an array of sentences, each sentence beginning with a non-space character
        '''
        single_sentence_regexp = r'([\s|\S]+?[\.|\!|\?])'
        individual_sentences = re.findall(single_sentence_regexp,self.text)
        individual_sentences = map(lambda sentence: cleanup_text(sentence),individual_sentences)

        '''
        First, look for multisentence groups that satisfy the criteria.
        Sentences must be consecutive, seperated by a single space.
        If this condition is met, return those values
        '''

        multisentence_groups = []
        for sentence_index in range(0,len(individual_sentences)):
            sentence = individual_sentences[sentence_index]
            match = False
            for sentence_index_b in range(sentence_index+1,len(individual_sentences)):
                new_sentence = ' '.join([sentence,individual_sentences[sentence_index_b]])
                if len(list(new_sentence)) >= min and len(list(new_sentence)) <= max:
                    match = True
                    sentence = new_sentence
                else:
                    break

            if match == True:
                multisentence_groups.append(sentence)

        if multisentence_groups != []:
            return multisentence_groups

        '''
        If no multisentence groups were found, look for individual sentences that meet this criteria
        '''
        if individual_sentences:
            single_sentence_matches = []
            for m in filter(lambda sentence: len(list(sentence)) >= min and len(list(sentence)) <= max,individual_sentences):
                single_sentence_matches.append(m)

            return single_sentence_matches


def main():
    usage = "usage: %prog [options] -f TEXT_FILE -n LENGTH_MIN -m LENGTH_MAX"
    parser = OptionParser(usage)

    parser.add_option("-v", "--text_file", dest="text_file", action="store", help="the input text file that contains the strings")
    parser.add_option("-n", "--length_min", dest="length_min", action="store", help="the minimum length in characters for a sentence to be returned")
    parser.add_option("-m", "--length_max", dest="length_max", action="store", help="the maximum length in characters for a sentence to be returned")

    (options, args) = parser.parse_args()

    if options.text_file is None or options.length_min is None or options.length_max is None:
        parser.error("missing a required argument")

    sc = SentenceCount(options.text_file)
    matches = sc.find_sentences(options.length_min,options.length_max)
    for match in matches:
        print "Match: ", match

if __name__ == '__main__':
    main()


