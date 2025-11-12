PRAGMA foreign_keys = ON;

create table request (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT DEFAULT NULL, -- PIN that creates request
    category_id INT,
    request_status boolean,
    request_date datetime,
    request_view_count INT,
    request_shortlist_count INT,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (1, 9, 54, false, '27/07/2025', 89, 66);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (2, 9, 36, false, '22/03/2025', 89, 95);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (3, 10, 1, false, '24/11/2024', 58, 52);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (4, 40, 1, true, '18/11/2024', 62, 83);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (5, 31, 71, false, '24/09/2025', 1, 20);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (6, 52, 95, true, '23/06/2025', 40, 12);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (7, 15, 14, false, '21/11/2024', 51, 91);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (8, 51, 62, true, '11/09/2025', 60, 73);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (9, 37, 67, true, '09/10/2025', 12, 44);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (10, 36, 11, true, '25/12/2024', 95, 26);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (11, 9, 71, false, '28/06/2025', 86, 33);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (12, 48, 66, false, '30/11/2024', 31, 4);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (13, 28, 59, true, '19/02/2025', 82, 6);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (14, 93, 21, true, '12/05/2025', 79, 96);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (15, 98, 83, false, '02/03/2025', 18, 77);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (16, 28, 83, true, '02/08/2025', 68, 34);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (17, 67, 88, false, '31/12/2024', 50, 31);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (18, 45, 17, true, '24/09/2025', 53, 50);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (19, 7, 80, true, '18/11/2024', 47, 41);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (20, 76, 44, true, '16/08/2025', 12, 4);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (21, 93, 9, false, '21/09/2025', 76, 10);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (22, 75, 84, false, '14/12/2024', 9, 80);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (23, 75, 97, false, '18/02/2025', 71, 70);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (24, 29, 39, false, '16/04/2025', 52, 49);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (25, 64, 23, false, '30/04/2025', 85, 23);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (26, 1, 91, false, '03/06/2025', 44, 56);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (27, 62, 25, true, '30/12/2024', 13, 68);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (28, 86, 4, true, '20/04/2025', 4, 65);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (29, 47, 39, false, '09/11/2024', 8, 29);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (30, 99, 2, true, '01/08/2025', 80, 90);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (31, 76, 31, false, '30/03/2025', 57, 48);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (32, 42, 10, false, '14/06/2025', 46, 3);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (33, 91, 24, true, '28/11/2024', 13, 97);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (34, 6, 6, true, '10/04/2025', 100, 9);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (35, 54, 28, true, '10/05/2025', 9, 60);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (36, 94, 50, false, '09/05/2025', 50, 20);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (37, 78, 15, true, '26/04/2025', 28, 21);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (38, 29, 37, true, '18/03/2025', 55, 34);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (39, 60, 79, true, '18/05/2025', 91, 85);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (40, 1, 5, false, '28/09/2025', 65, 78);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (41, 43, 91, true, '20/09/2025', 37, 34);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (42, 21, 47, true, '09/02/2025', 63, 24);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (43, 80, 88, true, '15/07/2025', 79, 48);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (44, 1, 95, true, '17/01/2025', 58, 98);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (45, 61, 88, false, '27/01/2025', 1, 97);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (46, 16, 35, false, '27/12/2024', 93, 40);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (47, 74, 83, false, '18/06/2025', 79, 47);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (48, 35, 77, true, '22/02/2025', 21, 99);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (49, 25, 92, true, '18/12/2024', 37, 45);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (50, 45, 70, true, '27/01/2025', 55, 38);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (51, 32, 6, true, '09/01/2025', 53, 21);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (52, 42, 41, false, '23/01/2025', 51, 17);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (53, 19, 84, true, '03/07/2025', 26, 5);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (54, 93, 53, false, '16/07/2025', 57, 76);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (55, 51, 48, false, '14/05/2025', 45, 51);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (56, 47, 24, true, '17/02/2025', 13, 93);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (57, 54, 53, true, '21/11/2024', 33, 99);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (58, 40, 68, false, '12/04/2025', 83, 72);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (59, 42, 78, false, '09/02/2025', 21, 80);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (60, 9, 32, true, '18/12/2024', 44, 93);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (61, 48, 77, false, '01/02/2025', 41, 43);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (62, 83, 34, false, '11/01/2025', 83, 33);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (63, 72, 19, true, '20/07/2025', 86, 7);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (64, 94, 66, true, '11/03/2025', 7, 21);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (65, 96, 26, true, '27/06/2025', 78, 31);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (66, 98, 9, true, '10/08/2025', 33, 50);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (67, 29, 41, true, '10/03/2025', 82, 30);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (68, 53, 12, true, '10/10/2025', 50, 66);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (69, 96, 76, true, '28/10/2025', 59, 36);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (70, 26, 49, true, '30/11/2024', 16, 95);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (71, 80, 48, false, '18/07/2025', 66, 61);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (72, 54, 74, false, '19/05/2025', 90, 89);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (73, 87, 50, false, '19/08/2025', 72, 11);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (74, 56, 68, false, '28/02/2025', 13, 24);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (75, 15, 79, true, '30/10/2025', 59, 75);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (76, 42, 86, true, '09/04/2025', 48, 16);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (77, 34, 8, false, '18/02/2025', 51, 22);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (78, 4, 51, true, '25/05/2025', 90, 79);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (79, 73, 5, true, '13/10/2025', 24, 75);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (80, 62, 3, false, '05/08/2025', 32, 98);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (81, 14, 65, false, '23/05/2025', 43, 44);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (82, 74, 79, false, '06/12/2024', 70, 23);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (83, 39, 46, true, '13/05/2025', 44, 86);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (84, 79, 96, true, '12/12/2024', 88, 5);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (85, 24, 9, false, '06/01/2025', 59, 86);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (86, 21, 98, true, '06/09/2025', 77, 40);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (87, 2, 69, false, '09/06/2025', 13, 14);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (88, 57, 85, false, '16/07/2025', 76, 71);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (89, 71, 42, true, '06/10/2025', 40, 58);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (90, 86, 15, false, '03/05/2025', 98, 35);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (91, 99, 68, true, '15/08/2025', 13, 58);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (92, 80, 88, false, '10/07/2025', 7, 12);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (93, 38, 84, true, '22/04/2025', 32, 64);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (94, 92, 87, true, '03/03/2025', 47, 100);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (95, 34, 88, false, '08/12/2024', 64, 97);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (96, 29, 79, false, '10/10/2025', 84, 23);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (97, 36, 27, true, '02/09/2025', 69, 8);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (98, 7, 56, false, '06/12/2024', 44, 7);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (99, 55, 28, false, '27/05/2025', 20, 71);
insert into request (request_id, user_id, category_id, request_status, request_date, request_view_count, request_shortlist_count) values (100, 41, 88, false, '11/07/2025', 99, 59);