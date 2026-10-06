SELECT p.product_name,s.year,s.price
FROM SALES s
LEFT JOIN PRODUCT p
on s.product_id=p.product_id;