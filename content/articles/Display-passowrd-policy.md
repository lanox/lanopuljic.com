Title: Display passowrd policy message.
Date: 2014-05-19 09:36:56 +1000
Category: Articles
Tags: linux
Author: Lano
Image:
Email: lanox.post@gmail.com
Summary: Display password policy when asked to change password

Echo service module for PAM can be used to displays it's policy to users for the new password.

####We need to create a message that you would like to display to users.

If file doesnt exist you just create a new file.

```bash 
vi /etc/issue.password
```

Create a displayed message to users, and add it to ```/etc/issue.password```

My example below.

```bash
  ************************************************************************************
  *  Minimum of 8 characters which MUST consist of AT LEAST the following:           *
  *                                                                                  *
  *   - Minimum of 4 lowercase characters                                            *
  *   - Minimum of 2 uppercase characters                                            *
  *   - Minimum of 1 decimal number                                                  *
  *   - Minimum of 1 non-alphanumeric character (i.e. special characters: eg: !@#$%) *
  *                                                                                  *
  ************************************************************************************
```

Edit ```pam.d/passwd file.```

Add the following line ```password optional pam_echo.so file=/etc/issue.passwd```
between ```account include system-auth``` and ```password substack system-auth```

It should look something as below.

```bash
account    include      system-auth
password   optional     pam_echo.so file=/etc/issue.passwd
password   substack     system-auth
```

If you done everything correctly once you try change the password for a user or if the user is prompted to change the password he/she should be prented with somehing like this.

```bash
[root@test ~]# passwd test
```
Changing password for user ```test```.
```
****************************************************************************************
*   Minimum of 8 characters which MUST consist of AT LEAST the following:              *
*                                                                                      *
*       - Minimum of 4 lowercase characters                                            *
*       - Minimum of 2 uppercase characters                                            *
*       - Minimum of 1 decimal number                                                  *
*       - Minimum of 1 non-alphanumeric character (i.e. special characters: eg: !@#$)  *
*                                                                                      *
****************************************************************************************
```
