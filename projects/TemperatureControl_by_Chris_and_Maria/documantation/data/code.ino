// Declare components of the circuit, Pins used, Temperatures

float R= 150; // Resistance used in circuit
float r_0= 100; //Thermistor at 0 Celcius
float a= 0.0039 ;// constant characterizing thermistor 

int PIN_HEATING= 2;
int PIN_COOLING =13;
int PIN_EMERGENCY= 41;
int PIN_MASTER =51;


int T_L =15;
int T_H= 30;
int H_D= 35;
int L_D= 10;

//-------------------------------------------------------------------------------------------------
void setup() {
  Serial.begin(9600);
 }

//Reads Output voltage in arduino units and translate it into degrees. (Voltage divider)

float read_Temperature(){
  float sensor = analogRead(A0);
  float x = (R/r_0)*(1023/sensor -1) -1;
  float T= x/a ;
  return T;    
  }

// Control functions for the response of arduino
void activate_heater(){
  digitalWrite(PIN_COOLING,LOW);
  digitalWrite(PIN_HEATING,HIGH); }

void activate_cooler(){
  digitalWrite(PIN_HEATING,LOW);
  digitalWrite(PIN_COOLING,HIGH);}

void deactivate(){
  digitalWrite(PIN_COOLING,LOW);
  digitalWrite(PIN_HEATING,LOW);}

void danger(){
  deactivate();
  digitalWrite(PIN_EMERGENCY,HIGH);
  delay(360000);
                                //The red button. If T exceeds prespecified temp, it sends a message to master. It shuts down any cooling or heating and sleeps for an hour;
  }



//MAIN----------------------------------------------------------------------------------------------------------------------

void loop() {
 float T = read_Temperature();
 if (T<L_D or T> H_D){danger();}
 
 if (T<T_H){
    activate_cooler();  }
 
 else if (T>T_L){
    activate_heater();}
 
 else{ deactivate();}
 Serial.print("Temperature = ");
 Serial.println(T); 
 Serial.println ("*C");
 delay(20000) ;
}
