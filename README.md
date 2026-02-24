# Temperature Monitoring System

##  Student Details
Name: Nitu Sharma  
Roll No: 202501100700201 
Section: ECE-B  

---

##  Problem Statement

- Build a Python code to display messages according to the temperature received from an assumed IoT system.
- Accept max and min limit temperature.
- Generate random values for temperature at every 2 second interval.
- Compare with the limits to display appropriate value.

##  Approach

The program:
1. Takes input for max and min limit.
2. Stores data in variables .
3. Generates a random temperature between -273.15 and 1000.
   and then round off to two digit place .
4. Checks the rounded value of temperature .
5. Displays the appropriate messsage.

##  Sample Output

Enter minimum temperature limit: -3
Enter maximum temperature limit: 89

Monitoring Temperature...

Current Temperature: 42.62
Temperature is within acceptable limit
----------------------------
Current Temperature: 228.71
Alert: Temperature is too high
----------------------------
Current Temperature: 924.87
Alert: Temperature is too high
----------------------------
Current Temperature: -56.06
Alert: Temperature is too low
----------------------------
Current Temperature: 222.81
Alert: Temperature is too high
----------------------------
Current Temperature: 484.32
Alert: Temperature is too high
----------------------------

