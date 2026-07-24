# Assessment Task 2

## Project Documentation

### Requirements Outline

#### The Need
Waking up at 2:00 AM to use the bathroom or complete other tasks, resulting in either stubbing your toe in the dark or blinding yourself by turning on the bright overhead lights.
#### The Proposed Solution
A Plug-in Nightlight system that connects directly into any standard wall outlet in your hallway, kitchen, or bathroom. The built-in light sensor ensures the device stays asleep during daylight or when overhead lights are on; when the room goes dark, the motion sensor activates to trigger a gentle, downward-facing glow for 30 seconds upon detecting movement. 

#### Key Actions
- The microcontroller checks the light sensor (LDR) to determine if the room is currently dark or bright.
- If the light sensor confirms the room is dark, the microcontroller activates and monitors the PIR sensor for any human heat.
- When the PIR sensor detects movement in the dark, the microcontroller sends a signal to turn on the plugged in night light.
- The microcontroller starts a 30-second timer the moment motion is detected, keeping the LED on for that duration, and then switches the LED off automatically once the time expires

#### Functional Requirements
- Light Sensor Input: If light levels are high (daylight or other lights on), the system must remain in sleep mode and keep the LED output off.
- Motion Sensor Input: If the room is dark and the PIR sensor detects human movement, the system must trigger the LED turning on event.
- LED Output: When there's motion detection in the dark, the LED must instantly turn on and project a gentle glow.
- Timer Control: The system must keep the LED illuminated for exactly 30 seconds after motion is detected, then automatically turn the LED off if no further movement is sensed.
- Gentle glow must be 450 lumens to keep brightness down not to affect users eyes or senses. (otherwise could get flashed)


#### Test Cases
| Test Case | Input     | Expected Output   |
|---------- |---------- |----------------   |
| Theres is other sources of light |Other light is on and then hand is waved in front of the PIR Sensor|PIR sensor should not transmit signals to the light so, no light turns on |
|There is no other source of light the room is pitch dark| Hand is waved in front in front of the PIR sensor, PIR sensor reads the motion and transmits a signal to the light| Light from nightlight turns on for 30 seconds                   |
| If Night light turns off after 30 secs if theres no movement        |  Room is dark, nightlight is triggered on, person steps out of PIR sensors view, stopwatch starts when LED light turns on            |  At exactly 30 seconds, night light dims and turns off.            |

#### Non Functional Requirements
- Response time must be 
