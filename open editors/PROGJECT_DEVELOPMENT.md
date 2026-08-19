# Assessment Task 2

## Project Documentation

### Requirements Outline

#### The Need
Waking up at 2:00 AM to use the bathroom or complete other tasks, resulting in either stubbing your toe in the dark or blinding yourself by turning on the bright overhead lights.
#### The Proposed Solution
A Plug-in Nightlight system that connects directly into any standard wall outlet in your hallway, kitchen, or bathroom. The built-in light sensor ensures the device stays asleep during daylight or when overhead lights are on; when the room goes dark, the motion sensor activates to trigger a gentle, downward-facing glow for 30 seconds upon detecting movement. 

#### Key Actions
- The microcontroller checks the light sensor (LDR) to determine if the room is currently dark or bright.
- If the light sensor confirms the room is dark, the microcontroller activates and monitors the ultrasonic sensor to detect changes in distance caused by movement.
- When the PIR sensor detects movement in the dark, the microcontroller sends a signal to turn on the plugged in night light.
- The microcontroller starts a 30-second timer the moment motion is detected, keeping the LED on for that duration, and then switches the LED off automatically once the time expires

#### Functional Requirements
- Light Sensor Input: If light levels are high (daylight or other lights on), the system must remain in sleep mode and keep the LED output off.
- Motion Sensor Input: If the room is dark and the ultrasonic sensor detects human movement, the system must trigger the LED turning on event.
- LED Output: When there's motion detection in the dark, the LED must instantly turn on and project a gentle glow.
- Timer Control: The system must keep the LED illuminated for exactly 30 seconds after motion is detected, then automatically turn the LED off if no further movement is sensed.
- The nightlight should produce a gentle glow, providing enough light for safe movement without requiring the user to turn on the main room lights.


#### Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| Theres is other sources of light |Other light is on and then hand is waved in front of the Ultrasonic Sensor|Ultrasonic sensor should not transmit signals to the light so, no light turns on |
|There is no other source of light the room is pitch dark| Hand is waved in front in front of the Ultrasonic sensor, Ultrasonic sensor reads the motion and transmits a signal to the light| Light from nightlight turns on for 30 seconds                   |
| If Night light turns off after 30 secs if theres no movement        |  Room is dark, nightlight is triggered on, person steps out of Ultrasonic sensors view, stopwatch starts when LED light turns on            |  At exactly 30 seconds, night light dims and turns off.            |

#### Non Functional Requirements
- Efficiency:
The system should only use power when necessary. The LED should remain off when there is sufficient ambient light and should only activate when the room is dark and movement is detected.

- Response Time:
The nightlight should activate within approximately 1 second of movement being detected in a dark room.

- Accuracy:
The system should reliably detect movement when the room is dark and prevent the LED from activating when there is sufficient light or no movement.

Originally, a PIR sensor was planned to detect human movement. However, a PIR sensor was not available in the sensor section, so we decided to replace it with an ultrasonic sensor. The ultrasonic sensor detects movement by measuring changes in distance.*

#### Test Cases Evaluations
Test Case 1: Light is present

The test was successful because the LDR detected that there was enough light in the room and the LED remained off when movement was detected. We tested different light levels and checked the LDR readings to make sure the limit was working correctly. One challenge was finding an appropriate light limit because the sensor readings changed depending on the surrounding light. The program could be improved by calibrating the LDR limit more accurately so it works reliably in different environments.

Test Case 2: Dark room and Movement detected

The test was mostly successful because when the room was dark, the ultrasonic sensor detected a change in distance and the LED turned on. We tested the ultrasonic sensor by changing the distance between my hand and the sensor and adjusted the movement limit when the sensor was not detecting smaller movements. One challenge was that the ultrasonic sensor did not always detect slow or small movements accurately. The program could be improved by taking multiple distance readings and using them to make movement detection more reliable.

Test Case 3: Light turns off after 30s

The test was successful because the LED turned off after the 30s timer when no further movement was detected.We used a stopwatch to compare the programmed timer with the actual time and checked that the LED switched off after the required period. One challenge was making sure the timer did not interfere with the other parts of the program, especially when checking for further movement. The program could be improved by making the timer more accurate and allowing the ultrasonic sensor to continuously check for movement while the LED is on.


## PMI
***Plus***:

***Minus***:

***Interesting***:
## Final Evaluation




### Flow charts and Pseudocode (will paste image of flowchart and copy past pseudocode from doc)
