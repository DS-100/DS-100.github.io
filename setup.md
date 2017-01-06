---
layout: page
title: "Getting Setup"
description: "Getting your computer setup for DS100 work"
group: navigation
order: 2
---

{% include JB/setup %}

## Contents

- **Installation**
  - [OSX](#osx)
  - [Windows](#windows)
  - [Linux](#linux)
- [Working on assignments](#working-on-assignments)
- [Opening notebooks](#opening-notebooks)
- [Verifying your installation](#verifying-your-installation)

## OSX

1. First, let's install `brew` if you haven't done that yet. In your terminal,
   run:

        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

   Verify your installation by making sure `brew --version` doesn't error at
   your terminal.

2. Next, install `wget`. This is a command-line tool that lets you download
   files / webpages at the command line.

        brew install wget

3. Download the Anaconda installation script:

        wget -O install_anaconda.sh https://repo.continuum.io/archive/Anaconda3-4.2.0-MacOSX-x86_64.sh

4. Install Anaconda:

        bash install_anaconda.sh

   Ensure the installation worked by running `conda --version`.

5. Run these commands to create a new [conda environment][env]. Each conda
   environment has its own package versions. This allows us to switch between
   package versions easily. For example, this class uses Python 3, but you
   might have another that uses Python 2. With a conda environment, you can
   switch between those at will.

        # Create a conda env called ds100 that uses python 3.5
        conda create --name ds100 python=3.5

        # Switch to the ds100 environment
        source activate ds100

        # Install the packages for ds100
        conda install -n ds100 jupyter pandas numpy matplotlib scikit-learn seaborn
        pip install datascience okpy

   From now on, you can switch to the `ds100` env with `source activate ds100`,
   and switch back to the default env with `source deactivate`.

6. Now, use `brew` to install the latest version of `git` by running:

        brew install git

   Ensure that `git` is installed by running `git --version`. The version
   should be 2.5.0 or higher.

You may remove the `install_anaconda.sh` script now if you'd like since it's
quite large.

[**Click here to continue to the next part of the setup.**](#working-on-assignments)

## Windows

Getting set up on Windows is especially prone to error if you aren't careful
about your configuration. If you've already had Anaconda or `git` installed and
can't get the other to work, try uninstalling everything and starting from
scratch.

### Installing Anaconda:

1. Visit https://www.continuum.io/downloads#windows and download the installer
   for Python 3.5. Download the 64-bit installer if your computer is 64-bit
   (more likely), the 32-bit installer if not. You can Google how to check
   whether your computer is 64 or 32 bit.

2. Leave all the options as default (install for all users, in the default
   location). Make sure both of these checkboxes are checked:

   ![conda4](https://cloud.githubusercontent.com/assets/2468904/21345446/24440520-c655-11e6-9d3d-f56d32ed7029.PNG)

3. Install.

4. Verify that the installation is working by starting the Anaconda Prompt (you
   should be able to start it from the Start Menu) and typing `python`:

   ![conda6](https://cloud.githubusercontent.com/assets/2468904/21345449/24497f5a-c655-11e6-9181-d253e5c0d07c.PNG)

   Notice how the `python` prompt shows that it is running from Anaconda. Now
   you have `conda` installed!

5. Run these commands to create a new [conda environment][env]. Each conda
   environment has its own package versions. This allows us to switch between
   package versions easily. For example, this class uses Python 3, but you
   might have another that uses Python 2. With a conda environment, you can
   switch between those at will.

        # Create a conda env called ds100 that uses python 3.5
        conda create --name ds100 python=3.5

        # Switch to the ds100 environment
        activate ds100

        # Install the packages for ds100
        conda install -n ds100 jupyter pandas numpy matplotlib scikit-learn seaborn
        pip install datascience okpy

   From now on, you can switch to the `ds100` env with `activate ds100`,
   and switch back to the default env with `deactivate`.

### Installing `git`:

1. You might already have `git` installed. Type `git` at the Anaconda Prompt.
   If that works, then you can skip these steps. Otherwise, you'll something
   that looks like:

   ![git1](https://cloud.githubusercontent.com/assets/2468904/21345450/244d2cae-c655-11e6-9a3f-1dee57be0ed6.PNG)

2. At the anaconda prompt, type:

        conda install -c anaconda git -y

3. Now, verify that `git` is installed by typing `git --version` on the command
   line. You should see output that looks like:

   ![git4](https://cloud.githubusercontent.com/assets/2468904/21345451/2457579c-c655-11e6-8ece-d760cf548749.PNG)

[**Click here to continue to the next part of the setup.**](#working-on-assignments)

## Linux

These instructions assume you have `apt-get` (Ubuntu and Debian).
For other distributions of Linux, substitute the available package manager.

2. Install `wget`. This is a command-line tool that lets you download
   files / webpages at the command line.

        sudo apt-get install wget

3. Download the Anaconda installation script:

        wget -O install_anaconda.sh https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh

   If you have a 32-bit operating system, use this command instead.

        wget -O install_anaconda.sh https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86.sh

4. Install Anaconda:

        bash install_anaconda.sh

   Ensure the installation worked by running `conda --version`.

5. Run these commands to create a new [conda environment][env]. Each conda
   environment has its own package versions. This allows us to switch between
   package versions easily. For example, this class uses Python 3, but you
   might have another that uses Python 2. With a conda environment, you can
   switch between those at will.

        # Create a conda env called ds100 that uses python 3.5
        conda create --name ds100 python=3.5

        # Switch to the ds100 environment
        source activate ds100

        # Install the packages for ds100
        conda install -n ds100 jupyter pandas numpy matplotlib scikit-learn seaborn
        pip install datascience okpy

   From now on, you can switch to the `ds100` env with `source activate ds100`,
   and switch back to the default env with `source deactivate`.

6. Now, install the latest version of `git`:

        sudo add-apt-repository ppa:git-core/ppa
        sudo apt-get update
        sudo apt-get install git

   Ensure that `git` is installed by running `git --version`. The version
   should be 2.5.0 or higher.

You may remove the `install_anaconda.sh` script now if you'd like since it's
quite large.

[env]: http://conda.pydata.org/docs/using/envs.html

[**Click here to continue to the next part of the setup.**](#working-on-assignments)

## Working on assignments

These instructions are the same for OSX, Windows, and Linux.

Now, let's download the course materials so you can start working on
assignments.

1. Visit https://github.com/ and log in / create an account if you don't
   already have one.
2. Visit https://ds100-repo.herokuapp.com/ and fill out the form to create a
   private repo to hold all of your work this semester. Bookmark the URL
   because you'll be using it soon.
3. In your terminal, navigate to the directory you want to put the DS100
   assignments in.
4. Run the following commands. Replace `<URL_OF_YOUR_PRIVATE_REPO>` with the
   URL of your repo.

    ```
    # Download the repo
    git clone https://github.com/DS-100/sp17-materials

    # Enter the repo folder
    cd sp17-materials

    # Rename the origin remote to ds100
    git remote rename origin ds100

    # Set the origin remote to your repo
    git remote add origin <URL_OF_YOUR_PRIVATE_REPO>
    ```

For example, if my repo is https://github.com/DS-100/s0001 I'd run:

    git remote add origin https://github.com/DS-100/s0001

This should download a copy of the course materials (including this homework)
onto your personal computer and set up `git` remotes so that you can pull
released assignments from the staff and push your personal work to your private
repo.

Now, when you want to pull new/updated assignments, you can run:

    git pull ds100 master

And when you want to push your work to your private repo:

    git push origin master

## Opening notebooks

To open Jupyter notebooks, you'll navigate to the `sp17-materials`
directory and run:

    jupyter notebook

This will automatically open the notebook interface in your browser. You can
then browse to a notebook and open it.

## Verifying your installation

Finally, let's open a notebook that will check to see whether you've installed
everything correctly.

In your `sp17-materials` directory, ensure that you are in the `ds100` conda
environment by running `source activate ds100` on OSX / Linux or `source
activate` on Windows. Then, run `git pull ds100 master` and then `jupyter
notebook`.

Now, open the `test_setup.ipynb` notebook. If you've installed everything
correctly, all the cells should run without error.

Congrats! You've set up your computer for DS100 work.
