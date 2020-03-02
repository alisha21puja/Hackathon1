# Hackathon [techevent]
Abstract
The objective is to develop a web platform, where in the colleges and schools , who are organizing different events like hackathons, workshops, or fests can register their events. This web platform gives the complete details of all the upcoming events registered in. The people who are interested can easily find appropriate events to take part in and to register for the event.
Existing system
The existing websites give the registration links and the news when the hackathon is being spread in the corresponding college using their web platform or might be with the help of the email service or through other social media websites like youtube, etc. There is no way to ask any participants to avoid circulating or distributing their ideas or feedback of the event which can be displayed on the website publicly [1]. 
There is no option to write blogs on the website by the participants or sponsors [2]. The registration links are most probably google sheets and such things or it might allow the participant to register on our platform and accordingly the data will be shared with organiser  of the particular event, the notification of the events and all will not be provided easily. Most often the organisers of the event create their own webpages for promotion and the registrations. the organisers look into sponsorship at their risk, the participants does not have any common platform to look into the upcoming events.
Proposed system
The proposed web based platform that is aimed to help the organizers of the fests, workshops or hackathon events to post their event details, resources and related information. The platform provides a common registration to the posted events, this will help the students to register and participate in the events easily. The companies who would like to sponsor the events can sponsor the events based on the event details. This platform maintains the blog feature to be in connection with different communities (participants, organizers, and sponsors). 
The web based platform helps the organiser to register an event easily, provide its description, and other details. The interested people who are searching for the events, can easily and quickly register for the event through our website, they will be noticed about the start of the event, after completion they will be prompted for the feedback and review the event they have attended. The organisers can easily get sponsors through  this portal. they can also specify the facilities for the sponsors and can determine the different scale of sponsor types. They can share the required resources and contents through this portal.
This web based platform will help the people who wish to be a part of hackathon events. To find the appropriate event to be a part of, biased on the feedback of the previous participants. The web based platform provides the complete details of the events and hence people can be updated with the recent hackathons and events that are going to happen and the other necessary event details. The webportal helps the users to post the event details, the people who like to participate in various events can look here for the various events, and can choose the best ones from his view, quickly without spending much time in searching for different events, since this platform helps all the organisers to register their events.


1. Project title
TECHEVENT
A web platform that helps to manage your technical events.
2. Description
TECHEVENT is a web platform that is aimed to help the organizers of the fests, workshops or hackathon events to post their event details, resources and related information. The platform provides registration to the events, this will help the participants to register and participate in the events easily. The companies who would like to sponsor the events can sponsor the events based on the event details. This platform maintains the blog feature to be in connection with different communities (participants, organizers, and sponsors). 
The web platform helps the organisers to register an event easily, provide its description, and other details. The interested people who are searching for the events, can easily and quickly register for the event through our platform, after completion of the event they will be prompted for the feedback/review the event they have attended. The organisers can easily get sponsors through  this portal, they can also specify the facilities for the sponsors and can determine the different scale of sponsor types. They can share the required resources and contents through this portal.
This web platform will help the users to manage their events quickly. The platform provides unique feature of share resources and blogs. This helps the organisers to share the prerequisite and other resources to the participants. The blogs helps the different users to share their ideas on various topics.


3. Testing techniques
3.1 UNIT TESTING
Unit testing is a software development process in which the smallest testable parts of an application, called units, are individually and independently scrutinized for proper operation. Unit testing is often automated but it can also be done manually. Unit testing involves only those characteristics that are vital to the performance of the under test. Once all of the units in a program have been found to be working in the most efficient and error-free manner possible, larger components of the program can be evaluated by means of integrating testing. 
3.2 INTEGRATION TESTING
Integration testing is the phase in software testing in which individual software modules are combined and tested as a group. It occurs after unit testing and validation testing. Integration testing takes as its input modules that have been unit  tested, groups them in larger aggregates, applies tests defined in an integration test plan to those aggregates, and delivers as its output the integrated system ready for system testing. 
3.3 White Box Testing
White-box testing, sometimes called glass-box testing, is a test-case design philosophy that uses the control structure described as part of component-level design to derive test cases. Using white-box testing methods, you can derive test cases that (1) guarantee that all independent paths within a module have been exercised at least once, (2) exercise all logical decisions on their true and false sides, (3) execute all loops at their boundaries and within their operational bounds, and (4) exercise internal data structures to ensure their validity.


3.3.1 Types of White Box Testing
3.3.1.1 Basic path testing
The basic path method enables the test-case designer to derive a logical complexity measure of a procedural design and use this measure as a guide for defining a basis set of execution paths. Test cases derived to exercise the basis set are guaranteed to execute every statement in the program at least one-time during testing.
3.3.1.2 Flow graph notation
The flow graph depicts logical control flow using the notation. Each structured construct has a corresponding flow graph symbol. And the testing is carried out like the traversal among the nodes.
3.3.1.3 Independent program path
An independent path is any path through the program that introduces at least one new set of processing statements or a new condition. When stated in terms of a flow graph, an independent path must move along at least one edge that has not been traversed before the path is defined. 
3.4 Black Box Testing
Black-box testing, also called behavioral testing, focuses on the functional requirements of the software. That is, black-box testing techniques enable you to derive sets of input conditions that will fully exercise all functional requirements for a program. Black-box testing attempts to find errors in the following categories: (1) incorrect or missing functions, (2) interface errors, (3) errors in data structures or external database access, (4) behavior or performance errors, and (5) initialization and termination errors. By applying black-box techniques, you derive a set of test cases that satisfy the following criteria: (1) test cases that reduce, by a count that is greater than one, the number of additional test cases that must be designed to achieve reasonable testing, and (2) test cases that tell you something about the presence or absence of classes of errors, rather than an error associated only with the specific test at hand.
3.4.1 Types of Black Box Testing
3.4.1.1 Graph- based Testing Methods
Graph based testing begins by creating a graph of important objects and their relationships and then devising a series of tests that will cover the graph so that each object and relationship is exercised and errors are uncovered. You can then derive test cases by traversing the graph and covering each of the relationships shown. These test cases are designed in an attempt to find errors in any of the relationships. Beizer describes a number of behavioral testing methods that can make use of graphs:
1. Transaction flow modeling. The nodes represent steps in some transaction, and the links represent the logical connection between steps. The data flow diagram can be used to assist in creating graphs of this type.
2. Finite state modeling. The nodes represent different user-observable states of the software, and the links represent the transitions that occur to move from state to state. The state diagram can be used to assist in creating graphs of this type.
3. Data flow modeling. The nodes are data objects, and the links are the transformations that occur to translate one data object into another.
4. Timing modeling. The nodes are program objects, and the links are the sequential connections between those objects. Link weights are used to specify the required execution times as the program executes.
3.4.1.2 Equivalence Partitioning
Equivalence partitioning is a black-box testing method that divides the input domain of a program into classes of data from which test cases can be derived. An ideal test case single-handedly uncovers a class of errors that might otherwise require many test cases to be executed before the general error is observed. Test-case design for equivalence partitioning is based on an evaluation of equivalence classes for an input condition. An equivalence class represents a set of valid or invalid states for input conditions. Typically, an input condition is either a specific numeric value, a range of values, a set of related values, or a Boolean condition.
3.4.1.3 Boundary Value Analysis (BVA)
A greater number of errors occurs at the boundaries of the input domain rather than in the center. It is for this reason that BVA has been developed as a testing technique. BVA leads to a selection of test cases that exercise bounding values. BVA is a test-case design technique that complements equivalence partitioning. Rather than selecting any element of an equivalence class, BVA leads to the selection of test cases at the edges of the class. Rather than focusing solely on input conditions, BVA derives test cases from the output domain as well.
4. TEST CASES
4.1 Login Form
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Form displayed with all the controls
Display the login form with all the controls
Form loaded successfully with all the controls
Pass
2
Enter wrong username and password
Display login form again with invalid message.
Message displayed
Pass
3
Enter not registered details.
Display invalid message.
Message displayed
Pass
4
Enter correct username and correct password of any of the registered users.
The appropriate home page is loaded.
Login to their home pages
Pass


5
Press login button without filling the username and password
Display warning message to fill the details
Warning message displayed
Pass

4.2 Registration Form
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Form displayed
Display form with all controls
Form loaded with all controls
Pass
2
Click Register button without data
Display warning message to fill all the details
Warning Message displayed to fill data
Pass
3
Enter correct data and fill the registration form
The data is stored in the database and a mail is sent to the registered mail address. And a message for successful registration is displayed
Registration is successful and a message to login appears.
Pass


4
Enter Wrong Mail Address
Display error message to enter correct mail address
Error message displayed
Pass
5
Enter Wrong Phone number
Display error message to enter correct phone number
Error message displayed
Pass
6
Enter different password
Display error message to enter matching passwords
Error message displayed
Pass
7
Enter invalid picture format
Display error message to select correct file type
Error message displayed
Pass

4.3 Organise Event Form
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Form displayed
Display form with all controls
Form loaded with all controls
Pass
2
Click Submit button without data
Display warning message to fill all the details
Warning Message displayed
Pass
3
Enter correct data to the fields
Event registered successfully and redirect to the events page
Events gets successfully registered
Pass


4
Click save button with wrong inputs
Display corresponding warning messages
Message displayed
Pass
5
Give invalid inputs to different fields
Appropriate validation messages are shown
The messages gets shown
Pass
4.4 Organiser Dashboard
No.
Test Scenario
Expected Result
Observed Result 
Result
1
On login the organiser dashboard is displayed
Dashboard is displayed
Dashboard appears when login as organiser
Pass
2
Check different navigation links
All links redirect to the corresponding pages
All links worked
Pass
+
4.5 Your Events
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Page loaded with all the events registered
Events listed
Events listed successfully
Pass
2
Click on various CRUD buttons for the event
CRUD operations working
All operations worked
Pass

4.6 Participate Events
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Page loaded with all the events registered
Events listed
Events listed successfully
Pass
2
Event details are listed
All the coming up events are listed
All events are listed
Pass
3
Click on participate button
The participation gets recorded
Successful in participating the event
Pass
4
Again click participate button
Warning message should be shown
Warning message is shown
Pass

4.7 Enquire about an event
No.
Test Scenario
Expected Result
Observed Result 
Result
1
Page loaded with all the contact form
Page loaded with the required controls
Page loaded successfully
Pass
2
Press the contact button without submit button
The contact form shows warning message
The message gets displayed
Pass
3
Select the event for contact
The to mail id gets filled
The to mail address appears
Pass
4
Check the mail sent items
The sent mail can be seen
The mail gets sent
Pass

4.8 Project home page
No.
Test Scenario
Expected Result
Observed Result 
Result
1
The pages are loaded with the appropriate controls
The pages and controls are loaded
The components are loaded properly
Pass
2
Checking different links
The links are redirecting to the appropriate pages
All links worked
Pass

4.9 Participant Dashboard
No.
Test Scenario
Expected Result
Observed Result 
Result
1
On login the dashboard is displayed
Dashboard is displayed
Dashboard appears when login as participant
Pass
2
Check different navigation links
All links redirect to the corresponding pages
All links worked
Pass
4.10 Event feedback
No.
Test Scenario
Expected Result
Observed Result 
Result
1
On selecting the event participated the feedback can be given
The feedback form is displayed when the button is clicked
Form loaded correctly
Pass
2
Fill the form with correct details
The message gets sent
Message sent successfully
Pass
3
Fill the form with invalid inputs
The corresponding warning messages are shown
The messages shown as warnings 
Pass

4.11 Blogs
No.
Test Scenario
Expected Result
Observed Result 
Result
1
The page loaded with all the controls
The page is shown with all the controls
The page is loaded with all the controls
Pass
2
Fill the form with appropriate data
The Data gets saved
The blogs gets added
Pass
3
Fill the fields with inappropriate data
Appropriate warnings are shown
The warnings worked
Pass





5. ER Diagram


6. DFD Diagrams
6.1 Level 0 DFD

6.2 Level 1 DFD




6.3 Level 2 DFD









7. Screenshots 
7.1 Home Page


7.2 Login / Signup


7.3 Organiser - Dashboard



7.4 Organise  Event



7.5 Your Events


7.6 Upcoming Events - Participants


7.7 Sponsor- Dashboard

7.8 Enquire about Event

