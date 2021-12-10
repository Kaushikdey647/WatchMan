/*Simple Intrusion Detector
   Consists of -
   1. LED X 1
   2. PIEZO BUZZER X 1
   3. HC-SRO4 X 1
   4. ARDUINO UNO R3
   5. BREADBOARD
   6. JUMPER WIRES
   Creator : Kaushik Dey(Kaushikdey647@gmail.com)
*/
int sonicTrig = 7; // Sonic Transmitter (connect 7 to echo)
int sonicEcho = A2; // Sonic reciever (connect A2 to echo)
float objDist; // object disatnce
float tPeriod; // Time in sonic reflection
float temp;
//Setting pin modes
void setup() {
  Serial.begin(9600);
  pinMode(sonicTrig, OUTPUT); // Set trig as output mode
  pinMode(sonicEcho, INPUT); // Set echo as input mode
  digitalWrite(sonicTrig, LOW); // to deactivate the pulse
  delay(1000); //hold it for a sec
  temp = 0;
}
//doing the thing
void loop() {
  digitalWrite(sonicTrig, HIGH);// Send cycle sonic bursts
  delay(10);//for 10 nanoseconds
  digitalWrite(sonicTrig, LOW);//then turn it off
  tPeriod = pulseIn(sonicEcho, HIGH);//and check the time taken in reflection
  objDist = tPeriod * 0.017; //calculate object distance
  objDist = (0.3*objDist + 0.7*temp);
  if(objDist>1000)objDist = 1000;
  Serial.println(objDist);
  temp = objDist;
}
