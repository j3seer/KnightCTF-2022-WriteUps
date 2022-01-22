# Challenge description

One of my friend developed this login panel and dared me to get the flag by logging in. I tired to bruteforce the login panel. But it doesn't work at all. Can you please figure out the login credentials or something more valuable for me?

Website Link

Flag Format: KCTF{S0M3_TEXT_H3R3}

**Author: marufmurtuza**
-----------------------------------------------------------

The website displays a login page and in the source code we find what appears to be a jsfuck obsfucated js code
So we just need to decode it 

```
([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[+[]]+(+[![]]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+!+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[+!+[]+[!+[]+!+[]+!+[]]]+([][[]]+[])[!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+[]]+((+[])[([][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+(![]+[])[!+[]+!+[]]+(![]+[])[+!+[]]+(!![]+[])[+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![...........
```
**Decoded** : 

```  
if (document.forms[0].username.value == "83fe2a837a4d4eec61bd47368d86afd6" && document.forms[0].password.value =="a3fa67479e47116a4d6439120400b057") 
    document.location = "150484514b6eeb1d99da836d95f6671d.php"
```

Using those credentials to login we get our flag 

``` KCTF{0bfuscat3d_J4v4Scr1pt_aka_JSFuck} ```
