from setuptools import setup

setup(
    name='git-annex-remote-dbx',
    version='1.0.2',
    author_email='montag451@laposte.net',
    maintainer='montag451',
    maintainer_email='montag451@laposte.net',
    url='https://github.com/montag451/git-annex-remote-dbx',
    description='git-annex special remote for Dropbox',
    long_description=open('README.rst').read(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'annexremote',
        'dropbox',
        'humanfriendly'
    ],
    scripts=['git-annex-remote-dbx']
)
