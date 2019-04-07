A git-annex special remote for Dropbox

Installation
============

.. code:: sh

   pip install git-annex-remote-dbx

Configuration
=============

To create a special remote using Dropbox as a backend, you can type
the following command (warning: this is an example, no encryption is
used which is bad):

.. code:: sh

   git annex initremote myremote type=external externaltype=dbx encryption=none prefix=git-annex upload_chunk_size=10MiB

To access your Dropbox, this special remote needs an access
token. When creating the special remote, a browser tab will be opened
for you to connect to your Dropbox and to grant access to this
application.

This special remote accepts several parameters:

- prefix: this is the directory where all your files will be stored
  (default: git-annex)
- upload_chunk_size: to limit his memory usage, this special remote
  does not load all the file in memory before uploading it but instead
  splits the file in chunk and sends these chunks in turn to
  Dropbox. This parameter lets you specify the size to be
  used. Increasing this value will improve the upload speed at the
  expense of the memory usage and the progress report frequency
  (default: 1 MiB)

Notes
=====

This special remote passes all the tests of :code:`git annex
testremote` successfully.
