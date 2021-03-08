# include <Servo.h>

String Data; //"X:90,Y:40"
String Serialdata;


char degree[3];
int pos;
Servo servo_X;
Servo servo_Y;
byte a[3];

// data returns a string of the direction the motor should go 
// X:90,Y:180

void setup() {
  servo_connect();
  Serial.begin(9600);
  // timeout is usally 1s. causes a delay in serial port
  Serial.setTimeout(10) ; 
}

void loop() {
     // move servo
       
}


void servo_connect(){
  servo_X.attach(10);
  servo_Y.attach(11);
}

void serialRead(){
  Serialdata = Serial.readString();
  //servo_X.write(parseData_X(Data));
  //servo_X.write(parseData_Y(Data));
  Serial.println(parseData_X(Serialdata));
  Serial.println(parseData_Y(Serialdata));
   
}
  
  
int parseData_X(String data){
  //myString.remove(index, count)
  // count indicates the number of charter to remove
  data.remove(data.indexOf(","));
  data.remove(0,data.indexOf(":") + 1) ; 
    return data.toInt();
  }

int parseData_Y(String data){
  data.remove(data.indexOf("X"),7);
    return data.toInt();
}
