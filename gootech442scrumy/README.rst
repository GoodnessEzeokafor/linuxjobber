=====
GOOTECH442SCRUMY
=====
GOOTECH442SCRUMY is an application built while i was an intern at
linuxjobber 2019

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "gootech442scrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'gootech442scrumy',
    ]

2. Include the gootech442scrumy URLconf in your project urls.py like this::

    path('gootech442scrumy/', include('gootech442scrumy.urls')),

3. Run `python manage.py migrate` to create the gootech442scrumy models.

3. Visit http://127.0.0.1:8000/gootech442scrumy/ to use the app.