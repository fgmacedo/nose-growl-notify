
NoseGrowlNotify is a `Nose`_ plugin that expose Nose tests results notifications over Growl.

Growl is a project that enables beautiful desktop notifications on `Windows`_, `Linux`_ and `Mac`_.

This project is similar and inspired by `nose-gnome-notify`_.

Install
=======

Install from source::

    $> git clone https://github.com/fgmacedo/nose-growl-notify.git
    $> cd nose-growl-notify
    $> python setup.py install


Basic usage
===========

Enable nosegrowlnotify on running nosetests::

    nosetests --with-nosegrowlnotify


Continuous Testing Driven Development
=====================================

Use with `Bruno Bord's Test Daemon`_ to create an simple environment of continuous testing to Python by rerunning tests every time you change something::

    tdaemon.py --custom-args "--with-nosegrowlnotify"

With this approach, you can freely code and refactor you code, and you'll be notified every time you broke some test, or that all
your tests still green, without leaving your favorite editor.


.. _`Nose`: http://www.somethingaboutorange.com/mrl/projects/nose/0.11.1/

.. _`Windows`: http://www.growlforwindows.com/

.. _`Linux`: http://mattn.github.io/growl-for-linux/

.. _`Mac`: http://growl.info/

.. _`nose-gnome-notify`: http://code.google.com/p/nose-gnome-notify/

.. _`Bruno Bord's Test Daemon`: http://github.com/brunobord/tdaemon
