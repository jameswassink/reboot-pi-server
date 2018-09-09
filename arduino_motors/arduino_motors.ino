#define M11 3
#define M12 5
#define M21 6
#define M22 9

int input = 0;

int** motorPins;

void setup() {
  // put your setup code here, to run once:
    
  Serial.begin(9600);
  
  
  pinMode(13,OUTPUT);
  pinMode(M11, OUTPUT);
  pinMode(M12, OUTPUT);
  pinMode(M21, OUTPUT);
  pinMode(M22, OUTPUT);

  int mp1[] = {M11, M12};
  int mp2[] = {M21, M22};
  
  motorPins[0] = mp1;
  motorPins[1] = mp2;
  
  delay(1000);
  while (!Serial){;}

//for (int i = 0; i < 5; i++){
  Serial.println("hello");
//}

  establishContact();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    input = Serial.read();
    Serial.print(input);
    switch(input){
      case 'w':
        goForwards();
        break;
      case 's':
        goBackwards();
        break;
      case 'a':
        rotateLeft();
        break;
      case 'd':
        rotateRight();
        break;
      default: 
        stopMoving();
        break;
    }
  }
}

void goForwards(){
  motorForward(0);
  motorForward(1);
}

void goBackwards(){
  motorReverse(0);
  motorReverse(1);
}

void rotateLeft(){
  motorReverse(0);
  motorForward(1);
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
  digitalWrite(motorPins[motor][0], HIGH);
  digitalWrite(motorPins[motor][1], LOW);
}

void motorReverse(int motor){
  digitalWrite(motorPins[motor][0], LOW);
  digitalWrite(motorPins[motor][1], HIGH);
}

void motorStop(int motor){
  digitalWrite(motorPins[motor][0], LOW);
  digitalWrite(motorPins[motor][1], LOW);
}
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}
