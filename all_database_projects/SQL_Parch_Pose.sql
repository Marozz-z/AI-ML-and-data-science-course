INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4001, ' Future Tech ', NULL, 30.0444, 31.2357, NULL, 1),
(4002, '  Smart Solutions', 'SMART.COM', NULL, NULL, 'Ahmed Ali', 2);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4003, 'ABC Company', 'abc1.com', 30.2, 31.1, 'Sara', 3),
(4004, 'ABC Company', 'abc2.com', 30.3, 31.2, 'Mona', 3);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4005, 'Tech Vision', 'duplicate.com', 30.5, 31.5, 'Ali', 4),
(4006, 'AI World', 'duplicate.com', 30.6, 31.6, 'Omar', 4);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4007, '   Delta Company    ', 'delta.com', 30.7, 31.7, '   Karim Hassan    ', 5);

INSERT INTO web_events
(id, account_id, occurred_at, channel)
VALUES
(9001, 4001, GETDATE(), 'facebook'),
(9002, 4001, GETDATE(), 'Facebook'),
(9003, 4001, GETDATE(), 'FACEBOOK'),
(9004, 4001, GETDATE(), 'fb'),
(9005, 4001, GETDATE(), 'google'),
(9006, 4001, GETDATE(), 'Google Ads');

INSERT INTO web_events
(id, account_id, occurred_at, channel)
VALUES
(9007, 4002, GETDATE(), NULL);

INSERT INTO orders
(id, account_id, occurred_at,
standard_qty, gloss_qty, poster_qty,
total, standard_amt_usd, gloss_amt_usd,
poster_amt_usd, total_amt_usd)
VALUES
(8001, 4001, GETDATE(), 100, 50, 20, 170, 7000, 1000, 500, 8500),
(8002, 4001, GETDATE(), 10, 5, 2, 17, 12000, 500, 300, 12800),
(8003, 4002, GETDATE(), 2, 1, 0, 3, 1500, 200, 0, 1700);

INSERT INTO orders
(id, account_id, occurred_at,
standard_qty, gloss_qty, poster_qty,
total, standard_amt_usd, gloss_amt_usd,
poster_amt_usd, total_amt_usd)
VALUES
(8004, 4002, NULL,
NULL, NULL, NULL,
NULL, NULL, NULL, NULL, NULL);

DELETE FROM orders
WHERE id BETWEEN 8001 AND 8004;

DELETE FROM web_events
WHERE id BETWEEN 9001 AND 9007;

DELETE FROM accounts
WHERE id BETWEEN 4001 AND 4007;

-- ==========================================
-- 1. INSERT INTO ACCOUNTS
-- ==========================================
INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4001, ' Future Tech ', NULL, 30.0444, 31.2357, NULL, 1),
(4002, '  Smart Solutions', 'SMART.COM', NULL, NULL, 'Ahmed Ali', 2);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4003, 'ABC Company', 'abc1.com', 30.2, 31.1, 'Sara', 3),
(4004, 'ABC Company', 'abc2.com', 30.3, 31.2, 'Mona', 3);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4005, 'Tech Vision', 'duplicate.com', 30.5, 31.5, 'Ali', 4),
(4006, 'AI World', 'duplicate.com', 30.6, 31.6, 'Omar', 4);

INSERT INTO accounts
(id, name, website, lat, [long], primary_poc, sales_rep_id)
VALUES
(4007, '   Delta Company    ', 'delta.com', 30.7, 31.7, '   Karim Hassan    ', 5);


-- ==========================================
-- 2. INSERT INTO WEB_EVENTS
-- ==========================================
INSERT INTO web_events
(id, account_id, occurred_at, channel)
VALUES
(9001, 4001, GETDATE(), 'facebook'),
(9002, 4001, GETDATE(), 'Facebook'),
(9003, 4001, GETDATE(), 'FACEBOOK'),
(9004, 4001, GETDATE(), 'fb'),
(9005, 4001, GETDATE(), 'google'),
(9006, 4001, GETDATE(), 'Google Ads');

INSERT INTO web_events
(id, account_id, occurred_at, channel)
VALUES
(9007, 4002, GETDATE(), NULL);


-- ==========================================
-- 3. INSERT INTO ORDERS
-- ==========================================
INSERT INTO orders
(id, account_id, occurred_at,
standard_qty, gloss_qty, poster_qty,
total, standard_amt_usd, gloss_amt_usd,
poster_amt_usd, total_amt_usd)
VALUES
(8001, 4001, GETDATE(), 100, 50, 20, 170, 7000, 1000, 500, 8500),
(8002, 4001, GETDATE(), 10, 5, 2, 17, 12000, 500, 300, 12800),
(8003, 4002, GETDATE(), 2, 1, 0, 3, 1500, 200, 0, 1700);

INSERT INTO orders
(id, account_id, occurred_at,
standard_qty, gloss_qty, poster_qty,
total, standard_amt_usd, gloss_amt_usd,
poster_amt_usd, total_amt_usd)
VALUES
(8004, 4002, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);


-- ==========================================
-- 4. DELETE STATEMENTS
-- ==========================================
DELETE FROM orders
WHERE id BETWEEN 8001 AND 8004;

DELETE FROM web_events
WHERE id BETWEEN 9001 AND 9007;

DELETE FROM accounts
WHERE id BETWEEN 4001 AND 4007;

SELECT 
    name,
    website,
    ISNULL(website, 'Unknown Website') AS clean_website
FROM accounts;

