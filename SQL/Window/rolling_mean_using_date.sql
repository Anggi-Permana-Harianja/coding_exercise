SELECT
    order_date, 
    region, 
    product_category,
    AVG(sales_amount) OVER (
        PARTITION BY region, product_category 
        ORDER BY order_date 
        RANGE BETWEEN 
            INTERVAL '6 days' PRECEDING AND CURRENT ROW
        ) AS rolling_avg_sales
FROM sales;
