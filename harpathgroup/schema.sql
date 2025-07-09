PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "locations"
(
    id          INTEGER                             not null
        primary key autoincrement,
    created_at  TIMESTAMP default CURRENT_TIMESTAMP not null,
    city        TEXT                                not null,
    description TEXT                                not null,
    identifier  TEXT                                not null,
    region      text                                not null
);
INSERT INTO locations VALUES(1,'2025-06-23 19:00:18','Napoli',replace(replace('The third largest metropolitan city in Italy, it has been described by the BBC as "the Italian city with too much history to handle."\r\n        ','\r',char(13)),'\n',char(10)),'napoli','Campania');
INSERT INTO locations VALUES(3,'2025-07-01 13:40:50','Salerno','Beautiful location.  It has much to offer.','salerno','Campania');
CREATE TABLE IF NOT EXISTS "hotels"
(
    id             INTEGER                             not null
        primary key autoincrement,
    created_at     TIMESTAMP default CURRENT_TIMESTAMP not null,
    name           TEXT                                not null,
    description    TEXT                                not null,
    perks          TEXT                                not null,
    location_id    INTEGER                             not null
        references locations,
    affiliate_link TEXT,
    identifier     text                                not null
);
INSERT INTO hotels VALUES(1,'2025-06-23 19:00:18','H22 Hotel','An inviting stay very close to Napoli Centrali, the city''s main train station, the H22 Hotel is the product of proprietor Giulia Berardinelli''s vision. She is a third-generation hotelier who has followed in the career footsteps of her father and grandfather. Each room in the building is decorated in a unique, special way. The name H22 signifies two hours taken out of the day, dedicated solely to oneself. The guests of H22 frequently speak to the sense of care and welcome cultivated by the staff of H22 Hotel.','Always fully refundable, rainfall showerheads',1,'https://expedia.com/affiliates/naples-hotels-h22-hotel.XEna95o','h22');
CREATE TABLE IF NOT EXISTS "hotel_photos"
(
    id         INTEGER                             not null
        primary key autoincrement,
    created_at TIMESTAMP default CURRENT_TIMESTAMP not null,
    width_t    INTEGER,
    height_t   INTEGER,
    src_t      TEXT,
    width      INTEGER,
    height     INTEGER,
    src        TEXT,
    hotel_id   INTEGER
        references hotels
            on delete cascade
);
INSERT INTO hotel_photos VALUES(1,'2025-06-23 19:00:18',225,150,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=225&ra=fit',1200,800,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=1200&ra=fit',1);
INSERT INTO hotel_photos VALUES(2,'2025-06-23 19:00:18',225,150,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=225&ra=fit',1200,800,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=1200&ra=fit',1);
INSERT INTO hotel_photos VALUES(14,'2025-07-09 13:22:23',150,225,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/7206edc9.jpg?impolicy=resizecrop&rw=150&ra=fit',1200,1800,'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/7206edc9.jpg?impolicy=resizecrop&rw=1200&ra=fit',1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('locations',4);
INSERT INTO sqlite_sequence VALUES('hotels',13);
INSERT INTO sqlite_sequence VALUES('hotel_photos',14);
COMMIT;
