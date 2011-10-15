.. _compile-time-configuration:

===============================
Initial Configuration of Askbot
===============================

While most configuration settings for askbot can be done at any time :ref:`through the web-interface <run-time-configuration>`, some manipulations on the server are still necessary.


Installing Askbot as a new Django project (standalone app)
==========================================================

When installing Askbot for the first time, you will need to initialize the site setup files by typing::

    askbot-setup

and answering the questions. The `askbot-setup` script will ask you where to deploy Askbot. If you are in
the directory where the Askbot project resides, you can answer `.` (`.` refers to the current directory).
There may be an error message; ignore it.

.. note::

    All Django sites have four project-wide files::

        settings.py - the main settings configuration file
        urls.py     - main url configuration
        __init__.py - often empty but needed for Python
        manage.py   - the hook allowing to run management commands

    `askbot-setup` adds those files to the directory you select (and some more things specific to Askbot).


Note that if you already have a Django site you will not want to use `askbot-setup`, because you don't want to just overwrite your existing settings.py. See below for instructions.

Another thing you have to do if you are creating a brand new Django project is edit the file `settings.py`_. At the very minimum, you will need to provide the correct values to::

    DATABASE_ENGINE = '' #e.g. 'mysql'
    DATABASE_NAME = '' #name of the database you created, e.g. 'askbot'.
    DATABASE_USER = '' #name of the database user, e.g. 'askbotuser'.
    DATABASE_PASSWORD = '' #password to the database
    CSRF_COOKIE_DOMAIN = ''#e.g. 'example.com' or 'askbot.example.com' (localhost/IP address for tests)

All values must be enclosed in single quotes, as shown above.

.. note::

    The files settings.py_ and urls.py_ may also need to be touched up 
    when you upgrate the software, because new versions may bring 
    new dependencies and add new site urls.


Adding Askbot to an existing Django project
===========================================

If you are adding askbot to an existing Django project, you will need to
merge settings.py_ and urls.py_ into your project manually. The templates to be used can be found
in the `askbot/setup_templates` subdirectory.


.. _urls.py: http://github.com/ASKBOT/askbot-devel/blob/master/askbot/setup_templates/urls.py
.. _settings.py: http://github.com/ASKBOT/askbot-devel/blob/master/askbot/setup_templates/settings.py
