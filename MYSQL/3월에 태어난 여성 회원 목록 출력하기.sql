SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE SUBSTRING(DATE_OF_BIRTH, 6, 2) = 03
    AND GENDER = W
    AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;