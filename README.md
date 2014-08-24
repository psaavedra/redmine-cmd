===========
redmine-cmd
===========

A Remote CMD for Redmine based on REST/API

Installation
------------

pip install redmine-cmd


Usage
-----

Usage: redmine-cmd [options]

Options::

  -h, --help            show this help message and exit
  -c CONFFILE, --conffile=CONFFILE
                        Conffile (default: .redmine_cmd.cfg)
  -l LOGFILE, --logfile=LOGFILE
                        Log file (default: /dev/stdout)
  --loglevel=LOGLEVEL   Log level (default: 20)

Usage of the interactive shell
------------------------------

Available commands::

  createtask  exit  settask  updatetask       viewtasks  viewusers
  closetask  endtask     help  status   viewcurrenttask  viewtimes


Configuration file
------------------

See https://github.com/psaavedra/redmine-cmd/blob/master/cfg/redmine_cmd.cfg.example

Comments
--------

- redmine-cmd requires the Web Services activation in Redmine
