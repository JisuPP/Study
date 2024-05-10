SELECT PRODUCT_CODE, 
    SUM(PRICE*SALES_AMOUNT) AS SALES
FROM PRODUCT JOIN OFFLINE_SALE USING(PRODUCT_ID)
GROUP BY PRODUCT_CODE
ORDER BY SUM(PRICE*SALES_AMOUNT) DESC, PRODUCT_CODE;