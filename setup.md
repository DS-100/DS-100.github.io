---
layout: page
title: "Getting Setup"
description: "Getting your computer setup for DS100 work"
group: navigation
order: 2
---

{% include JB/setup %}

## Steps to get set up for DS100 on Windows

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

2. Visit https://git-scm.com/download/win to start the download.

3. Install using all the defaults, making sure that the "Use Git from the
   Windows Command Prompt" checkbox is checked:

   ![git3](https://cloud.githubusercontent.com/assets/2468904/21345448/24497da2-c655-11e6-92e2-e150ce1acc3f.PNG)

4. Now, verify that `git` is installed by closing and reopening the Anaconda
   Prompt and then typing `git --version`. You should see output that looks
   like:

   ![git4](https://cloud.githubusercontent.com/assets/2468904/21345451/2457579c-c655-11e6-8ece-d760cf548749.PNG)

   Congrats! You now have both Anaconda and `git` set up and are ready to start
   the real work of Data 100.
