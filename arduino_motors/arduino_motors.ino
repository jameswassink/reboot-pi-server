#define M11 3
#define M12 5
#define M21 6
#define M22 9

int input = 0;

int** motorPins;

void setup() {
  // put your setup code here, to run once:
    
  Serial.begin(9600);
  
  
  //pinMode(13,OUTPUT);
  pinMode(M11, OUTPUT);
  pinMode(M12, OUTPUT);
  pinMode(M21, OUTPUT);
  pinMode(M22, OUTPUT); 
  
 // delay(1000);
  while (!Serial){;}

  Serial.println("hello");
}


void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    input = Serial.read();
    Serial.print(input, DEC);
    switch(input){
      case 119:
        goForwards();
        break;
      case 115:
        goBackwards();
        break;
      case 97:
        rotateLeft();
        break;
      case 100:
        rotateRight();
        break;
      default: 
        stopMoving();
        break;
    }
  }
}

void goForwards(){
  Serial.println("moving forwards");
  motorForward(0);
  motorForward(1);
}

void goBackwards(){
  motorReverse(0);
  motorReverse(1);
}

void rotateLeft(){
  motorForward(1);
  motorReverse(0);
}

void rotateRight(){
  motorForward(0);
  motorReverse(1);
}

void stopMoving(){
  motorStop(0);
  motorStop(1);
}


void motorForward(int motor){
  int pin = getPinForMotor(motor, 0);
  digitalWrite(pin, HIGH);
  Serial.print(pin);
  Serial.print(", ");
  pin = getPinForMotor(motor, 1);
  digitalWrite(pin, LOW);
  Serial.println(pin);
}

void motorReverse(int motor){
  digitalWrite(getPinForMotor(motor, 0), LOW);
  digitalWrite(getPinForMotor(motor, 1), HIGH);
}

void motorStop(int motor){
  digitalWrite(getPinForMotor(motor, 0), LOW);
  digitalWrite(getPinForMotor(motor, 1), LOW);
}


int getPinForMotor(int motor, int pin){
  if (motor == 0){
    if (pin == 0){
      return M11;
    }
    else {
      return M12;
    }
  }
  else {
    if (pin == 0 ){
      return M21;
    }
    else {
      return M22;
    }
  }
}