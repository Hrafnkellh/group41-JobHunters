# group41-JobHunters

We tested the website on firefox.

You can use it by running the following commands from the root directory of the application (the one this readme is in)
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
cd jobhunters
python manage.py runserver

You can then visit the website at an address displayed in your terminal.


We believe we've implemented all the core requirements as described in the assignment description but we made a slight change to the 'job applications page'
Instead of having a seperate page for it, you can see all your job applications at the bottom of your profile and from there you can click on each one to view
it in more detail on its dedicated page.

We also decided to use the word 'Employer' in place of 'Company' since this is a job seeking site.

in addition to a few extra requirements from our requirement analysis report taken verbatim listed below:

"The website should be pleasant to look at":
We think it looks pretty good.

"Users should be able to view what job type they are applying for. part/full time":
This can be viewed on each job listing's page. You can also filter for it on the front page.

"Users should be able to reset their password.":
This one didn't make a whole lot of sense since we´re not using an email server so it's
not clear how it would be done. Instead we decided to change it to "users should be able to change their passwords."
This can be done from the profile page.

"Users can withdraw an application.":
Applications can be deleted from your profile page.

"Users can access a Help Center with FAQs and guides." and "Users can access a section for career advice, interview tips, and professional development resources.":
We tried to implement this through three pages that can be accessed through links in the footer: FAQ, About us, and Job Tips.

"Users can track the status of their applications in real-time.":
You can check the status of your application at any time by going to the bottom of your profile page.

"Employers can schedule interviews through the platform.":
This was unfortunately never implemented, though the interview model was made and exists in the database.

"Users can filter job listings to find remote work opportunities.":
This is implemented and found under the "filtering and sorting options" tab on the main screen.

"Users can filter companies based on Environmental and Social Governance (ESG) ratings.":
The ESG ratings are displayed on each employer's page, but we never added it to filtering.