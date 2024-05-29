# Workshop 3 - Solution

This is a workshop related with a backend system to provide a vehicles catalog using python and patterns design.

## Requirements

The requirements for this workshop are presented as follows:
- Application is not registering in a good way the actions of users. Check why is this failing and fix it.
- There are just test cases for engines sub-system. You should add tests for all the other modules.
- Check for code smells across the code, use pylint is a good idea. However, it is not enough, you must fix all the issues found after make a code review.
- Code should be good formated and with the best comments you could write/update from the code.
- Check the logs in order to figure out the functionalities with bad performance, and fix them.
- Add a new feature to the application, now it should be able for users to be subscribed
to a newsletter using an email. The newsletter should be sent by the admin anytime he/she wants, just with the information with the last five vehicles created (if there are less than five, just sent the complete catalog).
- Cache memory is still do not implemented. It means, the last three searches made in
the system shloud be saved into memory just to avoid make the same search again. Every time a vehicle is added, this memory should be shuffed.
- Maybe an admin could make an error. So, provide an option to recovery the last vehicle deleted.
- Add a new type of engine: a hybrid engine. This engine should have a new attribute: electric_power (in Watts). The values for attributes of this new engine type will be defined by you but in the middle of the values of the other engines.
- Implement a set of validations for the vehicles created. It means, a vehicle should
have a valid model name (less than 30 characters, and just numbers and letters),a valid year (between 1990 and 2025), a valid price (between 20000000 COP and 500000000 COP), and a valid chassis (A or B).


## Business Rules

- The administrator sends newsletters 
- Prices of the vehicles should be between 20000000 COP and 500000000 COP
- Vehicle year must be between 2025 and 1990.
- Vehicle chasis must be A or B