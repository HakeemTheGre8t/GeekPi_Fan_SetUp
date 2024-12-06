# GeekPi_Fan_SetUp

EKKOGrid: Raspberry Pi Fan Control System and Custom Retro Gaming Console


Overview:

EKKOGrid is a Raspberry Pi-based project that integrates a custom automated fan control system to regulate CPU temperature, alongside configurations for a personalised retro gaming console. This project combines hardware, Python scripting, and Linux system configuration to deliver an optimised, real-world solution for thermal management while setting the stage for a retro gaming experience.



Features Achieved

1. Fan Control System:

• Automated Cooling: The fan turns ON when the CPU temperature exceeds 50°C and OFF when it drops below 40°C.

• Real-Time Temperature Monitoring: The Python script uses psutil to read CPU temperature and control GPIO pins to manage fan activity.

• Startup Automation: Configured to start automatically at system boot using /etc/rc.local, eliminating the need for manual script execution.



2. Hardware Integration:

• Raspberry Pi’s GPIO pins are used for fan control, integrated into the GeekPi DeskPi Lite case for a seamless setup.

• Custom cooling thresholds are implemented to ensure efficient temperature regulation.



3. Custom Splash Screen:

• A personalised splash video has been added to the Batocera folder, creating a unique boot-up experience.

• The splash screen reflects the retro gaming theme and enhances the console’s presentation.



4. Real-Time Testing:

• Fan behaviour and temperature monitoring were manually verified using Linux commands (e.g., cat /sys/class/thermal/thermal_zone0/temp).

• Ensured script functionality and GPIO responsiveness during development and deployment.



Planned Additions

To further enhance the EKKOGrid system, the following features are planned:

1. Error Handling:

• Implement robust error handling for edge cases, such as:

• Unreadable temperature sensors.

• GPIO pin setup issues.

• Example:

try:  
    temp = get_cpu_temp()  
except KeyError as e:  
    print(f"Error reading temperature: {e}")  
    # Exit or retry logic  




2. Logging:

• Add logging to record temperature readings and fan status for debugging and analysis:

• import logging  

• logging.basicConfig(filename='/userdata/system/fan_control.log', level=logging.INFO)  

• logging.info(f"Temperature: {temp:.2f}°C, Fan Status: {'ON' if fan_status else 'OFF'}")  



3. Custom Retro Gaming Console:

• Complete EKKOGrid’s transformation into a fully functional retro gaming console using Batocera.

• Integrate a library of retro games with customisable game stats tracking, such as high scores and playtime.


4. Web-Based Monitoring Dashboard:

• Develop a lightweight web app to monitor real-time CPU temperature and fan status, accessible via the Raspberry Pi’s local network.



Installation and Usage

Prerequisites:

• Raspberry Pi with GPIO support.

• GeekPi DeskPi Lite case with an attached fan.

• Python libraries: RPi.GPIO and psutil.



Steps:
1. Clone the Repository:
• Ensure the fan control script is placed in the /userdata/system directory.

2. Make the Script Executable:
• Use chmod +x /userdata/system/fan_control.py to make the script executable.

3. Configure Startup:
• Add the following line to /etc/rc.local:

/usr/bin/python3 /userdata/system/fan_control.py &  


4. Reboot and Test:
• Restart the Raspberry Pi and verify the fan behaviour.


Future Configurations for EKKOGrid

• Custom ROM Library Setup: Finalise the ROMs and emulator settings in Batocera for seamless retro gaming.

• UI Enhancements: Improve the user interface with themed backgrounds and animations that align with the EKKOGrid branding.

• Additional Hardware Features: Integrate LED indicators or a small display for live CPU stats and fan activity.



Project Significance

The EKKOGrid project showcases my ability to:

• Build hardware/software integrations with Python and Raspberry Pi.

• Automate processes using Linux system configuration.

• Solve real-world problems through scripting and testing.

• Extend project functionality with planned upgrades, such as error handling, logging, and UI enhancements.

This project reflects my growth as an embedded developer, combining technical skills with creativity and problem-solving.