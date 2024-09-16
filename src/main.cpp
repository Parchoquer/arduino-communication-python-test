#include <Arduino.h>

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        String cmd = Serial.readStringUntil('/n');

        if (cmd == "get_temp") {
            Serial.println(String(random(0, 100)));
        } else if (cmd == "get_hygro") {
            Serial.println(String(random(0, 100)));
        } else {
            Serial.println(cmd);
        }
    }

    // Serial.println(String(random(0, 100)));
    // delay(1000);
}
