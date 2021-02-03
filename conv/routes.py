# Route 1: Fetch last x messages of the conversation with a friend
"""Given a username, fetch last x messages from the conversation with a friend."""
"""NOTE: I think a message has to be stored twice. 
Because the messages have to be encrypted for the reference of the sender, 
she has to store the message separately.
And it is going to be stored in the recipient as well."""

# Route 2: Send a new message to a user
"""If the user is conversing for the first time, first verify the public key. 
Encrypt the message and send to the user."""

# Route 3: 