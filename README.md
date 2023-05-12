# Parking Garage Simulator

This is a parking garage simulator written in Python. The simulator allows the user to manage a parking garage with a ticket system. The garage keeps track of the cars parked inside by their license plate number and the time they entered the garage.

## Requirements

The simulator requires Python 3.x to be installed on your system. No additional modules or packages are needed.

## How to Use

1. Open a command prompt or terminal window in the project directory.
2. Run the command `python parking_garage.py` to start the simulator.
3. Follow the on-screen instructions to manage the parking garage.

The simulator provides the following functionalities:

- Add a new car to the parking garage by entering the license plate number.
- Issue a ticket to a parked car, recording the time it entered the garage.
- Remove a car from the garage by entering the license plate number and paying the ticket fee.
- Display the current status of the garage, including the number of cars parked, available parking spaces, and revenue.

## Features

- The garage has a fixed number of parking spaces.
- The simulator enforces a maximum parking time for each car, after which additional fees are applied.
- The ticket fee is based on the total time the car spent in the garage.
- The garage revenue is tracked and displayed in real-time.
- The simulator prevents multiple cars with the same license plate number from parking in the garage simultaneously.

## Acknowledgements

This project was created as a Coding Temple project. Special thanks to them, and the Python community for providing excellent resources and documentation.
