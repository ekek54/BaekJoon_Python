-- 코드를 입력하세요
SELECT CAR_TYPE AS CAR_TYPE, COUNT(CAR_ID) AS CARS
FROM (
    SELECT *
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE REGEXP_LIKE(options, '통풍시트|열선시트|가죽시트')
    ) as OP
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC