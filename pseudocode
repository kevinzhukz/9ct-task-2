Main:
BEGIN Main
    WHILE TRUE
        Read Light Sensor
        IF Room is Dark THEN
            Read Motion Sensor
            IF Motion Detected THEN
                Call Activate_Light
                Call Run_Timer
            ELSE
                Call System_Sleep
            END IF
        ELSE
            Call System_Sleep
        END IF
    END WHILE
END Main
Subroutines:
Activate_light:
BEGIN Activate_Light
    Set LED brightness to required level
    (450 lumen target)
    Turn LED ON
END Activate_Light

System_Sleep:

BEGIN System_Sleep
    Turn LED OFF
    Enter Low Power Mode
END System_Sleep

Run_Timer:
    BEGIN Run_Timer
    Start 30 second countdown
    WHILE Timer < 30 seconds
        Maintain LED ON
    END WHILE
    Turn LED OFF
END Run_Timer
