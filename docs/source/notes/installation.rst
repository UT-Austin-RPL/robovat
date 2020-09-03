Installation
============


Assets setup
------------

For most of the assets and configs, follow the following instruction:

.. code-block:: bash

                wget ftp://cs.stanford.edu/cs/cvgl/robovat/assets.zip
                wget ftp://cs.stanford.edu/cs/cvgl/robovat/configs.zip
                unzip assets.zip
                unzip configs.zip


Here we have two scripts for you to download YCB object mesh files and
generate urdf of YCB objects. The original robovat contains simplified and limited
number of YCB objects. You can obtain more varieties following the process:

.. code-block:: bash

                python ycb_downloader.py



Then you need to export downloaded files into urdf files for easy
use. The default path for dowload is `assets/sim/ycb`, and then
you will need to run the following command:

.. code-block:: bash

                python tools/export_ycb_urdf.py --input "assets/sim/ycb/*/google_16k/textured.obj" --rgba "1 1 1 1"
                

Virtual environment recommendation
----------------------------------

Pyenv virtualenv is recommended
`https://github.com/pyenv/pyenv-installer` (conda is also good.)

.. code-block:: bash

                curl https://pyenv.run | bash

Then add

.. code-block:: bash

                export PATH="$HOME/.pyenv/bin:$PATH"
                eval "$(pyenv init -)"
                eval "$(pyenv virtualenv-init -)"
      
to your `~/.bashrc`

And follow pyenv instructions to install a python version you want,
and create a virtual environment you want.


Install the package
-------------------

Now you should be able to install the robovat environment. First of
all, install the requirement:

.. code-block:: bash
                
                pip install -r requirements.txt

Then install the package:

.. code-block:: bash
                
                python setup.py install

