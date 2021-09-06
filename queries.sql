-- Get orders and line items
SELECT
  o.id,
  o.last_name,
  p.name,
  oi.price,
  oi.quantity
FROM
  orders_order o
  JOIN orders_orderitem oi ON o.id = oi.order_id
  JOIN shop_product p ON oi.product_id = p.id