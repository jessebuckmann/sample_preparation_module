# Reproducibility report

## Experiment/team: 
Stabilization by Mark and Stijn

## Reviewers: 
Jillis (Cavendish experiment) and Roos (Sample preperation module)
## Report 


### Disclaimer
We understand this was not an easy project to begin with. On top of that the vibration team was missing essential components, we do think they did their best with what they had and put a lot of time and effort in. Nevertheless, there are some things that can be improved upon, even without any further measurements. We did our best to give as much feed back as possible and hope it will be usefull. Good luck guys!


### Documentation:

1.	Could you understand the purpose of the experiment?

*Their purpose is to detect and filter out vibrations, as well as levelling a bed. This is a clearly defined objective and is essential if we want to carry out sensitive experiments in the modular experiment box.*

2.	Were the safety instructions clear?

*Not being drunk in the lab seems like good advice, could be phrased differently though. Otherwise, all hazards seem to be adressed.*

3.	How helpful is the documentation for reproducing the measurement?

*Not very helpful. They mention what they measured but not how. They also didn't mention where they got the setup.*

4.	Did you get stuck at some point? What extra help did you need to proceed?

*Yes, we already got stuck in the first 15 minutes. First we had to ask where the components were. They didn't mention they borrowed most of their materials, so these were not availlable to us. We came to the decision that we only wanted to test the accelerometer at hand, but when we tried this we found out that there was no ready code in their project folder. We eventually needed their assistence and their computer to test the arduino accelerometer.*

5.	Are you guided to reproduce previous measurements? How easily could you navigate through the project documentation?

*First of all, most of the essential components were missing. After communication we found out these components were borrowed from a staff member and were not availlable in short term. The exact dimensions and materials used are nowhere specified, which makes it impossible to recreate the experimental setup. The only thing that was accesible was the arduino with an accelerometer, which was not used in their own experimentents. They used a different accelerometer for their measurements that had to be returned quickly.
When trying to get the arduino working, we found out there was no code in their project folder. They did reference a library but did not mention which files of the library they used. They did not give any instructions on how they got the arduino working. In the end we used one of their laptops to test the accelerometer.
The project documentation was badly organised. Important documents and files were not easily accessible or missing. For example, instruction on how to use/construct the setup, code, materials used (insulation foam has many varieties, as do springs, nor are any dimesions specified).* 

6.	What can be improved in the documentation?

*First of all, they could have made better descriptive folder names. Also the folders could have been better structured and the files better distributed. They should have included a dedicated instruction file. Also a description of how they setup their experiments and how they obtained their measurements would have been useful. A discussion and conclusion on their bodeplots is missing other than relevance towards the modular experiment box, while there is a lot to talk about with all the different configurations tested (which ones act like low/high pass filter, does this fit with theory?). Furthermore, it would have been useful to mention their contacts.*

### Measurements:

1.	Can you operate the setup with the provided instructions? 

*No. The instructions on how to operate the setup were not included, let alone the setup itself or how to make it. Pictures alone do not suffice.*

2.	How close were the results you obtain to the previously reported results?

*We tested the accelerometer and found that it was indeed not sensitive enough. This is what their conclusion was as well. Numerical measurements were not obtained.*

3.	Can you understand and explain the analysis procedure to a third person?

*The main idea behind the setup and analysis is clear, but there are a lot of important details missing. For example, where is the uncertainty based on, how exactly is amplitude measured in relation to the driving amplitude, and whether the driving amplitude is constant or dependent on frequency.*

4.	Is the setup robust and safe to operate? 

*We don't know this because the setup was not availlable to us.*

5.	Did you encounter any issues? Could you troubleshoot those without contacting the owners?

*As described above, we ran into a lot of issues which could not be resolved without contact with the project owners.*

6.	What part of the measurement procedure did you appreciate most?

*The only thing we did was test the arduino. It was nice to see the position of the accelerometer change in real time but we soon realized the accelerometer was not sensitive enough, slow movements by hand were not detected. We can appreciate the amount of work that went into the bode plots, even though we can't varify them.*

### Interactions:

1.	Could you relate to the stated goal of the project?

*Yes, it would indeed have been useful to have vibration control and isolation in the modular experiment box. Sensitive experiments need to be free of vibrational noise. To that end, this project seems essential.*

2.	Which instructions did you need from the owners on top of the written files?

*We needed to know the location of the setup, missing parts and who to contact. Given time constraints we decided not to attempt to recreate their original setup. Next we needed their help to get usable arduino code. Lastly they pointed us to some files we completely missed and presumed missing.*

3.	Does the experiment accomplish its stated purpose?

*No, we agree with their conclusion that the accelerometer does not have the required sensitivity to perform its duty. With the the more sensitive accelerometer unaccessible we can't confirm anything else. In its current state this project will not forfill its required role in the modular experiment box. However, the measurements do indicate which dampening system works the best. This dampening system can be applied to the box anyway, even though the effect cannot be measured accurately.*

4.	What do you recommend to the project owners to improve their complete package?

*In order to get the experiment working, they could buy a more sensitive accelerometer. However, we can imagine this is too expensive. We recommend applying the best foam/spring configuration to the modular experiment box anyway to try. First, to eliminate as much of the noise as possible, even though we don't know how effective this will be. Secondly, to give the Cavendish project and future projects the necessary specifications to create a structural interface. (read: we would like to know how to attach our stuff to your dampening system)*

*We also reccomend to add more structure to your repository. Make some more directories and use more descriptive names, also for files. Adding more links would be usefull as well. For example, a link to the final rapport of your findings in the readme, and naming that file to something like "Data and discussion" or just "Rapport". And "TestRuns" to "Data" or "Measurements". Names like FirstRapport and Testruns are deceptive, they appear like intermediate results.*




