# CS361-IDEncryption-MicroService
This is a User ID and Password validation service where the User ID and Password are stored in an encrypted state.

The microservice will automatically create the text files needed to run the program, so it is completely self sufficient. All you will need to do is launch the app and the files will automatically be created. 

The three files necessary are as follows:

loginUser.txt - Input file - file preloaded with the word “waiting…”
validUsers.txt - file will contain preloaded encrypted usernames and associated passwords 
validUserResponse.txt - Communication file has three possible messages. 

The microservice handles three different scenarios: 

1.	Valid Login which is a current user and this will return the username
2.	Invalid Password which will give an error message
3.	New User which will give you a welcome message 

Note that the User ID/PW are encrypted but currently revealed as human readable for demonstration and debugging purposes.






