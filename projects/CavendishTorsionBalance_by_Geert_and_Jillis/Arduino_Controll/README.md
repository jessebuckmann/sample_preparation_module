The other file in this directory has the code to control the arduino and continuous servo for the Cavendish Balance.  
To control the arduino open this in the [arduino web editor](https://create.arduino.cc/editor) (or in your own local installation of the arduino editor). 
Set the board/port dropdown to "Arduino Due" and open the Serial Monitor from the sidebar.
You can send the code to the arduino by clicking on the arrow next to the board/port dropdown, the arduino will send a "hello world" message when the initiallization has worked.
More information on the arduino web editor can be found [here](https://create.arduino.cc/projecthub/Arduino_Genuino/getting-started-with-arduino-web-editor-on-various-platforms-4b3e4a)

The turningtable is controlled by sending single characters to the arduino; E, L, R, S, l and r.
- S will turn the turningtable from the neutral position to one of the measurement positions
- E will turn the turningtable from one of the measurement positions to the neutral position
- L or R will turn the turningtable from one to the other measurement position
- l or r will turn the turningtable slightly in the same direction as L and R respectively
