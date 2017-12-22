=====================
RestyResolver Example
=====================

Running:

.. code-block:: bash

    $ ./resty.py

Now open your browser and go to http://localhost:9090/v1.0/ui/ to see the Swagger UI.
``bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```