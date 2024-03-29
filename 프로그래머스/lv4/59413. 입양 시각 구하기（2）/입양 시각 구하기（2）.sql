-- 코드를 입력하세요
WITH RECURSIVE CTE 
AS (
    SELECT 0 AS N
    UNION ALL
    SELECT N + 1
    FROM CTE
    WHERE N < 23
)

SELECT 
    CTE.N AS HOUR,
    CASE 
    WHEN DATETIME IS NULL THEN 0
    ELSE COUNT(*)
    END AS COUNT
FROM CTE
LEFT JOIN ANIMAL_OUTS
ON CTE.N = HOUR(DATETIME)
GROUP BY HOUR
ORDER BY HOUR