-- https://www.interviewquery.com/questions/closest-sat-scores

-- Given a table of students and their SAT test scores, write a query to return the two students with the closest test scores with the score difference.

-- If there are multiple students with the same minimum score difference, select the student name combination that is higher in the alphabet.

-- Tips: Use self cross join

SELECT s1.student AS one_student, s2.student AS other_student,
    ABS(s1.score - s2.score) AS score_diff
FROM scores AS s1 CROSS JOIN scores AS s2
    ON s1.id != s2.id
ORDER BY score_diff, 1, 2
LIMIT 1