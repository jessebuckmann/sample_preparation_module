The following steps will guide you how to get everything running from scratch (reading [Possible problems](#Possible problems) section recommended)

### Windows installation

1. Go to https://github.com/SanliFaez/labphew

   1. Download the zip archive after pressing the "Code" button
   2. Extract the zip into a place of your choosing

   Another variant how you can get the copy of this repo:
   1.  Open the command prompt. You can open the command prompt by searching "powershell" or "cmd" in windows search. Or type Win+R, type "powershell" or "cmd" and press Enter
   2.  Type **git clone https://github.com/SanliFaez/labphew** . This command will make a copy of this repo in your current folder without need to zip/unzip the repo. You need to have Git installed on your system

2. Install anaconda from: https://www.anaconda.com/products/individual

   1. Open the anaconda prompt by searching "anaconda prompt" in windows
   2. Navigate to your copied repository folder "master-labphew" in the anaconda prompt using ***cd C:/path/to/dir/.../master-labphew*** (you can go up a folder using **cd ..**). Or just copy the path from file explorer and type **cd** and then insert the path
   3. Type ***pip install -e .*** and press Enter
   4. (Do only if use Spyder IDE) Type ***pip install pyqtwebengine*** and press enter *twice* (the second time after the first one is done). This package is needed only for Spyder IDE, without it it won't start

   Or you can do all the same but without installing heavy and slow anaconda. The main benefit which anaconda gives is that it installs Python to you computer. But if you already have Python installed, you probably want to go without anaconda.

   1. Navigate to your copied repository folder "master-labphew" in the command prompt (watch 1 step) using ***cd C:/path/to/dir/.../master-labphew*** (you can go up a folder using **cd ..**). Or just copy the path from file explorer and type **cd** and then insert the path
   2. Type ***pip install -e .*** and press Enter
   3. (Do only if use Spyder IDE) Type ***pip install pyqtwebengine*** and press enter *twice* (the second time after the first one is done). This package is needed only for Spyder IDE, without it it won't start

3. Download and install Waveforms program from: https://mautic.digilentinc.com/asset/110:waveforms-windows-64-bit-download. Agree to default options. The detailed guide(on Windows you don't need it) is [there](https://reference.digilentinc.com/learn/instrumentation/tutorials/analog-discovery-2-getting-started)

4. Go to https://git.science.uu.nl/ued2020/experiment-design-2020

   1. Download a zip of the repository. Extract the zip. Or you can do the same via Git as with labphew
   2. Go to experiment-design-2020/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/ folder
   3. Now you are all set to go to the [README](/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/README.md) on how to use the program!

### Linux installation

! Sadly, currently the Linux version on the program doesn't work. Everything is fine until the very last step 4.3 !

The steps on Linux are quite the same as on Windows, apart from the terminal launch. In Linux you need to google how to do that in your distribution. And on step 3 you need to install additional software as said [in this guide](https://reference.digilentinc.com/learn/instrumentation/tutorials/analog-discovery-2-getting-started). When you need to install Adept Runtime(not sdk, but runtime), go [there](https://reference.digilentinc.com/reference/software/adept/start?redirect=1) and download the latest version. To save you time, you can download the Waveforms software(after installing Adept Runtime) from [this](https://mautic.digilentinc.com/waveforms-download) page.

And in step 4 before launching the program comment the lines in BIMBO_Interface.py :

```
myappid = 'BIMBO'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
```

### MacOS installation

Well, you is going to be the first person who try to run this on mac. This [guide](https://reference.digilentinc.com/learn/instrumentation/tutorials/analog-discovery-2-getting-started) will show you how to install the Waveforms software, other steps are the same as in Windows.

### Android and IOS

Just install Windows

## Possible problems

It is important to watch where you install your packages. When you open the file in IDE and run it, you do that using some version of Python. If you have only one version of Python in the system, that's the easiest variant, all packages you install will be pinned to this Python version. But if you have multiple versions, the packages you install in one Python version won't be available in another. Why so? When installing packages, Python uses special module called pip. With each version of Python comes it's own pip module. And each pip module installs packages only for it's own version of Python. That's why if you install package in Python 3.6, you won't be able to use it in Python 3.7. Well, technically you probably can by finding in file system all the files of the package and copying them to the folder of another python version and doing something else, but that's a hassle, so we won't consider that.

The possible problem is that when you install Anaconda, it installs its own Python version with it. And you need to ensure that you install packages to the same Python version, which you will use in your IDE to run the python file. This can be easily done by typing command **pip -V** in the terminal, which gives you the full path to your pip module so you can see to which Python version you will install packages with it.