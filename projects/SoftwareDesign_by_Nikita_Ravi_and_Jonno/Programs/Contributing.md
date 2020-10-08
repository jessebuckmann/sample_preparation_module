Dear Contributor, we appreciate you showing your willingness to contribute!

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
*tabwidget.addTab(YourFILE.YourWidget(), 'Choose a fun name here')*
```
Now a new tab should appear in the BIMBO_Interface.
Now you can use all of PyQt5 to add new stuff to your widget! The complete documentation can be found [here](https://pypi.org/project/PyQt5/).
A quick example would be to add a button by 

```python
class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
        myButton = QPushButton('A useless button', self)
        myButton.resize(100, 32)
        myButton.move(50, 50)
```
This will display a button that does not yet do anything. In order to give let the button execute a function called YourFunction you can do

```python
class YourWidget(QWidget):
    def __init__(self):
        super().__init__()
        myButton = QPushButton('A useless button', self)
        myButton.resize(100, 32)
        myButton.move(50, 50)
        myButton.clicked.connect(self.YourFunction)
```
Use you creativity to make amazing buttons that can change the world! Good luck with contributing to the project.
