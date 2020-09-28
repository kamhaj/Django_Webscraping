from django.core.management.base import BaseCommand, CommandError
from actions.models import URLContent

#data_set value is for testing purposes, real plain text value should be taken from our database.
data_set = '''
           Welcome to the world of Geeks \
           This portal has been created to provide well written well \
           thought and well explained solutions for selected questions \
           If you like Geeks for Geeks and would like to contribute \
           here is your chance You can write article and mail your article \
           to contribute at geeksforgeeks org See your article appearing on\
           the Geeks for Geeks main page and help thousands of other Geeks. \
           '''

class Command(BaseCommand):
    def add_arguments(self, parser):   #parser is inbuilt
        parser.add_argument('url_id', type=int, help='URL ID in a database')
        parser.add_argument('--shift', default="0", help="The encryption shift value")


    def handle(self, *args, **options):
        help = 'The help for countcaptialwords command'
        upperCounter=0
        lowerCounter=0

        self.stdout.write(f'Name and Surname: ... ')

        # get URL by ID, get its encrypted message and count words in it
        #count how many words start with a capital letter
        '''
        we can split the whole text using text.split(" ") method (delimiter is space) and increment counter
        whenever we check that split[i].isUpper() is True. If its false we can increment another counter.
        By adding both counter we can get total number of words and present statistics in a required form.
        (remember to format to 2 decimal places).
        '''
        #content = (URLContent.objects.filter(pk=int(options['url_id'])))['encrypted_content']
        content = data_set.split(' ')
        for word in content:
            if not word:        # for empty words
                continue
            if word[0].isupper():
                upperCounter+=1
            else:
                lowerCounter+=1

        self.stdout.write(f'Uppercase words number is {upperCounter}, lowercase words number is {lowerCounter}')
        self.stdout.write(f'Total number of words is {str(upperCounter+lowerCounter)}')
        self.stdout.write(f'Uppercase/Total words ratio is {str(100*upperCounter/(upperCounter+lowerCounter))}%')
