# Challenge description

Be Admin & get the Flag.

Website Link

Note : Burte Force/Fuzzing not required and not allowed.

Flag Format: KCTF{S0m3_T3xt_Here}

**Author: TareqAhmed**

-----------------------------------------------------------

in this challenge we find ourself in a page with 

```
Only KnightSquad agents can access this page.
```
So we need to set our user-agent header to KnightSquad using burp suite

img1

then we get to this page 

```
This page refers to knight squad home network. So, Only Knight Squad home network can access this page.
```
==>  We need to set our **Referer** header to **localhost** 

img2

img3

img4

from the jsfuck code we get this weird string 

``` F`V,7DIIBn+?CWe@<,q!$?0EpF*DPCA0<oU8RZI/DJ<`sF8 ```

which turned out to be an ascii58 encoding 

decoding it with https://www.dcode.fr/ascii-85-encoding 

we receive these credentials :
``` 
username : tareq
password : IamKnight
```
we login with the credentials and we arrive here 

img5

since we have an account right now we must have a cookie and we do 

```VXNlcl9UeXBl=Tm9ybWFsX1VzZXI%3D```

decoded with base64 we get 

``` User_Type=Normal_User ```

so we just need to change ```Normal_User``` to ```Admin```

 ```Admin``` in base64 is ```QWRtaW4=```

payload :

VXNlcl9UeXBl=QWRtaW4%3D

Scroll down and we find our flag !

``` KCTF{FiN4LlY_y0u_ar3_4dm1N}  ```
