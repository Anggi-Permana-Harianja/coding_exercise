-- https://www.interviewquery.com/questions/closest-sat-scores

-- Given a table of students and their SAT test scores, write a query to return the two students with the closest test scores with the score difference.

-- If there are multiple students with the same minimum score difference, select the student name combination that is higher in the alphabet.



-- Tips: Use self join

SELECT t1.student AS one_student,
    t2.student AS other_student,
    ABS(t1.student - t2.student) AS score_diff
FROM table AS t1
JOIN table AS t2
    ON t1.score < t2.score
GROUP BY 3, 1, 2
LIMIT 1