SELECT eu.unique_id,e.name
FROM EMPLOYEES e
LEFT JOIN EMPLOYEEUNI eu
on eu.id=e.id

