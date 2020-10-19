# Reproducibility report

## Experiment/team: 
Sample preparation box by Roos and Jesse

## Reviewers: 
Mikita, Floris

## Report 

### Documentation:

1.	Could you understand the purpose of the experiment? Explain.
- The purpose itself is quite clear: make a well-ventilated and chemically resistant box, such that it functions as a small and lower-budget fumehood, which fits in the larger experiment box.

2.	Were the safety instructions clear?
- Instructions on prevention itself were clear, most notably on the preventive equipment one should wear while working with acids.
- When working with potentially dangerous chemicals, one should add instructions on what to do if something goes wrong, e.g. when you spill on your skin. Currently, this is missing. However, this is presumed to be not a major safety issue since the instructions state these tests need to be carried out under supervision.
- Apparently, the safety instructions of the power supply group mentions the possibility of the battery exploding if it is short-circuited. When simply connecting the two wires of the fan, we presume the risk of exploding is non-existent if you connect the wires normally, but perhaps it is good to mention this explicitly to avoid suprises.

3.	How helpful is the documentation for reproducing the measurement?
- Starting from the readme, it is not so clear where to begin with the peer-reviewing. Rather, one has to manually navigate the repo to find the file, altough the folder name
- The instruction document by itself is not enough to reproduce the experiment, and has to be supplemented by a log of sorts of earlier measurements. 
- It is quite inconvenient that part of the instructions for the coating testing are in the instruction file (i.e. the pipetting tutorial), and that the other part is in the testing directory (i.e. the details on the chemicals whose influence was examined). However, despite the missing quantities of 'spilled' material that were analyzed, the information in these two files combined gives a good overview of what was done and how it could be reproduced. 
- For the airflow measurements, details such as the exact location of measurement spots and whether the window should be open or closed were sometimes not so clear (see also question 2 under measurements).
- The file for the building process is not mentioned in the reproduction guide, such that one has to browse through the repo oneselve, while this is imformation is quite important if someone wants to get an idea of what you have been doing (even if the idea is to not redo the entire building process). The building process file itself does give a nice overview of the building process.

4.	Did you get stuck at some point? What extra help did you need to proceed?
- The battery from the power supply group was required to get the fan running, and thus required for the airflow measurments. However, the battery was in use for the peer-reviewing power supply group. Eventually, the battery became available so we were able to repeat the measurements. This possibility was not mentioned in the documentation, and an alternative power source (12V battery) was not provided.

5.	Are you guided to reproduce previous measurements? How easily could you navigate through the project documentation?
- Starting from the readme file of the project folder, one is guided more towards an understaning of the project goals. When following the peer-review instructions, one is guided towards the testing documentation, but not towards the building process documentation. 
- The structure of the repository itself is quite simple and therefore quite easy to navigate through, partially helped by the use of cross-references in both the readme and the instruction, altough a link in the former to the latter would make a fine addition.

6.	What can be improved in the documentation?
- Link to peer instructions in the readme file.
- Explicitly mention and refer to the documentation on the building process in the instruction.
- Be sure that measurement details make sense not only to you, but also to the general audience. In the case of measurement spots in the box, an illustration might help clear the view on this point.

### Measurements:

1.	Can you operate the setup with the provided instructions? 
- Mostly yes. Setting up the box for measurment is straightforward and adequetly described. The testing of the coating was deemed very much possible when acces to a lab and adequate supervision is acquired. Repetition of air flow measurements was also possible, save for some details that were not entirely resolved. While not attempted, it was deemed possible to build the box itself based purely on the building process description.

2.	How close were the results you obtain to the previously reported results?
- As of Monday (12/10), we were not able to repeat the coating testing since we did not have access to a chemical lab. The indicated contact person (Jesper Moes) was contacted on this Monday, and we will try to repeat the experiment before Thursday 15/10.
- Below are our air flow measurements compared to the ones reported by the project owners. As mentioned, sometimes the details were not entirely clear, and one of the anemonitors was not present. As may be seen, results largely agree, with significant deviation at a handful of measurement spots. This may also be due to aforementioned confusion on the exact nature of the measurements

|position|windspeed (m/s) provided by experiment group|windspeed (m/s) measured by peer reviewers|
| ------ | -------- | -------- |
|in the room we were measuring in| 0.00|0.00|
|sides of the box without ductape| 0.00|(1)|
|sides of top window|0.00|0.00|
|sides of front window|0.00|0.00|
|end of the pipe (testo)| 1.60|0.43 (window closed), 1.01 (window open) (2)|
|end of the pipe (kaindl)| 1.7|(3)|
|end of the pipe (travel&co)| 1.6|0.50 (window closed), 1.4 (window open) (2)|
|front of sash while fully opened|0.20|0.19|
|front of sash when almost closed|1.12|0.94|
|middle of hood| 0.23|0.07|
|right middle of hood| 0.04|0.05|
|left middle of hood| 0.04|0.05|
|inside hood right below fan| 0.66|0.40|
|inside hood side of fan| 0.52|(4)|

(1) We did not feel comfortable taking the ductape off, so this measurement was not repeated. 

(2) Instructions not clear if the window is to be open or to be closed during measurements

(3) Sensor not present

(4) Location not clear

3.	Can you understand and explain the analysis procedure to a third person?
- The analysis processes on chemical resistance and windspeed itself (save for some details on the latter) are well-documented and quite simple, so explaining the genral process to a third person is very much doable.

4.	Is the setup robust and safe to operate? 
- The set-up itself is robust and safe to operate.
- Based on the reported safety instructions, the chemical testing of the coating is safe for someone who also studied chemistry, and safe under adequate supervision for someone who studied only physics.

5.	Did you encounter any issues? Could you troubleshoot those without contacting the owners?
- The battery necesarry for the airflow measurements was also used by power supply group. We asked the project group if an alternative power source was present, but there was not. In the end we were able to use the battery after the group peer-reviewing the power supply gorup had finished.
- Testing of the coating required making an appointment with Jesper, which we were not able to do on Monday.
- Aforementioned uncertainties regarding the details on the airflow measurements. For some of the measurements, we thought of two possible locations/measurements settings. In those cases we tried both and reported the two values if they were significantly different. Three measurements were not retaken, one of which was taken during the prodcution process so not being able to repeat was not considered a problem. We could have asked the project group for more details on the nature of the other two (one where the required anemonitor was missing, one were the measurement location was not clear). Additionally, we could perhaps have asked the project group where to find the third anemonitor. 

6.	What part of the measurement procedure did you appreciate most?
- It is nice that the ventillation results are largely reproducible.

### Interactions:

1.	Could you relate to the stated goal of the project?
- Yes, see also answer to question 1 under documentation.

2.	Which instructions did you need from the owners on top of the written files?
- See question 5 under measurements.

3.	Does the experiment accomplish its stated purpose?
- Yes, the box is present, and according to measurments by the project group it is well-ventilated and the coated wood is reasonable resistant to most chemicals studied. This was confirmed by the peer-reviewers, as the air flow measurements were largely reproduced and the piece of coated wood used for the testing coating by the project group was still available for examination.

4.	What do you recommend to the project owners to improve their complete package?
- Find a separate battery/power supply so you're not dependant upon the power supply group and you can do experiments simultaneosly.
- Alter the readme file of your folder so one is more guided towards reproducing the experiment.
- Within the instructions, also mention the building process and link to it. Even though it will be a bit far-fetched to repeat the entire building process, it is good to have an idea on e.g. what materials you used in the production of your box.
- Make sure all the relevant details of your measurements, particularly the airflow measurments, are well-documented.

## Reaction
Thanks for the feedback! First of all, we don't think we should buy a seperate battery. When the sample preperation module is eventually added to the experiment box, there should be enough power to supply all the projects. We do agree that there should be more links between files and that we should have been more detailed in describing the measurement processes. We incorporated your feedback and hopefully you can agree that it improved our documentation.


