===========
redmine-cmd
===========

A Remote console for Redmine based on REST/API and time-tracking system

Installation
------------

::

  pip install redmine-cmd


Upgrading
---------

::
  
  pip install --upgrade redmine-cmd

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

For example::

  redmine-cmd --loglevel=20 -c ./redmine.cfg

; where `./redmine.cfg` looks like::

  [global]
  threshold=3600
  baseurl=https://redmine.myhost.domain
  sentinel=.
  default_time_entry_activitiy = 8
  # See key in https://redmine.myhost.domain/my/account
  key=5174044140444ffee5dd17922228d882166666b5
  session_file=.redmine_cmd_.session


Usage of the interactive shell
------------------------------

Available commands::

  EOF               createtask  help          settask  updatetask       viewusers
  change            end         prev          status   viewcurrenttask
  changetaskstatus  endtask     previoustask  tasks    viewtasks      
  create            exit        set           up       viewtimes 


Configuration file
------------------

See https://github.com/psaavedra/redmine-cmd/blob/master/cfg/redmine_cmd.cfg.example

Comments
--------

- redmine-cmd requires the Web Services activation in Redmine
