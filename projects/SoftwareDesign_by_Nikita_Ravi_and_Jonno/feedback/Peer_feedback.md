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
2.	Were the safety instructions clear? 
- No safety instructions.
3.	How helpful is the documentation for reproducing the measurement?
- The documentation is good, there are some minor steps missing which could have been included. This is mainly for setting up the program. The one step we were missing was opening BIMBO. The first time we saw BIMBO we didn't quite know what it meant and what kind of file it was. After looking a bit further we saw that it was a python file so we tried to open it with python which worked.
4.	Did you get stuck at some point? What extra help did you need to proceed? 
- Some of the lines were missing. No explanation of BIMBO. Took 10 seconds of Ravi's time.
- We tested saving some of the scanning data we obtained with the Arduino, but we were not able to browse for some unclear reason. We didn't know that we could type in the box as well and it took a while for us to find the correct filepath in order to save it. We did this with Ravi's help. For some reason the browse button does work on his PC which is weird.
- Bonus: Getting it working on the Mac took some more time, but this was not tested before. The fact that it worked in the end was very nice. Once it was running it actually worked better than it did on a windows, in the sense that the python code didn't crash when using it multiple times. 
5.	Are you guided to reproduce previous measurements? How easily could you navigate through the project documentation?
- Yes we are guided to reproduce measurements, the instrucions for the measurements where very clear. The one change we would make is to add the information about how to find the COM to the same point as filling in the COM. This would make it clearer. 
- Navigation was very easy due to the high number of links.
6.	What can be improved in the documentation?
- Describing acronyms. Make one big readme rather than 2, because the installation instructions were included in a seperate folder while they could be in the same one. See also [feedback notes](https://git.science.uu.nl/ued2020/experiment-design-2020/-/blob/patch-18/projects/SoftwareDesign_by_Nikita_Ravi_and_Jonno/feedback/FromOthers.md)

### Measurements:

1.	Can you operate the setup with the provided instructions? 
- Yes after the initial set-up we could easily perform the measurement. Not a real measuerment so there is not much that can go wrong.
2.	How close were the results you obtain to the previously reported results?
- Results are same, except for different scanning times.
3.	Can you understand and explain the analysis procedure to a third person?
- Yes we could.
4.	Is the setup robust and safe to operate? 
- Save to operate, not very robust yet, could use some little tweaks.  
5.	Did you encounter any issues? Could you troubleshoot those without contacting the owners?
- Yes we could solve the issues ourselves. It was a matter of finding the right files. 
- (SPYDER BUG: One time use.)
6.	What part of the measurement procedure did you appreciate most?
- We liked the colours in the graphs. Time well-spend on user interface.

### Interactions:

1.	Could you relate to the stated goal of the project?
- It was not intuitive for people without experience. Some of the set-up can be solved with additional lines of codes.
- Contributing is even less intuitive, we would not know how to add an additional sensor even after we have already used the set-up and have some background knowledge about programming.
2.	Which instructions did you need from the owners on top of the written files?
- Instructions on how to install on MAC.
- Save file would not have worked without the help of Ravi.
3.	Does the experiment accomplish its stated purpose?
- Not entirely not intuitive for people without experience.
4.	What do you recommend to the project owners to improve their complete package?
- Add some small additional instructions to clear up the steps that were a bit vague for us. Also inlcude how to comment something, people without experience would not know how to comment.
- Add guidelines and information on how to add an additional senser. This is for the contributing section. 

### General remarks

The reproduction was well explained, all three of us were dreading the software design reproduction at first, but the steps are clear. We could do the reproduction pretty well.
A job well done on the project. For us the explanation was clear with some small parts missing at some points. A few helpful comments from Ravi helped us through. The fact that it also worked on Mac is pretty nice, without having tested this first. 
We don't know how well it works with actual data. 


