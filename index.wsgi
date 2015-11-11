import sae
from thelibrary import wsgi
  
application = sae.create_wsgi_app(wsgi.application)