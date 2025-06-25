PRAGMA foreign_keys= OFF;
BEGIN TRANSACTION;
CREATE TABLE locations
(
    id          INTEGER   NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    city        TEXT      NOT NULL,
    description TEXT      NOT NULL,
    identifier  TEXT      NOT NULL,
    PRIMARY KEY (id AUTOINCREMENT)
);
INSERT INTO locations
VALUES (1, '2025-06-23 19:00:18', 'Napoli',
        'The third largest metropolitan city in Italy, it has been described by the BBC as "the Italian city with too much history to handle."',
        'napoli');
CREATE TABLE hotels
(
    id          INTEGER   NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name        TEXT      NOT NULL,
    description TEXT      NOT NULL,
    perks       TEXT      NOT NULL,
    location_id INTEGER   NOT NULL,
    PRIMARY KEY (id AUTOINCREMENT),
    foreign key (location_id) references locations (id)
);
INSERT INTO hotels
VALUES (1, '2025-06-23 19:00:18', 'H22 Hotel',
        'An inviting stay very close to Napoli Centrali, the city''s main train station, the H22 Hotel is the product of proprietor Giulia Berardinelli''s vision. She is a third-generation hotelier who has followed in the career footsteps of her father and grandfather. Each room in the building is decorated in a unique, special way. The name H22 signifies two hours taken out of the day, dedicated solely to oneself. The guests of H22 frequently speak to the sense of care and welcome cultivated by the staff of H22 Hotel.',
        'Always fully refundable', 1);
CREATE TABLE hotel_photos
(
    id         INTEGER   NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    width_t    INTEGER,
    height_t   INTEGER,
    src_t      TEXT,
    width      INTEGER,
    height     INTEGER,
    src        TEXT,
    hotel_id   INTEGER,
    primary key (id AUTOINCREMENT),
    foreign key (hotel_id) REFERENCES hotels (id)
);
INSERT INTO hotel_photos
VALUES (1, '2025-06-23 19:00:18', 150, 225,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/7206edc9.jpg?impolicy=resizecrop&rw=150&ra=fit',
        1200, 1800,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/7206edc9.jpg?impolicy=resizecrop&rw=1200&ra=fit',
        1);
INSERT INTO hotel_photos
VALUES (2, '2025-06-23 19:00:18', 225, 150,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=225&ra=fit',
        1200, 800,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/f73cbdfd.jpg?impolicy=resizecrop&rw=1200&ra=fit',
        1);
INSERT INTO hotel_photos
VALUES (3, '2025-06-23 19:00:18', 225, 150,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/030663f5.jpg?impolicy=resizecrop&rw=225&ra=fit',
        1200, 800,
        'https://images.trvl-media.com/lodging/93000000/92690000/92689700/92689637/030663f5.jpg?impolicy=resizecrop&rw=1200&ra=fit',
        1);

COMMIT;
