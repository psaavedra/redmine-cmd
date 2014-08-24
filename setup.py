from setuptools import setup, find_packages

version = "0.0.0"

long_description = ""
try:
    long_description=file('README.md').read()
except Exception:
    pass

license = ""
try:
    license=file('LICENSE').read()
except Exception:
    pass


setup(
    name = 'redmine-cmd',
    version = version,
    description = 'redmine-cmd.cfg.example',
    author = 'Pablo Saavedra',
    author_email = 'saavedra.pablo@gmail.com',
    url = 'http://github.com/psaavedra/redmine-cmd',
    packages = find_packages(),
    package_data={
    },
    scripts=[
        "tools/redmine-cmd",
    ],
    zip_safe=False,
    install_requires=[
        "httplib2",
        "simplejson",
    ],
    data_files=[
        ('/usr/share/doc/redmine-cmd/', ['cfg/redmine_cmd.cfg.example']),
    #     ('/etc/init.d', ['init-script'])
    ],

    download_url= 'https://github.com/psaavedra/redmine-cmd/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "python redmine cmd tracker",
)
