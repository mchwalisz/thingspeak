Changelog
=========

`v1.0.0 <https://github.com/mchwalisz/thingspeak/releases/tag/v1.0.0>`_
-----------------------------------------------------------------------

.. warning::

   - `read_key` and `write_key` have been replaced with `api_key`

     The user needs to decide which key should be used. The change is inline with thingspeak API design.

- Upated examples
- Added tests, using `vcrpy <https://vcrpy.readthedocs.io/en/latest/index.html>`_ to store http responses.
- Switched to use `poetry <https://poetry.eustace.io/>`_ for deployment and requirements management


`v0.4.0 <https://github.com/mchwalisz/thingspeak/releases/tag/v0.4.0>`_
-----------------------------------------------------------------------

- Added `thingspeak.get_field()`
- Added examples
- Added timeout option


`v0.3.6 <https://github.com/mchwalisz/thingspeak/releases/tag/v0.3.6>`_
-----------------------------------------------------------------------

- First releases

`v0.1.1 <https://github.com/bergey/thingspeak>`_
------------------------------------------------

- Original version of thingspeak library from @bergey
