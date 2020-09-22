# Comparison of a system based around power bank or fully DIY solar panel power station

## Power bank

### Advantages

+ Simple system, with internal charge controller
+ more [advanced powerbanks](https://www.coolblue.nl/product/834838/goal-zero-sherpa-100-ac-powerbank-met-power-delivery-25-600-mah.html#product-specifications) even have option for 220V AC output
+ 5V USB output used for the common Arduino

### disavantage

+ less control over output voltages. (Unless load has [USB-C commmunication option](https://www.allaboutcircuits.com/technical-articles/introduction-to-usb-type-c-which-pins-power-delivery-data-transfer/#:~:text=The%20default%20VBUS%20voltage%20is,maximum%20power%20of%20100%20W) to increase voltage up to 20V)
+ Not able to use solar panel as power source directly for the load, which results in low overal power consumtion ceiling
+ Can be slow to charge, due to power input limit

## [DIY solar panel power station](https://microcontrolere.wordpress.com/2016/12/16/mppt-solar-charger/)

### Advantages
+ Extremely versatile
+ Has option to use 12V battery, which usually have higher power output ceiling
+ Use solar cell and battery as power source in parallel

### disavantage
+ Requires 50+ parts 
+ Requires a lot of testing
+ Very fragile without expert knowledge on electronics