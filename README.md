# CodeGate


### DeflateGate Demo

1. clone CodeGate
  > git clone https://github.com/lisagandy/CodeGate.git

2. move to CodeGate project root directory
  > cd CodeGate/
  
2. clone [static](https://github.com/jordangumm/static)
  > git clone https://github.com/jordangumm/static

3. move to django project root directory
  > cd mysite/

2. clone [static](https://github.com/jordangumm/static)
  > git clone https://github.com/jordangumm/static

3. migrate apps
  > python manage.py makemigrations news beta

4. migrate project
  > python manage.py migrate

5. load deflategate data from NYTimes
  > python manage.py load_deflategate_data

6. host locally for testing
  > python manage.py runserver
  
7. load given url in browser!
