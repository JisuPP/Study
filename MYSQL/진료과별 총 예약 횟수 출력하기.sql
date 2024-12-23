SELECT MCDP_CD AS '진료과 코드', COUNT(*) '5월예약건수'
FROM APPOINTMENT
WHERE SUBSTRING(APNT_YMD, 1, 7) = '2022-05'
GROUP BY MCDP_CD
ORDER BY COUNT(*) ASC, MCDP_CD ASC;

-------------------------------------

SELECT
    MCDP_CD AS '진료과 코드',
    COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD) = 2022
    AND MONTH(APNT_YMD) = 05
GROUP BY 1
ORDER BY 2, 1;