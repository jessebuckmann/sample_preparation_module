Dear Contributor, we appreciate you showing your willingness to contribute! If you want to report a bug or suggest a change please adhere to the steps in this [README](https://git.science.uu.nl/r.deberg/experiment-design-2020/-/tree/master/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno#how-to-report-issuesbugscomplimentscomplaints)

### Adding your own tab!

The easiest way to contribute is by adding new tabs with programs to the BIMBO_Interface.
The way to this is creating a QDialog. Just make a new python file and start with the following class:

```python
from PyQt5.QtWidgets import *

class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
```
In order to add this QWidget to the main window, you can simply import the file at the top of BIMBO_Interface by placing it in the same folder and importing it with:

```python
Import YourFILE
```

Now you can add a new line of code to the BIMBO_Interface.py in the function StartProgram after the line tabwidget = QTabWidget():

```python
tabwidget.addTab(YourFILE.YourWidget(), 'Choose a fun name here')
```
Now a new tab should appear in the BIMBO_Interface.
Now you can use all of PyQt5 to add new stuff to your widget! The complete documentation can be found [here](https://pypi.org/project/PyQt5/).
A quick example would be to add a button by 

```python
from PyQt5.QtWidgets import *

class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
        myButton = QPushButton('A useless button', self)
        myButton.resize(100, 32)
        myButton.move(50, 50)
```
This will display a button that does not yet do anything. In order to give let the button execute a function called YourFunction you can do

```python
from PyQt5.QtWidgets import *

class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
        myButton = QPushButton('A useless button', self)
        myButton.resize(200, 32)
        myButton.move(50, 50)
        myButton.clicked.connect(self.YourFunction)
    
    def YourFunction(self):
        print("Hello")
```
Use you creativity to make amazing buttons that can change the world! Good luck with contributing to the project.


### Implementing new features

If you feel really experienced and up to a challenge, you can try to implement one of the usefull planned features. See the list below!

1. **An Overview tab**

The idea of this tab is that is shows you the current values of all measured quantities, such that you can take a quick look and see how your experiment is going.

2. **A button that can rotate the balls for the Cavendish experiment**.

This button just rotates the balls. They already have the program, just needs to be implemented.

### Fixing bugs
A list of known bugs can be found [here](/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/Programs/Bugs.md).
