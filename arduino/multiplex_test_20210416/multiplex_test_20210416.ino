 //multiplexer's two level reader for constant resistance
//Mux control
int sig = A0;
int s3 = 9;
int s2 = 10;
int s1 = 11;
int s0 = 12;
int en = 13;

int s3_2 = 7;
int s2_2 = 6;
int s1_2 = 5;
int s0_2 = 4;

float Vin=3.3;        //voltage at 5V pin of arduino
float Vout=0;     //voltage at A0 pin of arduino
float R1=18000;    //value of known resistance
float R2=0;       //value of unknown resistance
float buffer=0; 
int number = 0;   //number of each resistance
String reciver;
boolean start=true;
int muxChannel[16][16][10];

void setup() {  
  pinMode(sig, INPUT);
  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(en, OUTPUT);
  pinMode(s0_2, OUTPUT);
  pinMode(s1_2, OUTPUT);
  pinMode(s2_2, OUTPUT);
  pinMode(s3_2, OUTPUT);

  digitalWrite(s0, LOW);
  digitalWrite(s1, LOW);
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  digitalWrite(s0_2, LOW);
  digitalWrite(s1_2, LOW);
  digitalWrite(s2_2, LOW);
  digitalWrite(s3_2, LOW);
  digitalWrite(en, LOW);
  Serial.begin(115200);
//  Serial.println("Setup Finished...");
}

void loop() {
  if(Serial.available()>0){
    reciver = Serial.readStringUntil('\n');
    Serial.println(reciver);
    if(reciver == "start"){
      start = true;
    }
    else if(reciver == "break"){
      start = false;
    }
    Serial.print(start);
  }
  if(start){
      for (int i = 0; i < 16; i ++) {
        readMux(i);
      }
      Serial.println("ALL DONE");
   } 
//  for (int i = 0; i < 16; i ++) {
//    Serial.print("Multiplexer");
//    Serial.println(i);
//    readMux(i);
//     Serial.println("Done");
//     Serial.println("");
//  }
//  Serial.println("ALL DONE");
////  while(10);
}

 //second level multiplexer select
int readMux2(int channel) {

  int controlPin[] = {s0_2, s1_2, s2_2, s3_2};

  int muxChannel[16][4] = {
    {0, 0, 0, 0}, //channel 0
    {1, 0, 0, 0}, //channel 1
    {0, 1, 0, 0}, //channel 2
    {1, 1, 0, 0}, //channel 3
    {0, 0, 1, 0}, //channel 4
    {1, 0, 1, 0}, //channel 5
    {0, 1, 1, 0}, //channel 6
    {1, 1, 1, 0}, //channel 7
    {0, 0, 0, 1}, //channel 8
    {1, 0, 0, 1}, //channel 9
    {0, 1, 0, 1}, //channel 10
    {1, 1, 0, 1}, //channel 11
    {0, 0, 1, 1}, //channel 12
    {1, 0, 1, 1}, //channel 13
    {0, 1, 1, 1}, //channel 14
    {1, 1, 1, 1}  //channel 15
  };

  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }
}

  //first level multiplexer select
int readMux(int channel) {

  int controlPin[] = {s0, s1, s2, s3};
  int controlPin_2[] = {s0_2, s1_2, s2_2, s3_2};

  int muxChannel[16][4] = {
    {0, 0, 0, 0}, //channel 0
    {1, 0, 0, 0}, //channel 1
    {0, 1, 0, 0}, //channel 2
    {1, 1, 0, 0}, //channel 3
    {0, 0, 1, 0}, //channel 4
    {1, 0, 1, 0}, //channel 5
    {0, 1, 1, 0}, //channel 6
    {1, 1, 1, 0}, //channel 7
    {0, 0, 0, 1}, //channel 8
    {1, 0, 0, 1}, //channel 9
    {0, 1, 0, 1}, //channel 10
    {1, 1, 0, 1}, //channel 11
    {0, 0, 1, 1}, //channel 12
    {1, 0, 1, 1}, //channel 13
    {0, 1, 1, 1}, //channel 14
    {1, 1, 1, 1}  //channel 15
  };

  for (int i = 0; i < 4; i ++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
 //   delay(10);
    }
      for (int i = 0; i < 16; i ++) {
      readMux2(i);
    float value = analogRead(sig);// Get Lux value
    buffer=value*Vin;
    Vout=(buffer)/1023.0;
//    Serial.println(5*analogRead(sig)/1023.0*1000);
    buffer=Vout/(Vin-Vout); 
    R2=R1*buffer;
    Serial.print(number);
    Serial.print(":");
    Serial.println(R2);
//    Serial.println(Vout);
    if(number<250){
      number++;
      }else{
        number = 0;
        break;
      }
  }
}
 
