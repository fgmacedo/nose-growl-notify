
NoseGrowlNotify is a `Nose`_ plugin that expose Nose tests results notifications over `Growl`_.

Growl is a project that enables beautiful desktop notifications on Windows, Linux and Mac.

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


Advanced usage
==============

Use with `Bruno Bord's Test Daemon`_ to create an simple environment of continuous testing to Python by rerunning tests every time you change something::

    tdaemon.py --custom-args "--with-nosegrowlnotify"


.. _`Nose`: http://www.somethingaboutorange.com/mrl/projects/nose/0.11.1/

.. _`Growl`: http://www.growlforwindows.com/ 

.. _`nose-gnome-notify`: http://code.google.com/p/nose-gnome-notify/

.. _`Bruno Bord's Test Daemon`: http://github.com/brunobord/tdaemon
