# Planet Temperature Calculator
## About This Project
This project started out as a simple curiosity. One day while watching youtube I wondered how hard it would be to convert equations into code. When I finished implementing a blackbody calculator I wanted to have a way to calculate the temperature of a body with a single layer of atmosphere that absorbs all infrared radiation. With that desire came the need for a way to obtain the solar constant of a planet based upon its distance from a star.
## How to use
As of this stage in the project you will have to download the Temperature Calculator folder and open the folder in an integrated terminal (I use VScode). After doing so you can enter commands 
## Features 
To check the rule set of each feature. 
    ```
    python [file_name.py] rules
    ```
### Blackbody tmeperature
Calculating the blackbody temperature of a planet will require four inputs; The temperature of the star, the percentage of light reflected by the planet (albedo), the radius of the planet's orbit in Astronomical Units, and the radius of the star in Astronomical Units.
Valid commands are structured as such: 
    ```
    python blackbody.py blackbody [star temp here] [albedo] [R of planet orbit] [R of star]
    ```
### Simple Atmosphere
Calculating the simple atmosphere temperature of the planet requires up to two inputs; the radius of the planet's orbit in Astronomical Units, and the percentage of light reflected by the planet (albedo).
To calculate the solar constant of a planet the command would look like this:
    ```
    python simple_atmosphere.py solar\ constant [R of planet orbit]
    ``` 
For the simple atmosphere calculator a command would look like this instead:
    ```
    python simple_atmosphere.py simple\ atmosphere [R of planet orbit] [albedo]
    ```
## Upcoming features
### Greenhouse effect
This will allow for more accurate calculations of a planets temperature after being influenced by heat radiated by the planet and more precise amounts of radiation trap by the atmosphere.
### Solar panel efficiency calculator
This feature will allow for inputs of solar panel size and angle for an approximation of power output. 
