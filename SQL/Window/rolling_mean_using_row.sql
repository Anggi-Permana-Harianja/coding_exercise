SELECT
    order_date, 
    region, 
    product_category,
    AVG(sales_amount) OVER (
        PARTITION BY region, product_category
        ORDER BY order_date
        ROWS BETWEEN
            6 PRECEDING AND current_row
    ) AS rolling_avg_sales
FROM sales;
