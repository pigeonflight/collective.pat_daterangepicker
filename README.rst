.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/collective.pat_daterangepicker.svg?branch=master
    :target: https://travis-ci.org/collective/collective.pat_daterangepicker

.. image:: https://coveralls.io/repos/github/collective/collective.pat_daterangepicker/badge.svg?branch=master
    :target: https://coveralls.io/github/collective/collective.pat_daterangepicker?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/collective.pat_daterangepicker.svg
    :target: https://pypi.python.org/pypi/collective.pat_daterangepicker/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.pat_daterangepicker.svg
    :target: https://pypi.python.org/pypi/collective.pat_daterangepicker
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.pat_daterangepicker.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.pat_daterangepicker.svg
    :target: https://pypi.python.org/pypi/collective.pat_daterangepicker/
    :alt: License


==============================
collective.pat_daterangepicker
==============================

This is not working for general use yet!
If you absolutely must use it today...
Then include the daterangepicker by using `add_resource_on_request`
in the python class of your browserview:
::

    from Products.CMFPlone.resources import add_resource_on_request
    ...


    class YourView(BrowserView):
        ...
        def __call__(self):
            add_resource_on_request(self.request, 'app-daterangepicker')

Then in your page template include an input box with a `.pat-daterangepicker` class.

Something like this:
::

         <input class="pat-daterangepicker" value="2020/01/01 - 2020/03/03" />


Features
--------

This provides a bundled daterangepicker (using the package from daterangepicker.com)


