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
- When the Ultrasonic sensor detects movement in the dark, the microcontroller sends a signal to turn on the plugged in night light.
- The microcontroller starts a 30s timer the moment motion is detected, keeping the LED on for that duration, and then switches the LED off automatically once the time expires

#### Functional Requirements
- Light Sensor Input: If light levels are high (daylight or other lights on), the system must remain in sleep mode and keep the LED output off.
- Motion Sensor Input: If the room is dark and the ultrasonic sensor detects human movement, the system must trigger the LED turning on event.
- LED Output: When there's motion detection in the dark, the LED must instantly turn on and project a gentle glow.
- Timer Control: The system must keep the LED illuminated for approximately 30s (maybe one second difference +-1s) after movement is detected. If further movement is detected while the LED is on, the 30s timer should restart. If no further movement is detected, the LED should automatically turn off.
- The nightlight should produce a gentle glow, providing enough light for safe movement without requiring the user to turn on the main room lights.



#### Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| Theres is other sources of light |Other light is on and then hand is waved in front of the Ultrasonic Sensor| The ultrasonic sensor may detect movement, but the LED should remain off because the LDR detects that there is enough light. |
|There is no other source of light the room is pitch dark| Hand is waved in front in front of the Ultrasonic sensor, Ultrasonic sensor reads the motion and transmits a signal to the light| Light from nightlight turns on for 30 seconds                   |
| If Night light turns off after 30 secs if theres no movement        |  Room is dark, nightlight is triggered on, person steps out of Ultrasonic sensors view, stopwatch starts when LED light turns on            |  At approximately 30 seconds, night light turns off.            |

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

The test was mostly successful because when the room was dark, the ultrasonic sensor detected a change in distance and the LED turned on. We tested the ultrasonic sensor by changing the distance between Alfonso's hand and the sensor and adjusted the movement limit when the sensor was not detecting smaller movements. The program could be improved by taking multiple distance readings and using them to make movement detection more reliable.

Test Case 3: Light turns off after 30s

The test was successful because the LED turned off after the 30s timer when no further movement was detected.We used a stopwatch to compare the programmed timer with the actual time and checked that the LED switched off after the required period. One challenge was making sure the timer did not interfere with the other parts of the program, especially when checking for further movement. The program could be improved by making the timer more accurate and allowing the ultrasonic sensor to continuously check for movement while the LED is on.


## PMI Table



|Name   | Plus | Minus     | Implication |
|---------- |---------- |---------- |----------------   |
|Mrigaank Sodhi | All wiring worked well with no errors, and all sensors achieved their purpose in detecting the stimulus which solved their original problem flawlessly. | There was no solution if there was an accidental turn on, such as a button to turn it off. | A working button to turn the system on and off when there is an unneccessary turn on.
Zach Timbrell| Good comments and understandable code, all wires and sensors worked immaculately.| It doesnt have different brightness levels and colours |Switiching the colour of the light and maybe experimenting with the brightness of the levels.|
Fayaaz Kabir| The LDR and ultrasonic sensor worked well together to detect darkness and movement, and the LED turned on when both conditions were met. The wiring was also successful and the system was able to run as intended. | The LED only had one brightness level.| A dimmer or different LED could also be added to allow different brightness levels so the light is more comfortable to use at night.   |



Final Evaluation
Evaluate our Final Test in Relation to Functional Criteria:

Our final test was mostly successful in meeting the functional requirements of our project. The LDR was able to detect when the room was dark and bright, although the readings sometimes changed depending on the surrounding light. When the room was dark, the ultrasonic sensor was able to detect movement by measuring changes in distance and the LED turned on as expected. The LED also remained off when there was enough light in the room, which showed that the LDR and ultrasonic sensor worked together to control the nightlight. We also proved the 30sec timer also worked successfully by using a stopwatch to measure the time. It turned the LED off after the required amount of time when no further movement was detected. When further movement was detected while the LED was on, the timer could restart, allowing the light to remain on while the person/hand was still moving. and the LDR readings were sometimes inconsistent. These issues meant that the system did not work perfectly in every situation, but it still met most of the functional requirements.

Evaluate our Final Test in Relation to Non-Functional Criteria:

Our final test met most of the non functional requirements, including efficiency, response time and accuracy. The system was efficient because the LED remained off when there was enough surrounding light and only activated when movement was detected in a dark room. This reduced unnecessary energy use because the LED was not constantly operating. The response time was also quick enough for the user to receive light soon after movement was detected, making the nightlight suitable for someone moving around at night. The accuracy was mostly successful, although the LDR sometimes gave different readings depending on the surrounding light and the ultrasonic sensor could struggle with smaller or slower movements. These problems reduced the reliability of the system in some situations. Overall, the final test showed that the nightlight was efficient and responsive, but its accuracy could be improved through better sensor calibration and more reliable movement detection.

Evaluate our Final Performance in Relation to the Identified Need:

Our final product successfully addressed the original problem of needing to move around at night without turning on a bright light. When the room was dark and movement was detected, the LED provided enough light for the user to see where they were going without needing to turn on the main room lights. This created a more comfortable solution because the light was only activated when it was needed. The 30s timer also helped prevent the LED from staying on unnecessarily, which improved the efficiency of the product. The use of the LDR meant that the system could remain inactive when there was already enough light in the room. I think the final product provided a practical solution to the identified need and demonstrated that the main idea of an automatic nightlight was successful.

Evaluate our Project in Relation to Project Management:

We managed the project by first identifying the problem, developing requirements and planning how the sensors, microcontroller and LED would work together. We then developed the pseudocode and flowcharts before creating and testing the program and wiring. During development, we tested the LDR and ultrasonic sensor and identified problems with their readings. We adjusted the light limit and movement limit to improve the performance of the system. We also tested the 30-second timer to make sure the LED switched off correctly and tested the system under different lighting and movement conditions. Separating the program into different functions for the LDR, ultrasonic sensor, movement detection, LED and timer made the code easier to understand and helped us identify and fix problems. One area we could improve in our project management was time management. More time could have been spent testing different sensor values and hardware configurations, which may have improved the accuracy and reliability of the final product.

Evaluate our Project in Relation to Peer Feedback:

Based on the peer feedback we received, our project had several strengths as well as areas that could be improved. A positive was that the LDR and ultrasonic sensor worked together to detect darkness and movement, allowing the LED to turn on when required. The wiring and code also worked well for most of the testing. However, the feedback identified that the LDR readings could change depending on the surrounding light, and the LED only had one brightness level. One suggestion from the feedback was to add a button that would allow the user to manually turn the system on and off. We agreed with this feedback because a button would give the user more control over the nightlight and allow it to be switched off when it is not needed. The feedback also supported the problems we identified during our own testing. Overall, the peer feedback helped us identify useful improvements that could make our nightlight more reliable, convenient and easier to use.

Justify Future Improvements We Could Make to Our Final Product:

There are several improvements that could be made to our final product. The biggest hardware improvement would be replacing the ultrasonic sensor with a PIR sensor because a PIR sensor is specifically designed to detect human movement and could provide more reliable movement detection. This would reduce the problem of the ultrasonic sensor missing small or slow movements. The LDR could also be improved by testing a wider range of lighting conditions and calibrating the light limit more accurately. This would make the system better at determining when the room is actually dark and reduce unnecessary activation of the LED. Another improvement would be adding different brightness levels to the LED so that the user could have a softer light at night while still having enough brightness to see safely. On the software side, the movement detection could be improved by taking multiple sensor readings and comparing them to reduce inaccurate readings. These improvements would increase the accuracy, reliability, efficiency and comfort of the nightlight and would make it a more effective solution to the original problem.