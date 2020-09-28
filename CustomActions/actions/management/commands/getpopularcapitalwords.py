from django.core.management.base import BaseCommand, CommandError
from collections import Counter
from actions.models import URLContent

#data_set value is for testing purposes, real plain text value should be taken from our database.
data_set = "Welcome to the world of Geeks " \
           "This portal has been created to provide well written well" \
           "thought and well explained solutions for selected questions " \
           "If you like Geeks for Geeks and would like to contribute " \
           "here is your chance You can write article and mail your article " \
           " to contribute at geeksforgeeks org See your article appearing on " \
           "the Geeks for Geeks main page and help thousands of other Geeks. " \


# Python program to find the k most frequent words
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('N', type=int, help='N most commond words in a text')


    def handle(self, *args, **options):
        help = 'The help for getpopularcapitalwords command'
        self.stdout.write(f'Name and Surname: ... ')

        ''' We have to iterate through all encrypted messages and use the Counter class to find N most common words. 
        Then we can use ceasar decryption to find their true meanings. No need to decrypt the whole text if decryption
        is provided in a right way. Number of appearances already provided (tuples).
        '''
        # URLContent.objects.all() ...

        split_it = data_set.split()

        # Pass the split_it list to instance of Counter class.
        counter = Counter(split_it)

        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = counter.most_common(options['N'])

        #decrypt most_occur with a function before printing it
        print(most_occur)


def most_common_words(string)
    counts=Hash.new(0)
    words=string.downcase.delete('.,!?').split(" ")
    words.each {|k| counts[k]+=1}
    p counts.sort.reverse[0]
end