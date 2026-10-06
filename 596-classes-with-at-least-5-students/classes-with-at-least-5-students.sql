SELECT class FROM COURSES
GROUP BY class
HAVING count(class)>=5;