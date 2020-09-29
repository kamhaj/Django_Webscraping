# Django_Webscraping
Django custom admin methods

## 1 - downloadpage function - downloads text from html body based on url provided, encrypts it and saves it in DB

#usage >python manage.py downloadpage <url> --shift <shift>
# shift - for Ceasar cypher
example:
python manage.py downloadpage https://www.youtube.com/watch?v=RqymMQUxdpo&ab_channel=Wudoe --shift 5

## 2 - countcapitalwords function - counts capital words from given URL
#usage - > python manage.py countcapitalwords <url_id> --shift <shift>  (further decryption usage possible if needed)
example:
python manage.py countcapitalwords 2 --shift 5
