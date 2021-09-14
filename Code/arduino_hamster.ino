//Numbers of leds for different sensors inputs
int sensor_1_LED = 11;
int sensor_2_LED = 12;
int sensor_3_LED = 13;

//Number of pins for sensors inputs
int sensor_1_DATA = A1;
int sensor_2_DATA = A2;
int sensor_3_DATA = A3;

//Thresholds for sensors
int sensor_1_TRESH = 600;   // Wheel
int sensor_2_TRESH = 600;   // Water
int sensor_3_TRESH = 230;   // Ammonia gas

//Status of sensor (above threshold or not)
bool sensor_1_MSG = false;
bool sensor_2_MSG = false;
bool sensor_3_MSG = false;

int ammoniaTimer = 0;

void setup() {
  pinMode(sensor_1_LED, OUTPUT);
  pinMode(sensor_2_LED, OUTPUT);
  pinMode(sensor_3_LED, OUTPUT);
  pinMode(sensor_1_DATA, INPUT);
  pinMode(sensor_2_DATA, INPUT);
  pinMode(sensor_3_DATA, INPUT);
  Serial.begin(115200);
}

void loop() {
  int sensor_1_VALUE = analogRead(sensor_1_DATA);
  int sensor_2_VALUE = analogRead(sensor_2_DATA);
  int sensor_3_VALUE = analogRead(sensor_3_DATA);

  // Checks if it has reached the threshold value
  if (sensor_1_VALUE > sensor_1_TRESH) {
    if (!sensor_1_MSG) {
      Serial.print("Sensor_1: ");
      Serial.println(sensor_1_VALUE);
      sensor_1_MSG = true;
    }
    digitalWrite(sensor_1_LED, HIGH);
  } else {
    digitalWrite(sensor_1_LED, LOW);
    sensor_1_MSG = false;
  }
  if (sensor_2_VALUE > sensor_2_TRESH) {
    if (!sensor_2_MSG) {
      Serial.print("Sensor_2: ");
      Serial.println(sensor_2_VALUE);
      sensor_2_MSG = true;
    }
    digitalWrite(sensor_2_LED, HIGH);
  } else {
    digitalWrite(sensor_2_LED, LOW);
    sensor_2_MSG = false;
  }

  if (sensor_3_VALUE > sensor_3_TRESH) {
    if (!sensor_3_MSG) {
      Serial.print("Sensor_3: ");
      Serial.println(sensor_3_VALUE);
      sensor_3_MSG = true;
    }
    digitalWrite(sensor_3_LED, HIGH);
  } else {
    digitalWrite(sensor_3_LED, LOW);
    sensor_3_MSG = false;
  }

  // Send ammonia sensor value to RPi
  if (ammoniaTimer >= 6000) {
    ammoniaTimer = 0;
    Serial.print("Sensor_3i: ");
    Serial.println(sensor_3_VALUE);
  } else {
    ammoniaTimer++;
  }

  delay(10);
}
