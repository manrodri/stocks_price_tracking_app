stock price tracking app
=======================

Tool for tracking the price of a list of stocks. This is a cli tool with a menu.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone https://github.com/$USERNAME/stocks_price_tracking_app.git``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Choose an option from the menu. To exit program press CTRL + C.

    $ python3.7 app.py 

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn’t active then use:

::

    $ pipenv run make
