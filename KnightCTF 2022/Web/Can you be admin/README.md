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

![1](https://user-images.githubusercontent.com/58823465/150653871-b9416477-fd8f-48d5-a963-fbc81e51f79f.png)


then we get this 

```
This page refers to knight squad home network. So, Only Knight Squad home network can access this page.
```
==>  We need to set our **Referer** header to **localhost** 

![3](https://user-images.githubusercontent.com/58823465/150653878-fc3aba21-b38a-474f-b9aa-3925794666f7.png)


Checking the source code we find a jsfuck 

![4](https://user-images.githubusercontent.com/58823465/150653901-886489ea-a192-4be5-b5b5-96887b02004a.png)

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

![5](https://user-images.githubusercontent.com/58823465/150653908-92d24f0a-058e-4c33-aa50-4bc3fda7cb83.png)


since we have an account right now we must have a cookie and we do 

```VXNlcl9UeXBl=Tm9ybWFsX1VzZXI%3D```

decoded with base64 we get 

``` User_Type=Normal_User ```

so we just need to change ```Normal_User``` to ```Admin```

 ```Admin``` in base64 is ```QWRtaW4=```

payload :
``` 
VXNlcl9UeXBl=QWRtaW4%3D
``` 
![6](https://user-images.githubusercontent.com/58823465/150653915-0aafbc27-abc0-4753-9f0f-f0576c90dff6.png)

There is our flag !

``` KCTF{FiN4LlY_y0u_ar3_4dm1N}  ```
