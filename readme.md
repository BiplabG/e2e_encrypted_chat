## End to end encrypted chat system
The goal of this project is to have a simple end to end encrypted chat system with following features.
1. User creation. (However user login/signup will not be implemented.)
Creation of user would mean creating public/private keys. And then registering the public key of the user in the public key db of the chain. In the public key db, the signature of the user will also be kept. 
2. A user can send text messages including the emojis to another user.
3. When a user first sends message to a new user, an exchange of public key must happen. And both the users shall verify each other's public key with the signature. 

Challenges
1. To create/store public, private key pair. 
2. How to store chat messages in the DB between the user is itself a challenge. 