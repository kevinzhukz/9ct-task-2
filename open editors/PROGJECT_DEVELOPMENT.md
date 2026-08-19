# Assessment Task 2

## Project Documentation

### Requirements Outline

#### The Need
Waking up at 2:00 AM to use the bathroom or complete other tasks, resulting in either stubbing your toe in the dark or blinding yourself by turning on the bright overhead lights.
#### The Proposed Solution
A Plug in Nightlight system that connects directly into any standard wall outlet in your hallway, kitchen, or bathroom. The built in light sensor ensures the device stays asleep during daylight or when overhead lights are on; when the room goes dark, the motion sensor activates to trigger a gentle glow for 30 seconds upon detecting movement. 

#### Key Actions
- The microcontroller checks the light sensor (LDR) to determine if the room is currently dark or bright.
- If the light sensor confirms the room is dark, the microcontroller activates and monitors the ultrasonic sensor to detect changes in distance caused by movement.
- When the PIR sensor detects movement in the dark, the microcontroller sends a signal to turn on the plugged in night light.
- The microcontroller starts a 30s timer the moment motion is detected, keeping the LED on for that duration, and then switches the LED off automatically once the time expires

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
Evaluate your Final Test in Relation to Functional Criteria:

Our final test was mostly successful in meeting the functional requirements of our project. The LDR was able to detect when the room was dark and the ultrasonic sensor detected movement, causing the LED to turn on. The button also allowed the system to be turned on and off, and the timer turned the LED off after 30 seconds. However, the ultrasonic sensor was sometimes less accurate when detecting small movements, so this is an area that could be improved.

****Evaluate our Final Test in Relation to Non-Functional Criteria:****

Our final test met most of the non functional requirements, including efficiency, response time and accuracy. The system was efficient because the LED stayed off when the room was bright and only activated when movement was detected in darkness. The response time was quick enough for the user to receive light when moving around at night. We also had a button to turn the system on and off which would be useful to save battery during they day when it will not be needed. However, the accuracy could be improved because the ultrasonic sensor sometimes struggled to detect slow or small movements.

****Evaluate our Final Performance in Relation to the Identified Need:****

Our final product successfully addressed the original problem of needing to move around at night without turning on a bright overhead light. When the room was dark and movement was detected, the LED provided light so the user could see where they were going. The 30 sec timer also prevented the light from staying on unnecessarily, helping to save energy. Overall, our final product provided a practical solution to the identified need, although the movement detection could be made more reliable as noted before.

****Evaluate our Project in Relation to Project Management:****

We managed the project by first identifying the problem and creating requirements before developing and testing the code and wiring. We separated the program into different functions for the LDR, ultrasonic sensor, LED and timer, which made it easier to find and fix errors. During testing, we identified problems with the sensor readings and adjusted the program to improve its performance. One area we could improve is managing our time better so we could spend more time testing different sensor values and hardware configurations.

****Evaluate our Project in Relation to Peer Feedback:****

Haven't got peer feed back yet will do after i get peer feedback

****Justify Future Improvements We Could Make to Our Final Product:****

There are several improvements we could make to our final product. The biggest hardware improvement would be replacing the ultrasonic sensor with a PIR sensor, as a PIR sensor is designed specifically to detect human movement and could be more reliable for this purpose. We could also improve the LDR by testing different light levels and selecting a more accurate value for detecting darkness. Another improvement would be making the program more efficient by allowing the sensors to continuously monitor movement while the 30s timer is running. These changes would improve the accuracy, reliability and overall effectiveness of our nightlight solution.







