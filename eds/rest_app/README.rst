=====================
RestyResolver Example
=====================

Running:

.. code-block:: bash

    $ python resty.py

Now open your browser and go to http://localhost:9090/eds/ui/ to see the Swagger UI.
``bash
# building the image
docker build -t resty .

# starting up a container
docker run -p 9090:9090 resty
```