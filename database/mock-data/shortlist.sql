CREATE TABLE shortlist (
    shortlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,  -- CSR user who shortlisted
    request_id INTEGER NOT NULL,  -- The PIN request they saved
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    UNIQUE(user_id, request_id)  -- Prevent duplicate shortlists
);

-- CSR user 3 shortlisted these open requests
insert into shortlist (shortlist_id, user_id, request_id) values (1, 3, 1);
insert into shortlist (shortlist_id, user_id, request_id) values (2, 3, 7);
insert into shortlist (shortlist_id, user_id, request_id) values (3, 3, 15);

-- CSR user 5 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (4, 5, 2);
insert into shortlist (shortlist_id, user_id, request_id) values (5, 5, 11);
insert into shortlist (shortlist_id, user_id, request_id) values (6, 5, 23);

-- CSR user 8 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (7, 8, 3);
insert into shortlist (shortlist_id, user_id, request_id) values (8, 8, 12);
insert into shortlist (shortlist_id, user_id, request_id) values (9, 8, 25);

-- CSR user 12 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (10, 12, 5);
insert into shortlist (shortlist_id, user_id, request_id) values (11, 12, 17);
insert into shortlist (shortlist_id, user_id, request_id) values (12, 12, 29);

-- CSR user 15 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (13, 15, 7);
insert into shortlist (shortlist_id, user_id, request_id) values (14, 15, 21);
insert into shortlist (shortlist_id, user_id, request_id) values (15, 15, 31);

-- CSR user 18 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (16, 18, 22);
insert into shortlist (shortlist_id, user_id, request_id) values (17, 18, 24);
insert into shortlist (shortlist_id, user_id, request_id) values (18, 18, 32);

-- CSR user 22 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (19, 22, 15);
insert into shortlist (shortlist_id, user_id, request_id) values (20, 22, 36);
insert into shortlist (shortlist_id, user_id, request_id) values (21, 22, 40);

-- CSR user 25 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (22, 25, 45);
insert into shortlist (shortlist_id, user_id, request_id) values (23, 25, 46);
insert into shortlist (shortlist_id, user_id, request_id) values (24, 25, 47);

-- CSR user 30 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (25, 30, 52);
insert into shortlist (shortlist_id, user_id, request_id) values (26, 30, 54);
insert into shortlist (shortlist_id, user_id, request_id) values (27, 30, 55);

-- CSR user 33 shortlisted these
insert into shortlist (shortlist_id, user_id, request_id) values (28, 33, 58);
insert into shortlist (shortlist_id, user_id, request_id) values (29, 33, 59);
insert into shortlist (shortlist_id, user_id, request_id) values (30, 33, 61);

insert into shortlist (shortlist_id, user_id, request_id) values (31, 4, 2);
insert into shortlist (shortlist_id, user_id, request_id) values (32, 4, 3);
insert into shortlist (shortlist_id, user_id, request_id) values (33, 4, 59);

insert into shortlist (shortlist_id, user_id, request_id) values (34, 6, 1);
insert into shortlist (shortlist_id, user_id, request_id) values (35, 6, 4);
insert into shortlist (shortlist_id, user_id, request_id) values (36, 6, 25);

insert into shortlist (shortlist_id, user_id, request_id) values (37, 7, 5);
insert into shortlist (shortlist_id, user_id, request_id) values (38, 7, 13);
insert into shortlist (shortlist_id, user_id, request_id) values (39, 7, 33);

insert into shortlist (shortlist_id, user_id, request_id) values (40, 9, 7);
insert into shortlist (shortlist_id, user_id, request_id) values (41, 9, 12);
insert into shortlist (shortlist_id, user_id, request_id) values (42, 9, 41);

insert into shortlist (shortlist_id, user_id, request_id) values (43, 11, 14);
insert into shortlist (shortlist_id, user_id, request_id) values (44, 11, 28);
insert into shortlist (shortlist_id, user_id, request_id) values (45, 11, 42);

insert into shortlist (shortlist_id, user_id, request_id) values (46, 13, 16);
insert into shortlist (shortlist_id, user_id, request_id) values (47, 13, 18);
insert into shortlist (shortlist_id, user_id, request_id) values (48, 13, 27);

insert into shortlist (shortlist_id, user_id, request_id) values (49, 14, 19);
insert into shortlist (shortlist_id, user_id, request_id) values (50, 14, 23);
insert into shortlist (shortlist_id, user_id, request_id) values (51, 14, 55);

insert into shortlist (shortlist_id, user_id, request_id) values (52, 16, 21);
insert into shortlist (shortlist_id, user_id, request_id) values (53, 16, 30);
insert into shortlist (shortlist_id, user_id, request_id) values (54, 16, 22);

insert into shortlist (shortlist_id, user_id, request_id) values (55, 17, 47);
insert into shortlist (shortlist_id, user_id, request_id) values (56, 17, 50);
insert into shortlist (shortlist_id, user_id, request_id) values (57, 17, 63);

insert into shortlist (shortlist_id, user_id, request_id) values (58, 19, 10);
insert into shortlist (shortlist_id, user_id, request_id) values (59, 19, 11);
insert into shortlist (shortlist_id, user_id, request_id) values (60, 19, 72);

insert into shortlist (shortlist_id, user_id, request_id) values (61, 20, 35);
insert into shortlist (shortlist_id, user_id, request_id) values (62, 20, 36);
insert into shortlist (shortlist_id, user_id, request_id) values (63, 20, 84);

insert into shortlist (shortlist_id, user_id, request_id) values (64, 21, 24);
insert into shortlist (shortlist_id, user_id, request_id) values (65, 21, 25);
insert into shortlist (shortlist_id, user_id, request_id) values (66, 21, 26);

insert into shortlist (shortlist_id, user_id, request_id) values (67, 23, 31);
insert into shortlist (shortlist_id, user_id, request_id) values (68, 23, 40);
insert into shortlist (shortlist_id, user_id, request_id) values (69, 23, 53);

insert into shortlist (shortlist_id, user_id, request_id) values (70, 24, 18);
insert into shortlist (shortlist_id, user_id, request_id) values (71, 24, 34);
insert into shortlist (shortlist_id, user_id, request_id) values (72, 24, 78);

insert into shortlist (shortlist_id, user_id, request_id) values (73, 26, 43);
insert into shortlist (shortlist_id, user_id, request_id) values (74, 26, 50);
insert into shortlist (shortlist_id, user_id, request_id) values (75, 26, 77);

insert into shortlist (shortlist_id, user_id, request_id) values (76, 27, 60);
insert into shortlist (shortlist_id, user_id, request_id) values (77, 27, 70);
insert into shortlist (shortlist_id, user_id, request_id) values (78, 27, 29);

insert into shortlist (shortlist_id, user_id, request_id) values (79, 28, 51);
insert into shortlist (shortlist_id, user_id, request_id) values (80, 28, 63);
insert into shortlist (shortlist_id, user_id, request_id) values (81, 28, 74);

insert into shortlist (shortlist_id, user_id, request_id) values (82, 29, 67);
insert into shortlist (shortlist_id, user_id, request_id) values (83, 29, 22);
insert into shortlist (shortlist_id, user_id, request_id) values (84, 29, 14);

insert into shortlist (shortlist_id, user_id, request_id) values (85, 31, 45);
insert into shortlist (shortlist_id, user_id, request_id) values (86, 31, 53);
insert into shortlist (shortlist_id, user_id, request_id) values (87, 31, 61);

insert into shortlist (shortlist_id, user_id, request_id) values (88, 32, 18);
insert into shortlist (shortlist_id, user_id, request_id) values (89, 32, 31);
insert into shortlist (shortlist_id, user_id, request_id) values (90, 32, 43);

insert into shortlist (shortlist_id, user_id, request_id) values (91, 34, 54);
insert into shortlist (shortlist_id, user_id, request_id) values (92, 34, 58);
insert into shortlist (shortlist_id, user_id, request_id) values (93, 34, 77);

insert into shortlist (shortlist_id, user_id, request_id) values (94, 35, 62);
insert into shortlist (shortlist_id, user_id, request_id) values (95, 35, 68);
insert into shortlist (shortlist_id, user_id, request_id) values (96, 35, 81);

insert into shortlist (shortlist_id, user_id, request_id) values (97, 36, 1);
insert into shortlist (shortlist_id, user_id, request_id) values (98, 36, 11);
insert into shortlist (shortlist_id, user_id, request_id) values (99, 36, 82);

insert into shortlist (shortlist_id, user_id, request_id) values (100, 37, 83);