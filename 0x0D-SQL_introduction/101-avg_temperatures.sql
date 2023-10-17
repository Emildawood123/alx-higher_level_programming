-- cript that displays the average temperature (Fahrenheit) by city ordered by temperature 
SELECT city, AVG(value) AS avg_temp FROM 'temperatures.sql' ORDER BY avg_temp;
