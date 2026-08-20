BEGIN Main
    WHILE TRUE
        Check ON/OFF Button
        IF System is ON THEN
            Read Light Sensor
            IF Room is Dark THEN
                Read Ultrasonic Sensor
                IF Motion Detected THEN
                    Call Activate_Light
                    Call Run_Timer
                ELSE
                    Call System_Sleep
                END IF
            ELSE
                Call System_Sleep
            END IF
        ELSE
            Call System_Sleep
        END IF
    END WHILE
END Main

Activate_Light:

BEGIN Activate_Light
    Turn LED ON
END Activate_Light

System_Sleep:

BEGIN System_Sleep
    Turn LED OFF  #keep system waiting
END System_Sleep

Run_Timer:
    BEGIN Run_Timer
    Start 30 second countdown
    WHILE Timer < 30 seconds
        Maintain LED ON
    END WHILE
    Turn LED OFF
END Run_Timer
