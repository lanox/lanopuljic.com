Title: Alert by email when server is up and running
Date: 2014-05-19 09:36:56 +1000
Category: Linux
Tags: linux,bash
Author: Lano Puljic
Email: lano.puljic@gmail.com

If you are lazy like me to wait for server to come back after a reboot, but would like to be notify when it does here is the simple one liner commend that will save you.

```bash
while ! ping -c1 the_host_down; do sleep 1; done && date | mail -s 'the host is back!' youname@iamawesome.com
```
