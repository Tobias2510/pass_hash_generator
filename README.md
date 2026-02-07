# Pass_Hash_Generator

## Purpose:

The goal is to minimize social media usage, by generating a random unknown password of a fixed length that the user can set as his
password for social media apps. The user will only get the corresponding sha3 256 hash.
To find out the password, the user has to "crack" the hash by using some tool like `hashcat` or a self written program.

## Reason:

The reason behind is that no matter how hard humans try to fight their social media addiction it usually does not work.
That is because most social media apps are very addicting and to fight it people often try to block the app or use some app blocker apps.

### The problem:

The main problem is that setting an app password often doesnt work, because the user knows the password or the user can disable the app blocker.
Most of the time this leads to a spiral, where you only make your access to social media a bit harder due to the extra steps of disabling the password or blocker.

### The solution:

By setting a unknown, randomized password it is impossible for the user to reset the app blockage, (exept he implements some password reset...) and because
of the sha3 256 hash, the user is able to find out his password, by "cracking" the hash. It is a basic "proof of work" concept.
The user cannot find out the password without putting in compute power and by adjusting the length of the password the user can set his "timer".
The whole process is limited by hardware and time, so there is no way for the user to "cheat" by finding out the password by using some other method.
