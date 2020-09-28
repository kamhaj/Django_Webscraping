from django.core.management.base import BaseCommand, CommandError
from actions.models import URLContent
from bs4 import BeautifulSoup
import requests


#hardcoded for testing purposes only
html_doc = "ala ma kota a kot ma Alę"

class Command(BaseCommand):
    def add_arguments(self, parser):   #parser is inbuilt
        parser.add_argument('url', type=str, help='URL to download from')
        parser.add_argument('--shift', default="0", type=int, help="The encryption shift value")


    def handle(self, *args, **options):
        help = 'The help for downloadpage command'
        self.stdout.write(f'Name and Surname: ... ')
        url_text = webscrape(options['url'])
        encrypted_msg = caesar_cipher_encrypt(plain_text=url_text, shift=options['shift'])

        #check if url already exist in DB, if yes - overwrite (same ID)
        if URLContent.objects.filter(url_address= options['url']):
            #try except preferable here //TODO
            p = URLContent.objects.filter(url_address=options['url']).update(encrypted_content=encrypted_msg)
            #self.stdout.write(f'PageID: {p.id}')
            self.stdout.write('Downloaded and encrypted again.')
        else:
            #try except preferable here //TODO
            p = URLContent(url_address=options['url'], encrypted_content=encrypted_msg)
            p.save()
            #self.stdout.write(f'PageID: {p.id}')
            self.stdout.write('Downloaded and encrypted.')


#does it make a difference whether a page is not secured? check on that --> yes, error code 404
def webscrape(url):
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content, features="html.parser")   #can use differenet parser, they have unique traits (e.g. some are faster)
    #soup = BeautifulSoup(html_doc, features="html.parser")
    if r.status_code != 200:
        raise CommandError(f'Something went wrong while trying to reach given URL. Code status {r.status_code}')
    return soup.get_text()


def caesar_cipher_encrypt(plain_text, shift):
    result = ""
    # transverse the plain text
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char == ' ':
            result += ' '
        elif char.upper() in ['Ą', 'Ć', 'Ę', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']:
            result += char
        else:
            # Encrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr( (ord(char) + shift-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr( (ord(char) + shift-97) % 26 + 97)
    return result

''' # poprawic '''
def caesar_cipher_decrypt(encrypted_text, shift):
    result = ""
    # transverse the plain text
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char == ' ':
            result += ' '
        elif char.upper() in ['Ą', 'Ć', 'Ę', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']:
            result += char
        else:
            # Decrypt uppercase characters in plain text
            if (char.isupper()):
                result += chr( (ord(char) - shift-65) % 26 + 65)
            # Decrypt lowercase characters in plain text
            else:
                result += chr( (ord(char) - shift-97) % 26 + 97)
    return result