int eegPin = 0;
int voltage = 0;
int filtered = 0;
float alpha = 0.25;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  voltage = analogRead(eegPin);
  filtered = alpha*voltage + (1-alpha)*filtered;
  Serial.println(filtered);
}
