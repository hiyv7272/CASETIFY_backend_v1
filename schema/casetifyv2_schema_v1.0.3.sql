###############################################################################
# [CASETIFYv2 초기 INSERT data schema 스크립트]
###############################################################################


-- INSERT INTO USER 비회원
INSERT INTO CASETIFYv2.USER (id, name, email, password, mobile_number, create_datetime, update_datetime, is_use) VALUES (1, '비회원', 'test00@test.com', '12345678', '01000000000', NOW(), NOW(), True);


--  INSERT INTO FEATURED table
INSERT INTO FEATURED (name) VALUES ('phone_case');
INSERT INTO FEATURED (name) VALUES ('watch_band');
INSERT INTO FEATURED (name) VALUES ('ACC');


-- INSERT INTO DEVICE_BRAND table
INSERT INTO DEVICE_BRAND (name) VALUES ('Apple');
INSERT INTO DEVICE_BRAND (name) VALUES ('Samsung');
INSERT INTO DEVICE_BRAND (name) VALUES ('LG');


-- DEVICE_COLOR table
INSERT INTO DEVICE_COLOR (name) VALUES ('Silver');
INSERT INTO DEVICE_COLOR (name) VALUES ('Gold');
INSERT INTO DEVICE_COLOR (name) VALUES ('Space_Grey');
INSERT INTO DEVICE_COLOR (name) VALUES ('White');
INSERT INTO DEVICE_COLOR (name) VALUES ('Black');
INSERT INTO DEVICE_COLOR (name) VALUES ('Red');
INSERT INTO DEVICE_COLOR (name) VALUES ('Coral');
INSERT INTO DEVICE_COLOR (name) VALUES ('Yellow');
INSERT INTO DEVICE_COLOR (name) VALUES ('Blue');
INSERT INTO DEVICE_COLOR (name) VALUES ('Green');
INSERT INTO DEVICE_COLOR (name) VALUES ('Purple');
INSERT INTO DEVICE_COLOR (name) VALUES ('Midnight_Green');


-- INSERT INTO DEVICE
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='White' LIMIT 1), 'iphone_SE2', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Black' LIMIT 1), 'iphone_SE2', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Red' LIMIT 1), 'iphone_SE2', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_11_Pro_Max', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Gold' LIMIT 1), 'iphone_11_Pro_Max', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_11_Pro_Max', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Midnight_Green' LIMIT 1), 'iphone_11_Pro_Max', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_11_Pro', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Gold' LIMIT 1), 'iphone_11_Pro', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_11_Pro', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Midnight_Green' LIMIT 1), 'iphone_11_Pro', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='White' LIMIT 1), 'iphone_11', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Black' LIMIT 1), 'iphone_11', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Red' LIMIT 1), 'iphone_11', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Yellow' LIMIT 1), 'iphone_11', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Green' LIMIT 1), 'iphone_11', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Purple' LIMIT 1), 'iphone_11', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_Xs', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_Xs', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Gold' LIMIT 1), 'iphone_Xs', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_Xs_Max', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_Xs_Max', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Gold' LIMIT 1), 'iphone_Xs_Max', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='White' LIMIT 1), 'iphone_XR', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Black' LIMIT 1), 'iphone_XR', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Red' LIMIT 1), 'iphone_XR', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Coral' LIMIT 1), 'iphone_XR', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Yellow' LIMIT 1), 'iphone_XR', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Blue' LIMIT 1), 'iphone_XR', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_X', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_X', '1');

INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Silver' LIMIT 1), 'iphone_8', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Gold' LIMIT 1), 'iphone_8', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Space_Grey' LIMIT 1), 'iphone_8', '1');
INSERT INTO DEVICE (DEVICE_BRAND_id, DEVICE_COLOR_id, name, is_use) VALUES (1, (SELECT id from DEVICE_COLOR WHERE name='Red' LIMIT 1), 'iphone_8', '1');


-- INSERT INTO ARTIST
INSERT INTO ARTIST (name, description) VALUES ('CASETIFYLAB', 'This artwork is hand-picked and curated exclusively for Casetify. To help create sustainable jobs for creative communities across the globe, we''re committed to giving a portion of our profits back to our artists.');
INSERT INTO ARTIST (name, description) VALUES ('Vicky Webb', 'This artwork is hand-picked and curated exclusively for Casetify. To help create sustainable jobs for creative communities across the globe, we''re committed to giving a portion of our profits back to our artists.');


-- INSERT INTO ARTWORK_COLOR
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Clear', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Black', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('White Frost', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Rainbow', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Pink/Blue', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Yellow', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Neon Lime', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Glow In The Dark Pink', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Gold Chrome', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Silver Monochrome', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Rose Pink', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Unicorn Pastel', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Minimalist Too - White Marble', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Minimalist Too - Black Marble', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Spotted - Leopard', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Tort - Tortoise Shell', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Blue/Black', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Flame(Yellow/Orange)', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Hotline(Blue/Pink)', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('VIP(berry/Violet)', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Exxxtra(Green/Yellow)', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Silver', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Bronze', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Pink', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Red', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Purple', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Hot Pink', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Orange', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Green', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Midnight Green', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Solid Black', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Olive', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Navy', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Python - Ivory', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Python - Onyx', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Lavender Purple', '');
INSERT INTO ARTWORK_COLOR (name, info) VALUES ('Morning Glory Multi', '');


-- INSERT INTO ARTWORK_TYPE
INSERT INTO ARTWORK_TYPE (name) VALUES ('Impact');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Premium Marble');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Neon Sand');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Glitter');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Luxe Pressed Flower');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Gold Karat');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Snap');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Grip');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Wallet');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Leather Card');
INSERT INTO ARTWORK_TYPE (name) VALUES ('DTLA Impact Resistant');
INSERT INTO ARTWORK_TYPE (name) VALUES ('Ultra Thin Skin');


-- INSERT INTO ARTWORK
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '1', '1', '1', '', '0', NOW() ,NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '1', '2', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '1', '24', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '3', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '2', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '24', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '4', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '5', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '6', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '26', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '3', '7', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '5', '8', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '5', '9', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '5', '10', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '5', '11', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '5', '12', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '7', '18', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '7', '19', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '7', '20', '1', '', '0',NOW(),NOW(), '1');
INSERT INTO ARTWORK (name, FEATURED_id, DEVICE_id, ARTWORK_TYPE_id, ARTWORK_COLOR_id, ARTIST_id, description, is_custom, create_datetime, update_datetime, is_use) VALUES ('pp-0008', '1', '1', '7', '21', '1', '', '0',NOW(),NOW(), '1');


-- INSERT INTO ARTWORK_PRICE
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('1', '1', '35');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('2', '1', '35');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('3', '1', '35');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('4', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('5', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('6', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('7', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('8', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('9', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('10', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('11', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('12', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('13', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('14', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('15', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('16', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('17', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('18', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('19', '1', '40');
INSERT INTO ARTWORK_PRICE (ARTWORK_id, DEVICE_id, price) VALUES ('20', '1', '40');


-- INSERT INTO ARTWORK_COLOR_DEVICE
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('1', '1', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('2', '2', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('3', '24', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('4', '3', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('5', '2', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('6', '24', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('7', '4', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('8', '5', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('9', '6', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('10', '26', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('11', '7', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('12', '8', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('13', '9', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('14', '10', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('15', '11', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('16', '12', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('17', '18', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('18', '19', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('19', '20', '1');
INSERT INTO ARTWORK_COLOR_DEVICE (ARTWORK_id, ARTWORK_COLOR_id, DEVICE_id) VALUES ('20', '21', '1');


-- INSERT INTO ARTWORK_IMAGE
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('1', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001042.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001042.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001042.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001042.jpg?v=2', 'https://cdn.casetify.com/img/case/case_color_preview_16001042.jpg?v=3', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001042__render14.png.560x560-w.m80.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('2', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001043.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001043.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001043.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001043.jpg?v=2', 'https://cdn.casetify.com/img/case/case_color_preview_16001043.jpg?v=3', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001043__render14.png.560x560-w.m80.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('3', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001044.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001044.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001044.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001044.jpg?v=2', 'https://cdn.casetify.com/img/case/case_color_preview_16001044.jpg?v=3', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001044__render14.png.560x560-w.m80.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('4', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001039.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001039.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001039.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001039__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001039.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/22b4041dab11afcd160466024b011bd0.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('5', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001040.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001040.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001040.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001040__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001040_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/103e4eac901e632e312c728ecd276a60.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('6', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001041.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001041.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001041.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001041__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001041_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/7e1c7bb21aa6f265a8bc8a1df71ad0e7.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('7', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001063.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001063.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001063.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001063__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001063_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/7a822608b319cffdca18de1fe9ee726d.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('8', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001064.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001064.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001064.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001064__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001064_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/75bb36d5df480c167b8ec87c2de064f3.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('9', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001065.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001065.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001065.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001065__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001065_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/e79734495598341fd1ffa8de681eab87.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('10', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001066.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001066.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001066.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001066__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001066_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/e06ebbd5b71774b3aed432d7a6e774b8.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('11', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_silver_16001067.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_space-gray_16001067.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674x2_iphone-se__color_red_16001067.png.1000x1000-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001067__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001067_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/8cd3e5c855f893d016a6d0f8d2a114de.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('12', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001072.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001072.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001072.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001072__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001072.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/57f20abde860ce7cfd758822b395f2d4.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('13', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001073.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001073.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001073.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001073__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001073.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/a6e24529e9c17116d0fb2e93c7bfd7c2.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('14', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001074.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001074.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001074.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001074__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001074.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/288f2ba128858d06f14476a230d85312.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('15', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001075.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001075.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001075.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001075__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001075_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/f5c1e11353e67ba816461d5790604154.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('16', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001076.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001076.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001076.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001076__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001076.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/06fed197276379971db1b3fc427b3a9e.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('17', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001068.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001068.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001068.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001068__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001068_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/d0ab6085f70fff938ad9a21c760ff88a.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('18', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001069.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001069.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001069.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001069__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001069_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/cf7e2115ae0c6412c8e6332b81edf94f.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('19', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001070.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001070.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001070.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001070__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001070_gold.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001070__render14.png.560x560-w.m80.jpg,');
INSERT INTO ARTWORK_IMAGE (ARTWORK_id, image_url_1, image_url_2, image_url_3,image_url_4, image_url_5, image_url_6) VALUES ('20', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001071.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_space-gray_16001071.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_red_16001071.png.560x560-w.m80.jpg', 'https://cdn-image02.casetify.com/usr/14396/4304396/~v8/7057674_iphone-se__color_silver_16001071__render8.png.560x560-w.m80.jpg', 'https://cdn.casetify.com/img/case/side_color_preview_16001071_gold.jpg', 'https://ctgimage1.s3.amazonaws.com/cms/image/30e8589330ecd787c22cadbd7328e95d.jpg,');


-- INSERT INTO CHECKOUT_STATUS
INSERT INTO CHECKOUT_STATUS (name) VALUES ('주문완료');
INSERT INTO CHECKOUT_STATUS (name) VALUES ('주문취소');
INSERT INTO CHECKOUT_STATUS (name) VALUES ('결제완료');
INSERT INTO CHECKOUT_STATUS (name) VALUES ('결제취소');