Client library for the thingspeak.com API
=========================================

.. image:: https://travis-ci.org/mchwalisz/thingspeak.svg?branch=master
    :target: https://travis-ci.org/mchwalisz/thingspeak
.. image:: https://travis-ci.org/mchwalisz/thingspeak.svg?branch=develop
    :target: https://travis-ci.org/mchwalisz/thingspeak
    :alt: travis develop
    
ThingSpeak is an open source “Internet of Things” application and API to store and retrieve data from things using HTTP over the Internet or via a Local Area Network. With ThingSpeak, you can create sensor logging applications, location tracking applications, and a social network of things with status updates. https://thingspeak.com https://github.com/iobridge/ThingSpeak

This repository is contains Python module that helps in talking to ThingSpeak API.

Full documentation is under http://thingspeak.readthedocs.io/en/latest/

Install using::

    pip install thingspeak

.. warning::

   This is a complete redesign of the library as compared to v0.1.1.
   Previous version is available in https://github.com/bergey/thingspeak
   and is no longer maintained.

   To install old version you can still use::

      pip install thingspeak==0.1.1
