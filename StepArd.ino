#define XSTEP 2
#define XDIR 5
#define XSTOP 9
#define photoDiodePin A3

int fromPC = 0;
unsigned int sRange = 2880, sRes = 4, delay_home = 3, delay_sense = 500;

void stepper(unsigned char rot_rsln)
{
  for (int i = 0; i < rot_rsln; i++)
  {
    digitalWrite(XSTEP, LOW);
    delayMicroseconds(delay_sense);
    digitalWrite(XSTEP, HIGH);
    delayMicroseconds(delay_sense);
  }
}
void homing(void)
{
  digitalWrite(XDIR, LOW); //towards Limit Switch
  delay(10);
  while (digitalRead(XSTOP) == 1)
  {
    digitalWrite(XSTEP, LOW);
    delay(delay_home);
    digitalWrite(XSTEP, HIGH);
    delay(delay_home);
  }
}
void analyZinator(void)
{
  delay(500);
  int stp_tot = 0;
  while (stp_tot <= sRange)
  {
    digitalWrite(XDIR, HIGH); //away from Limit Switch
    delay(10);
    stepper(sRes);
    stp_tot = stp_tot + sRes;

    int inten = 0; int sumInten = 0; int avgInten = 0;
    delay(20);
    for (int i = 1; i <= 5; i++) {
      delay(30);
      inten = 1024 - analogRead(photoDiodePin);
      sumInten = sumInten + inten;
    }
    avgInten = sumInten / 5;
    Serial.println(avgInten);
    delay(20);
  }
}

void setup() {
  pinMode(XSTEP, OUTPUT);
  pinMode(XDIR, OUTPUT);
  pinMode(XSTOP, INPUT_PULLUP);
  Serial.begin(115200);
  Serial.flush();
  homing();
  delay(100);
}

void loop() {
  delay(100);
  if (Serial.available() > 0) {
    delay(300);
    fromPC = Serial.read();
    if (fromPC == '1') {
      delay(100);
      analyZinator();
      delay(500);
      Serial.println("exit");
      delay(200);
      homing();
    }
  }
}
