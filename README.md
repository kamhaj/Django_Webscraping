# Django_Webscraping
> Django custom admin methods

## Quick start - use commands in CMD/Terminal, where manage.py file is

## 1 - downloadpage function - downloads text from html body based on url provided, encrypts it and saves it in DB
> usage >python manage.py downloadpage <url> --shift <shift>
  shift - for Ceasar cypher
  
example:
```bash
python manage.py downloadpage https://www.youtube.com/watch?v=RqymMQUxdpo&ab_channel=Wudoe --shift 5
```

## 2 - countcapitalwords function - counts capital words from given URL
> usage - > python manage.py countcapitalwords <url_id> --shift <shift>  (further decryption usage possible if needed)
  
example:
```bash
python manage.py countcapitalwords 2 --shift 5
```
