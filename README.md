# SRM-Redesign

![AWS LEX BADGE](https://img.shields.io/badge/AWS%20-Lex-orange)
![Python Badge](https://img.shields.io/badge/Python-v3.7.8-yellowgreen)

-------------

## About the Project

This is our take to re-design SRM’s official website where we have documented our design process, pros and cons of the current website and how we came up with this design as the solution to the problem statement. We have added a couple of design images to explain our process however, we would recommend you to visit the deployed link for the complete view.

-------------

## Packages and Services used in the Devepoment Process

- **Django** : Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, focusing on writing your app without needing to reinvent the wheel. It’s free and open source.
- **AWS Lex** : Amazon Lex is an AWS service for building conversational interfaces for applications using voice and text.
- **Kommunicate** : Kommunicate is a human + bot hybrid customer support software for real-time and proactive customer support, made for businesses of every size.
- **Bootstrap v5** : Quickly design and customize responsive mobile-first sites with Bootstrap, the world's most popular front-end open source toolkit.
- **Heroku** : Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

-------------

## PROS OF THE CURRENT WEBSITE:

- **Color Organization** : Colors are an essential part of visual design language which is used to communicate with the users. The current SRM website’s color pallete is based on it’s branding i.e the logo. It’s a good idea to integrate the brand colors in our project.
- **Uniform Structure** : College websites have a very big database which requires daily update and maintenance. Having different UI’s for different sections of the website would have resulted in confusion and trouble for the team. However, we see SRM has maintained a uniform tabulated structure involving dropdowns and tabs thus organizing the data in a simple yet attractive design.
- **Multiple CTAs** : The website has multiple elements leading to the same pages thus, enabling the user to access important pages from their current position in the website.
- **Path Display** : Keeping in mind that it is a huge website, the designers have done a great job in showing the path from home to the current page that the user is visiting.
- **Using Material Design** : The designers have used cards and tables in their UI which not only gives the website a structure but also, keeps the design trendy and attractive.

-------------

## CONS OF THE CURRENT WEBSITE:

- **Navigation** : The current website consists of two navbars which do not remain the same while moving on to any other page. While navigating through the website, we came across issues such as tabs leading to external websites. This may lead to confusion since it is a huge website.
- **Landing Page Picture** : A landing page of the website is the first look of the college. The website consists of pictures of SRM students in different locations instead of our own campus. This can be considered as a con since it doesn’t give a clear picture of what to expect from the college, when an user visits the page.
- **Misleading UX elements** : Some of the cards don’t show any response when hovered. From a UX point of view, this doesn’t notify the user that the element is actually interactive. Some of the links such as “More” in the home page (Tab: Academics) are placed below the text causing confusion about which card it is actually meant for.
- **About section is last** : The “About” section of any website is known to give the introduction to the product or brand. It is ideally supposed to be the first section of the website, but however in our case, it is situated in the end.
- **Responsiveness** : The navbars of the home page were not fully organised when it came to mobile view of the website. They were overlapping in 2-3 size ratios thus causing huge issues for our mobile users.

-------------

## MOTIVATION BEHIND THE PROJECT

Keeping in mind the pros and cons of the website, this is how we came up with the designthat we consider to be the ideal solution of the current stage. We have re-implemented the pros with a slight touch of improvement in our website design. For the cons, we brain-stormed ideas and researched on how to solve and make it convenient yet attractive for the users.

-------------

## OUR SOLUTIONS TO THE ISSUES:

- For Navigation, we have come up with a single page structure/ design that fits all the criterias and the multiple types of information provided in the website. Each of these structures have information pulling from the backend as a result of which, it will be very easy to edit or add new information. We have reduced the 2 navbars into a single constant one which covers all the information required for the student/parent.

