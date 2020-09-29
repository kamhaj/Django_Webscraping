# Django Webscraping
> Django custom admin methods

## Quick start - use commands in CMD/Terminal, where manage.py file is
shift - for Ceasar cypher

#### 1 - downloadpage function - downloads text from html body based on url provided, encrypts it and saves it in DB
>python manage.py downloadpage <url> --shift <shift> 
  
example:
```bash
python manage.py downloadpage https://www.youtube.com/watch?v=RqymMQUxdpo&ab_channel=Wudoe --shift 5
```



#### 2 - countcapitalwords function - counts capital words from given URL
> python manage.py countcapitalwords <url_id> --shift <shift>
  
example:
```bash
python manage.py countcapitalwords 2 --shift 5
```
