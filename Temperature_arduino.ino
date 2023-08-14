int pinTemp = A5;   //This is where our Output data goes

void setup() {
  Serial.begin(9600);     
}

void loop() {
  float temp = analogRead(pinTemp);    //Read the analog pin
  temp = temp * 0.48828125;   // convert output (mv) to readable celcius
  
  // Get the current timestamp in milliseconds
  unsigned long currentMillis = millis();
  
  // Calculate hours, minutes, and seconds from milliseconds
  int seconds = (currentMillis / 1000) % 60;
  int minutes = (currentMillis / (1000 * 60)) % 60;
  int hours = (currentMillis / (1000 * 60 * 60)) % 24;
  
  // Print the timestamp
  Serial.print(hours);
  Serial.print(":");
  if (minutes < 10) Serial.print("0"); // Add leading zero if minutes < 10
  Serial.print(minutes);
  Serial.print(":");
  if (seconds < 10) Serial.print("0"); // Add leading zero if seconds < 10
  Serial.print(seconds);
  Serial.print(" - Temperature: ");
  Serial.print(temp);
  Serial.println("C");  //print the temperature status
  
  delay(1000);  
}
