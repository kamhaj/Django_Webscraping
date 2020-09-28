# Django_Webccraping
Django custom admin methods

## readme file
# recruitment task

#usage >python manage.py downloadpage <url> --shift <shift>
# shift - for Ceasar cypher
example:
python manage.py downloadpage https://www.youtube.com/watch?v=RqymMQUxdpo&ab_channel=Wudoe --shift 5

#usage - > python manage.py countcapitalwords <url_id> --shift 5
example:
python manage.py countcapitalwords 42 --shift 5

#usage - > python manage.py getpopularcapitalwords <N>
# N - number of most popular words we want to get
example:
python manage.py getpopularcapitalwords 10
