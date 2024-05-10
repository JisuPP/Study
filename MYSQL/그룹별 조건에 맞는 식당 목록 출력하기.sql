SELECT MP.MEMBER_NAME
     , RR.REVIEW_TEXT
     , DATE_FORMAT(RR.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW AS RR
JOIN MEMBER_PROFILE AS MP
    ON RR.MEMBER_ID = MP.MEMBER_ID
WHERE RR.MEMBER_ID = (SELECT MEMBER_ID
                     FROM REST_REVIEW
                     GROUP BY MEMBER_ID
                     ORDER BY COUNT(REVIEW_SCORE) DESC
                     LIMIT 1)
ORDER BY RR.REVIEW_DATE, RR.REVIEW_TEXT