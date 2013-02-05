"""
fg-ws
-----

fg-ws is a rest client tool for FutureGrid cloud project.

Easy to Setup
``````````````

::

    $ pip install fg-ws 
    $ fg-ws users
     list of users 

Links
`````

* `website <https://github.com/lee212/fg-ws>`_
* `documentation <https://github.com/lee212/fg-ws>`_

"""
from setuptools import Command, setup

setup(
    name='fg-ws',
    version='0.10-dev',
    url='http://github.com/lee212/fg-ws/',
    license=open('LICENSE').read(),
    author='Hyungro Lee',
    author_email='hroelee@gmail.com',
    description='A rest client tool for futuregrid cloud project',
    long_description=__doc__,
    packages=['fg-ws'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts':
            [
             'fg-ws = fg-ws.FGWSApps:list_active_users',
 
)
