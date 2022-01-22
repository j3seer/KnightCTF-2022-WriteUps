# challenge Description

Challenge Link : http://find-pass-code-two.kshackzone.com/

Flag Format : KCTF{something_here}

Note : Burte Force/Fuzzing not required and not allowed.

**Author: NomanProdhan**

-----------------------------------------------------------

Same thing as "Find pass Code - 1" we have to find the pass_code !

We also get a comment telling us the same thing
> Hi Serafin, I think you already know how you can view the source code :P

Passing the source param we get this source code : 

``` 
<?php
require "flag.php";
$old_pass_codes = array("0e215962017", "0e730083352", "0e807097110", "0e840922711");
$old_pass_flag = false;
if (isset($_POST["pass_code"]) && !is_array($_POST["pass_code"])) {
    foreach ($old_pass_codes as $old_pass_code) {
        if ($_POST["pass_code"] === $old_pass_code) {
            $old_pass_flag = true;
            break;
        }
    }
    if ($old_pass_flag) {
        echo "Sorry ! It's an old pass code.";
    } else if ($_POST["pass_code"] == md5($_POST["pass_code"])) {
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

We can see we have php type juggling here and we have to submit the md5 hash of the pass_code ! 

==> MD5 Magic Hashes !

Link to a repo with magic hashes : 

https://github.com/ryanking13/ctf-cheatsheet/blob/master/Cryptography/Useful_Hashes.md

Using this number "0e1137126905" we can bypass this bad implementation of md5 comparaisions and get our flag

``` KCTF Flag : KCTF{ShOuD_wE_cOmPaRe_MD5_LiKe_ThAt__Be_SmArT} ```
