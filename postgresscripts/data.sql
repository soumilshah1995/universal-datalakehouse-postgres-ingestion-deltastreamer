CREATE TABLE IF NOT EXISTS public.sales
(
    salesid SERIAL PRIMARY KEY,
    invoiceid integer,
    itemid integer,
    category text COLLATE pg_catalog."default",
    price numeric(10,2),
    quantity integer,
    orderdate date,
    destinationstate text COLLATE pg_catalog."default",
    shippingtype text COLLATE pg_catalog."default",
    referral text COLLATE pg_catalog."default",
    updated_at TIMESTAMP DEFAULT NOW()
    );

INSERT INTO public.sales (invoiceid, itemid, category, price, quantity, orderdate, destinationstate, shippingtype, referral) VALUES (101, 1, 'Electronics', 599.99, 2, '2023-11-21', 'California', 'Express', 'Friend');
INSERT INTO public.sales (invoiceid, itemid, category, price, quantity, orderdate, destinationstate, shippingtype, referral) VALUES (102, 3, 'Clothing', 49.99, 5, '2023-11-22', 'New York', 'Standard', 'OnlineAd');
INSERT INTO public.sales (invoiceid, itemid, category, price, quantity, orderdate, destinationstate, shippingtype, referral) VALUES (103, 2, 'Home & Garden', 199.50, 1, '2023-11-23', 'Texas', 'Express', 'WordOfMouth');
INSERT INTO public.sales (invoiceid, itemid, category, price, quantity, orderdate, destinationstate, shippingtype, referral) VALUES (104, 4, 'Books', 15.75, 3, '2023-11-24', 'Florida', 'Standard', 'SocialMedia');
INSERT INTO public.sales (invoiceid, itemid, category, price, quantity, orderdate, destinationstate, shippingtype, referral) VALUES (103, 2, 'Home & Garden', 199.50, 1, '2023-11-23', 'Texas', 'Express', 'WordOfMouth');