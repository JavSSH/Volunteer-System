create table userprofile (
	role_id INT,
	role_name VARCHAR(50),
	description TEXT,
	status VARCHAR(50)
);
insert into userprofile (role_id, role_name, description, status) values (1, 'UserAdmin', 'A UserAdmin manages all the user accounts', true);
insert into userprofile (role_id, role_name, description, status) values (2, 'PlatformManager', 'A PlatformManager manages all the volunteer categories', true);
insert into userprofile (role_id, role_name, description, status) values (3, 'PersonInNeed (PIN)', 'A PIN manages all their requests', true);
insert into userprofile (role_id, role_name, description, status) values (4, 'CSR Rep', 'A CSR Rep manages volunteer opportunities', true);