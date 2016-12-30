---
layout: page
title: "Getting Setup"
description: "Getting your computer setup for DS100 work"
group: navigation
order: 2
---

{% include JB/setup %}

## Contents

- [OSX](#osx)
- [Windows](#windows)
- [Linux](#linux)

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

5. Now, use `brew` to install the latest version of `git` by running:

        brew install git

   Ensure that `git` is installed by running `git --version`. The version
   should be 2.5.0 or higher.

Congrats! You are ready for DS100 work. You may remove the
`install_anaconda.sh` script now if you'd like since it's quite large.

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
   you have Python installed!

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

   Congrats! You now have both Anaconda and `git` set up and are ready to start
   the real work of Data 100.

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

5. Now, install the latest version of `git`:

        sudo add-apt-repository ppa:git-core/ppa
        sudo apt-get update
        sudo apt-get install git

   Ensure that `git` is installed by running `git --version`. The version
   should be 2.5.0 or higher.

Congrats! You are ready for DS100 work. You may remove the
`install_anaconda.sh` script now if you'd like since it's quite large.
