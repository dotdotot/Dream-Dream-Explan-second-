int motor1 = 2;
int motor1_2 = 3;
int motor2 = 4;
int motor2_2 = 5;
int motor1_pwm = 10;
int motor2_pwm = 11;

void setup() {
  pinMode(motor1, OUTPUT);
  pinMode(motor1_2, OUTPUT);
  pinMode(motor2, OUTPUT);
  pinMode(motor2_2, OUTPUT);

  pinMode(motor1_pwm, OUTPUT);
  pinMode(motor2_pwm, OUTPUT);

  analogWrite(motor1_pwm, 70);
  analogWrite(motor2_pwm, 70);
}

void loop() {
  digitalWrite(motor1, HIGH);
  digitalWrite(motor1_2, LOW);
  delay(1000);

  digitalWrite(motor1, LOW);
  digitalWrite(motor1_2, HIGH);
  delay(1000);

  digitalWrite(motor1, LOW);
  digitalWrite(motor1_2, LOW);

  digitalWrite(motor2, HIGH);
  digitalWrite(motor2_2, LOW);
  delay(1000);

  digitalWrite(motor2, LOW);
  digitalWrite(motor2_2, HIGH);
  delay(1000);

  digitalWrite(motor2, LOW);
  digitalWrite(motor2_2, LOW);
}
