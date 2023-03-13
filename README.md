# CS50_Final_Project: METHOD CLIMBING
## Video Demo: https://www.youtube.com/watch?v=UFanJqpbrow
# Description:

# Method Climbing is a training app made for rock climbers that lets you record your climbing sessions + all the climbs you send. This app collects all of your climbing data and shows you how you are progressing in the form of charts (which I created using Chart JS). There are 4 main pages: Profile, Logbook, Goals, and Progression. There is also 3 pages before you have logged in: an about page ('Why Use Method Climbing?'), the 'Login' page, and the 'Register' page.

# The Profile section allows you to see some of the information you inputed when you registered (such as your full name, country, username, birthday) and you have the option to input extra bits of information like your biggest goal, when you started climbing, etc. There are two buttons in the profile section that lead you to an 'Edit Profile' form- where you can edit the information in your profile, and a 'Change Password' form- where you can change your password (which must meet certain requirements in order to be valid and well protected).

# The Logbook page allows you to log sessions and climbs. The 'Log A New Climb/Session' button takes you a form where you can input data about a climb you have just done (date, type of climb, grade, attempts, style, notes) and once you submit the form, you will be taken to a page that shows you all the climbs you have done on that date in the form of a table. You have the option to delete climbs by clicking on the 'Delete' button at the right of the table row. To see session data from a specific day, on the main page of Logbook, you can click on the dropdown menu under 'See Session Data From' and then click 'Get Session Overview'.

# The Goals page lets you see your goals in the form of a list. You have the option of adding, editing, deleting, or crossing off a goal.

# The Progression page displays 3 different charts: your boulder grade pyramid, your sport climbing grade pyramid, and your climbing style histogram. These Javascript charts pull user data from SQL using Flask and connect it to JS using Jinja.

# My initial idea was far too ambitious, I wanted a full app with every feature a training app could have. Unfortunately, my skill did not yet match my vision. My idea went through many changes and reiterations. Although my app looks very simple, every page required tons of research and learning how to put my vision into code using the different frameworks we learned in CS50x. I looked at many training and climbing apps that exist out there for inspiration which helped me fledge out my idea further.