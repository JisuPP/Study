SELECT
    D.ID,
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM DEVELOPERS D
    JOIN SKILLCODES S
        ON (S.CODE & D.SKILL_CODE) = S.CODE
WHERE S.NAME IN ('PYTHON', 'C#')
ORDER BY D.ID;