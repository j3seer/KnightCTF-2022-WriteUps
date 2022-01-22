# Challenge description

Alex is trying to get a flag from this website. But something is wrong with the button. Can you help him to get the flag?

Note : Burte Force/Fuzzing not required and not allowed.

Flag Format: KCTF{S0M3_TEXT_H3R3}

**Author: marufmurtuza**

-----------------------------------------------------------

The website displays a **get the flag!** button but when we click the link we are redirected to 

``` http://do-something-special.kshackzone.com/gr@b_y#ur_fl@g_h3r3! ```

So we just urlencode it ! 

``` http://do-something-special.kshackzone.com/gr%40b_y%23ur_fl%40g_h3r3%21 ```

and we get our flag : 

``` KCTF{Sp3cial_characters_need_t0_get_Url_enc0ded} ```

