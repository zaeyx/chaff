chaff
=====
This proof of concept demonstrates the idea behind chaff.

Password policy doesn't always stop users from picking horrible passwords.

Chaff cloaks the password hash of the user among tons of other hashes.  All hashes work to authenticate the user, but all the hashes other than the one containing the users chosen password are randomly generated to be computationally unfeasible to crack.

In this way, all the hashes working means there is no indication of which one is the user's chosen password.  The user's chosen password is the only one possible to crack.

Assume an attacker properly guesses (or knows) that the user's password is four characters lower-alpha. An exhaustive search attack on this password is completely feasible at 26^4!

Chaff camouflages this weak hash in a field of 26^4 passwords.  Now to do an exhaustive search the attacker must try 26^4 on every one of these hashes (26^4*26^4=26^8).  

Without changing anything about the hash we have made the incredibly weak password as hard to crack as an 8 character password.

The trade off comes in hard disk space, the current password files take 14mb of space on the hard drive (for 128 bit md5 hashes saved as 32 bytes each).  I am planning on finding a new way to cut down on this. 

Enjoy this proof of concept!
