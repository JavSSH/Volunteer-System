CREATE TABLE opportunity (
    opportunity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    pin_user_id INTEGER NOT NULL,
    csrrep_user_id INTEGER NOT NULL,
    opportunity_date datetime,
    FOREIGN KEY (request_id) REFERENCES request(request_id),
    FOREIGN KEY (pin_user_id) REFERENCES user(user_id),
    FOREIGN KEY (csrrep_user_id) REFERENCES user(user_id)
);

-- Opportunities created from completed requests
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (1, 4, 40, 3, '19/11/2024');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (2, 6, 52, 5, '24/06/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (3, 8, 51, 8, '12/09/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (4, 9, 37, 12, '10/10/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (5, 10, 36, 15, '26/12/2024');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (6, 13, 28, 18, '20/02/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (7, 14, 93, 22, '13/05/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (8, 16, 28, 25, '03/08/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (9, 18, 45, 30, '25/09/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (10, 19, 7, 33, '19/11/2024');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (11, 20, 76, 37, '17/08/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (12, 27, 62, 41, '31/12/2024');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (13, 28, 86, 44, '21/04/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (14, 30, 99, 48, '02/08/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (15, 33, 91, 52, '29/11/2024');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (16, 34, 6, 55, '11/04/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (17, 35, 54, 58, '11/05/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (18, 37, 78, 62, '27/04/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (19, 38, 29, 65, '19/03/2025');
insert into opportunity (opportunity_id, request_id, pin_user_id, csrrep_user_id, opportunity_date) values (20, 39, 60, 68, '19/05/2025');
