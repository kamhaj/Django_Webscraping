# Django Webscraping
> Django custom admin methods

## Quick start - use commands in CMD/Terminal, where manage.py file is
shift - for Ceasar cypher

#### ⋅⋅* downloadpage function - downloads text from html body based on url provided, encrypts it and saves it in DB
>python manage.py downloadpage <url> --shift <shift> 
  
example:
```python
python manage.py downloadpage https://en.wikipedia.org/wiki/Kitten --shift 5
```
--
--

#### ⋅⋅* countcapitalwords function - counts capital words from given URL
> python manage.py countcapitalwords <url_id> --shift <shift>
  
example:
```python
python manage.py countcapitalwords 2 --shift 5
```
