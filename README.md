# RobotFramework_LeanFT

This is a Robot Framework library implementaion to interface with UFT14's LeanFT Runtime, using the standard LeanFT SDK. Solution Components: 
      * LeanFT
      * LeanFT Java SDK
      * Jython
      * Intellij

# Installation Instructions

Step 1: Install Java 8.191 SE JDK 

Step 2: Install HP UFT - ( Only V 14+ is currently supported)

Step 3: Jython -   https://www.jython.org/download.html    -  jython-installer-2.7.2

Step 4: Downloaded IntelliJ - Community (2017.1 windows zip edition)
https://www.jetbrains.com/idea/download/other.html

Step 5: Navigate to <UFT Home>\HPE\Unified Functional Testing\IDE\IntelliJ\plugins and copy leanFT folder
Paste it inside the unzipped IntelliJ folder<IntelliJ Home>\plugins (Sometimes this folder would be created under ‘Users’)
	
In most cases, the below navigation would work as these are standard home folders: 
Navigate to C:\Program Files (x86)\HPE\Unified Functional Testing\IDE\IntelliJ\plugins—and copy leanFT folder

Paste it inside the unzipped IntelliJ folder C:\Program Files\JetBrains\IntelliJ IDEA Community Edition\plugins (Sometimes this folder would be created under ‘Users’)
	
Step 6:
Install Robot Framework (jython -m pip install robotframework)

Step 7:

In Windows 10
Click Start and type “Environment” now click on “Edit Environment System Variables”

Select PATH and Click Edit button under System variables and add below paths

C:\jython2.7.2
C:\jython2.7.2\bin

Under system variables update or add below values

Variable: JAVA_HOME
Value: C:\Program Files\Java\jdk1.8.0_191

Variable: JRE_HOME
Value: C:\Program Files\Java\jre1.8.0_191

Variable: LEANFT_HOME
Value: <UFT Home>

For standard installations the following should work

“C:\Program Files (x86)\HPE\Unified Functional Testing”

Step 8: 

  Download the WinLFT Library and place it within JYTHONPATH.
  
Step 9: 
  
  Update the relevant plugins to support python for intellij
  Update the relevant plugins to support robot framework for intellij


# Usage Instructions

(1) Create a LEanFT Application Model project in itelliJ. For thid library to work. It is important that the application model is always created in the package "com.company.ApplicationModel". 

This is will act as shared repository of all the application objects. For steps, refer the below URL and follow instructions for intelliJ Idea

       https://admhelp.microfocus.com/uftdev/en/15.0-15.0.2/HelpCenter/Content/HowTo/TestObjects_AppModel.htm#mt-item-1
  
 Note: The solution in its current state only supports one object model i.e. all objects on the AUT should be spied into one app model project intellij. The below URL has some tips on how large app models could be managed 
 
  	https://admhelp.microfocus.com/uftdev/en/15.0-15.0.2/HelpCenter/Content/HowTo/TestObjects_AppModel.htm#mt-item-5
	
   
(2) Once the objects are all spied, create a jar for the project as a class 

(3) Create  a new python project and select the interpreter as Jython

(4) Import the jar from (2) as dependency. 

(5) All the objects in the jar are now available for robot keywords.

(6) USe the documentation file "WinLFT_Documentation.html" available within this repo for the keywords available. 



Rock On !!

	



