DROP TABLE IF EXISTS meal_list;

CREATE TABLE IF NOT EXISTS meal_list (
    meal_id SERIAL PRIMARY KEY,
    meal_name TEXT NOT NULL, 
    meal_price TEXT NOT NULL
);

INSERT INTO meal_list(meal_name, meal_price) VALUES ('Thai Fish Cake', '$13.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Thai Samosa', '$13.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Chicken Satay', '$13.95');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Tom Yum Soup', '$17.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Pineapple Fried Rice', '$17.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Green Curry', '$17.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Pad Thai', '$16.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Khao Moo Krob Cripsy Pork', '$17.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Hor Mok Pla Curry Fish', '$20.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Papaya Salad Thai Style', '$15.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Mango Sticky Rice', '$12.00');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Thai Ice Tea', '$5.50');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Strawberry Lemonade', '$3.50');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Thai Ice Coffee', '$5.50');
INSERT INTO meal_list(meal_name, meal_price) VALUES ('Sparkling Water', '$4.50');
