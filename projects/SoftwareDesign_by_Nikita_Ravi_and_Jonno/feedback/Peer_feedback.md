# Reproducibility report

## Experiment/team: 
Software Design/ Ravi, Jonno and Nikita

## Reviewers: 
Maurice, Mark and Jesse

## Report 

### Documentation:

1.	Could you understand the purpose of the experiment? 
- 1st goal. It can be done, but it is easier to do if you already have some background experience.
- 2nd goal. For Psuedo data it works, for real data we were not able to test since there was no real data available.
- 3rd goal. Not achieved.  
**1st goal: I guess once you get it up and running it is intuitive, but a little hard to install.**  
**2nd goal: It also works for the real data. Just trust us :wink:.**  
**3rd goal: Was not asked of us by anyone, although for the AD2 it is basically already implemented and just not shown.**  

2.	Were the safety instructions clear? 
- No safety instructions.  
**Dont blow up your PC and you'll be fine.**  

3.	How helpful is the documentation for reproducing the measurement?
- The documentation is good, there are some minor steps missing which could have been included. This is mainly for setting up the program. The one step we were missing was opening BIMBO. The first time we saw BIMBO we didn't quite know what it meant and what kind of file it was. After looking a bit further we saw that it was a python file so we tried to open it with python which worked.  
**Added meaning of BIMBO to the main README. Also in second README added to run the file in Spyder.**    

4.	Did you get stuck at some point? What extra help did you need to proceed? 
- Some of the lines were missing. No explanation of BIMBO. Took 10 seconds of Ravi's time.
- We tested saving some of the scanning data we obtained with the Arduino, but we were not able to browse for some unclear reason. We didn't know that we could type in the box as well and it took a while for us to find the correct filepath in order to save it. We did this with Ravi's help. For some reason the browse button does work on his PC which is weird.
- Bonus: Getting it working on the Mac took some more time, but this was not tested before. The fact that it worked in the end was very nice. Once it was running it actually worked better than it did on a windows, in the sense that the python code didn't crash when using it multiple times.   
**First point, see above. I think you mean browse with the AD2, but we were not able to reproduce this. For more info see your other feedback file. Nice bonus.**  

5.	Are you guided to reproduce previous measurements? How easily could you navigate through the project documentation?
- Yes we are guided to reproduce measurements, the instrucions for the measurements where very clear. The one change we would make is to add the information about how to find the COM to the same point as filling in the COM. This would make it clearer. 
- Navigation was very easy due to the high number of links.  
**Changed the thing about the COM.**  

6.	What can be improved in the documentation?
- Describing acronyms. Make one big readme rather than 2, because the installation instructions were included in a seperate folder while they could be in the same one. See also [feedback notes](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/patch-18/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/feedback/FromOthers.md)
- In order to make it more suitable for people without any coding experience include small explanations, e.g. how to comment. The three of us don't quite know how we would start with an additional sensor or any form of contributing. Maybe elaborate on this slightly more under the contributing (mainly a question of us not being very familiar with Arduino), if that is your focus. If you only want contributions from people that fully understand how to encode it then it is fine.  
**Acronyms described. If we merge both READMEs it will get very big. Also, we want to keep general information about the project seperated from info about installing. That's why there is 2, and we think it is a bit clearer. We think our target group should be able to google things like how to comment in Spyder. If you really do not know any programming, we can install the program on your pc and you only have to press a button to start. In the future it would certainly be nice to make the program and executable. We think if you want to contribute, you should already know a little bit as we cannot explain everything. However, people are always free to shoot us a message on teams, we added this to the contributing file.**  

### Measurements:

1.	Can you operate the setup with the provided instructions? 
- Yes after the initial set-up we could easily perform the measurement. Not a real measurement so there is not much that can go wrong.  
**Good.**  

2.	How close were the results you obtain to the previously reported results?
- Results are same, except for different scanning times. 
- Some functionality issues occured such as only being able to run the code once in Python after having to reboot python, maybe this can be solved with pycharm we have not tried this. Or the issue of not being able to browse in our case.   
**For the issue, see the other feedback file.**  

3.	Can you understand and explain the analysis procedure to a third person?
- Yes we could.  
:thumbsup:  

4.	Is the setup robust and safe to operate? 
- Safe to operate. As mentioned before python does a little weird sometimes. There was also a random issue where the pressure measurement didn't work once, issue still not clear.  
**Yeah python is weird.**  

5.	Did you encounter any issues? Could you troubleshoot those without contacting the owners?
- Yes we could solve the issues ourselves. It was a matter of finding the right files. 
- (SPYDER BUG: One time use.)
- We couldn't solve the browse issue ourselves, but if in the instructions it is included that you can type it yourself this would be resolved.
- Random issue with pressure measurement is not clear. Starting the programme again removed this error.  
**Added extra instruction on the browse/textbar. Not sure about that third point. Random things happen and hard to fix if not reproducible. The one time use issues is probably related to Spyder, but not on every pc so hard to actually fix.**   

6.	What part of the measurement procedure did you appreciate most?
- We liked the colours in the graphs. Time well-spend on user interface.
- We also appreciated the fact that the explanations were very clear. The steps were typically easy to follow. The user interface was also nice.    
:fire: :fire: :fire:  

### Interactions:

1.	Could you relate to the stated goal of the project?
- It was not intuitive for people without experience. Some of the set-up can be solved with additional lines of codes.
- Contributing is even less intuitive, we would not know how to add an additional sensor even after we have already used the set-up and have some background knowledge about programming.
- We can relate to wanting to be able to measure something so this goal is very relatable and wanting to make your programme as easy to use as possible is also a good idea.  
**We think our main goals was to make the actual program intuitive and not necessarily the downloading etc. It would be nice to make this into an executable however. Ravi should probably just give away his laptop together with the box. For contributing, the only way to really know how it works is to dig through the code. \#relatable.**  

2.	Which instructions did you need from the owners on top of the written files?
- Instructions on how to install on Mac, there were no instructions for this yet since they hadn't tried it yet. Addition is also in the [feedback notes](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/patch-18/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/feedback/FromOthers.md).
- Save file would not have worked without the help of Ravi.  
**Added some Mac instructions. We do not know which save file you mean exactly. But for the AD2 browse it was just an unknown bug. For the arduino it is annoying that you cannot see that it is scanning, but we will try to add this. This was however described in the README.**  


3.	Does the experiment accomplish its stated purpose?
- Not entirely not intuitive for people without experience. The measurement itself did work which is nice. I do think it will be interesting to see how well it is going to work once it gets hooked up to all the other systems in the box and real data is provided.  
**Yeah see above for more explanation on the intuitiveness of the program.**  


4.	What do you recommend to the project owners to improve their complete package?
- Add some small additional instructions to clear up the steps that were a bit vague for us. (Also inlcude how to comment something, people without experience would not know how to comment. If you really aim for the programme to be useable by everyone.)
- Add guidelines and information on how to add an additional senser. This is for the contributing section, if this is the aim.
- Enable the user to see when you are scanning.
- Change to Pycharm if this indeed solves the problem of having to reboot SPYDER of having to replug the arduino.
**See above for a reaction on how to comment. For the sensor part, added that you can contact us for more information if you do not have any experience at all. The Arduino scanning thingy will be implemented. Changing to Pycharm would indeed solve some issues probably, but would further complicate the installation. Might do this in the future (next year haha).**  

### General remarks

The reproduction was well explained, all three of us were dreading the software design reproduction at first, but the steps are very clear. We could do the reproduction pretty well.
A job well done on the project. For us the explanation was clear with some small parts missing at some points. A few helpful comments from Ravi helped us through. The fact that it also worked on Mac is pretty nice, without having tested this first. 
We don't know how well it works with actual data, and if it is compatable with the systems used by the other groups.   
:heart: :heart: :heart:

