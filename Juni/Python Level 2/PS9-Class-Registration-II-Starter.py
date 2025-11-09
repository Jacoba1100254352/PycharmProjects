"""
When students enroll in their classes for the semester, their names are appended to a list for each class. However, the system mistakenly does not prevent students from enrolling in a class multiple times if they resubmit the form, so several students appear on a class list multiple times, in the order they submitted the form. The system also does not properly waitlist students, as each class has a maximum enrollment of 6 students.

Write a program that, given the lists for each class, prints out who is on the waitlist for each class. Note that if a student was within the first six students to sign up, even if their name is on the list later, they should be enrolled in the class.
"""

biology = ["Sarah", "Ahmed", "Fred", "Gillian", "Shradah", "Max", "Max", "Sara", "Max", "Esther"]

computerScience = ["Sarah", "John", "Fred", "Gillian", "Jermaine", "Max", "Sara", "Juan", "Esther"]

english = ["Nico", "Sharjeel", "Isabella", "Taylor", "Ali", "Ali", "Jean-Baptiste", "Jean-Baptiste", "Jean-Baptiste",
           "William"]
