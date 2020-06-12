float alt = 0.0;
float speed_ = 0.0;
float gforce = 0.0;
float bat_temp = 0.0;
float cube_temp = 0.0;
float motor_temp = 0.0;
float pressure = 0.0;
int lat = 0.0;
int long_ = 0.0;
int pings = 0;
String s = ";";

int camera_recording = 1;

void setup() {
   Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
    camera_recording = Serial.read();
  } 

  if(camera_recording == 1) {
    lat = 1;
    long_ = 1;
  } else {
    lat = 0;
    long_ = 0;
  }
    
  alt += 10.23;
  speed_ += 9.1;
  gforce += .1;
  bat_temp += .1;
  cube_temp += .3;
  motor_temp += .4;
  pressure += .2;
 
  Serial.println(alt + s + speed_ + s + gforce + s + bat_temp + s + cube_temp + s + motor_temp + s + pressure + s + lat + s + long_ + s + pings += 1 + s);
  delay(200);
}
