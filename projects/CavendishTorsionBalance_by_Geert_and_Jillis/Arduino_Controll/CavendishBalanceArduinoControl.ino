#include <Servo.h>



Servo bigServo;                 // providing a name

int ballsDelay = 2400;          // Timelength to move balls from counterclockwise to clockwise position (and vice versa)



int incomingByte = 0; // for incoming serial data
int toServo = 0;      // to send to servo
int stateBalls = 0;   // 0 for center, 1 for fully left, -1 for fully right

void setup()
{
  bigServo.attach(3);
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Native USB only
  }

  Serial.print("Hello world.");
}



void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte);

    if(incomingByte == 83 && stateBalls == 0){ //Start from 0 position, go to the "+1" position on input S
      Serial.print("Start");
      Serial.println();
      int localDelay = ballsDelay / 2;
      toServo = 180;
      bigServo.write(toServo);
      toServo = 90;
      delay(localDelay);
      bigServo.write(toServo);
      stateBalls = 1;
    }

    else if(incomingByte == 69){ //Go from any position back to the neutral position on input E
      Serial.print("End");
      Serial.println();
      int localDelay = ballsDelay / 2;
      if (stateBalls == 1){toServo = 0;}
      else if (stateBalls == -1) {toServo = 180;}
      bigServo.write(toServo);
      toServo = 90;
      delay(localDelay);
      bigServo.write(toServo);
      stateBalls = 0;
    }
    
    else if(incomingByte == 82 && stateBalls == 1){ //Go to the "-1" position on input R
      Serial.print("Go right");
      Serial.println();
      toServo = 0;
      bigServo.write(toServo);
      toServo = 90;
      delay(ballsDelay);
      bigServo.write(toServo);
      stateBalls = -1;
    }
    
    else if(incomingByte == 76 && stateBalls == -1){ //Go to the "+1" position on input L
      Serial.print("Go left");
      Serial.println();
      toServo = 180;
      bigServo.write(toServo);
      toServo = 90;
      delay(ballsDelay);
      bigServo.write(toServo);
      stateBalls = 1;
    }

    
    else if(incomingByte == 108 ){ //finetune the position in "+1" direction on input l
      Serial.print("Go Left");
      Serial.println();
      toServo = 180;
      bigServo.write(toServo);
      toServo = 90;
      int localDelay = 100;
      delay(localDelay);
      bigServo.write(toServo);
    }    
    else if(incomingByte == 114){ //finetune the position in "-1" direction on input r
      Serial.print("Go Left");
      Serial.println();
      toServo = 0;
      bigServo.write(toServo);
      toServo = 90;
      int localDelay = 100;
      delay(localDelay);
      bigServo.write(toServo);
    }

  }
}
