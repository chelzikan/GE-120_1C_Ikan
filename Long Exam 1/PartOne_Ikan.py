"""


1. Differentiate Procedural Programming from Functional Programming

in procedural programming, you follow control structures. in functional programming, it is up to the programmers on how to execute their codes in such a way that it'll still work in the end. 

2. How does Git help in the Collaborative Development and Version Control environment of programming?

Git helps us collab with other people thru branches. inside that branches, we can make our independent repositories, wherein we can edit our codes
whenever and wherever we like. tapos yung mga naedit natin na changes, we can push it so others can see 'yung changes na ginawa natin. then, ipupull naman
nila yung changes para maupdate yung local repository nila. tapos after non, pwede na nating imerge yung mga changes or pagsamahin yung codes na ginawa natin individually and noong
mga kacollab natin. 
so in essence, git allows us to work simultaneously. habang ibang part ang cinocode mo, pwedeng ibang part din ang cinocode ng kasama mo, then pwede 
niyo silang pagsamahin together. 
for example, we want to create a map displaying the # of out of school youth across metro manila. if nakapagcollect na kayo ng data, you can divide tasks
with your groupmates. so kunyare, ikaw ang magaayos/magcocode ng data distribution para sa map, yung isang kasama mo ang nagaayos for the visual elements of the map, etc.
with al the changes you and your groupmates made, you can just push and pull na lang para maging updated kayo and merge it afterwards na lang then you'll have an output na. 



3. When should one use a while loop and when should one use for a loop? Give examples in the field of Geomatics.

While loop can be used if we want to input/process many data. it will work as long as the condition we input holds true. but if the statement is false,
then it will end. 
for example, may REC ka and yung required is <= 1:10000. if naginput ka nang naginput ng REC mo and it is lower than 1:10000, you will be asked to input REC again. magtutuloy tuloy yung pag-ask sayo ng paginput until masatisfy mo na yung 1:10000.


for loop naman, you can use it if you want madefine yung variables/values mo in that given list. 
for example, you want to calculate the bearings ng traverse. maaask ka to input yung distances and azimuth, then kung hanggang ilang lines yung meron ka or gusto mong ilagay. yung iinput mo na data for that line ay madedefine siya wherein magkakaoutput ka in the end ng bearings, lat, and dep ng lines. 


4. Discuss the Divide and Conquer Paradigm in programming.

Divide and conquer paradigm just basically tells us na there's one problem, then you divide it to subproblems na gagawan mo ng solutions. then in the end, pagsasamahin mo 
lang yung mga solutions na iyon to answer your problem. 

for example kinuha mo yung vertical and horizontal measurement ng traverse mo and gusto mo siyang icompute. you can divide the traverse into vertical and horizontal, and then you makes codes to solve each. after that, you combine them into a single solution na lang.


5. Give an example of a task related to geomatics that is done manually and can be optimized using programming. What would be your plan-of-attack for this solution?

area subdivision. instead of solving it manually, it can be done using programming. first, using the while loop, it will ask the users the number of points sa kanilang lot. after that, we will use for loop, to ask the users the distances and bearings
between the lines. then, we will input codes that can compute for the area of the lot. to determine the dividing line, trial line, and closing line, you can use 'yung if-elif-else functions. then,
you will again input codes that can help you determine the distances between sa lines (dividing, trial, and closing) and points mo. after that, you print yung result na gusto mong makuha.





: < hohoho
"""