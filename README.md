# Blood_Pressure

## OBJECTIVE:

To write a Flask app that runs locally, and remotely (frozen), which will read two inputs sent to it via two textboxes in a frontend page, 
compute an output using a pickled ML file, and send it back to the frontend to display.

## PROJECT DESCRIPTION:
The Web application will take 2 inputs from the user- namely the user's age and their weight , through a form . 
There will be 2 buttons - submit and clear . Upon clicking the submit button, the input values are sreceived by the flask server , 
which then makes use of the Machine learning pickle file to predict the blood pressure of the user , whose value is rendered and displayed on the frontend.

The home page consists of a form that has 2 inputs, 2 buttons. 
The inputs must be validated- That is they cannot allow character values to be entered for Age and should display some alert message if the users accidentally enters wrong input type. Also , the user cannot submit until he/she enters the input .This is covered in the video clearly. The submit button should submit the input values and get the output, which is the predicted blood pressure . And, the search button , upon clicking should clear the input results as well as the predicted output value

The output is rendered from backend and displayed at the botton of the form in a seperate container. The container needs to be styled to make it look good !!

The last last functionality is a button on top of the page- its named 'More Info' , which upon clicking should open a collapsible panel from right side of the page. Thid displays some additional information such as blood pressure range , hypertensions etc
