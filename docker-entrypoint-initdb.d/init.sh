set -e
psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}<< EOSQL

CREATE DATABASE work_shift_management;

USE work_shift_management;

CREATE TABLE users(
	user_id INT(8) PRIMARY KEY AUTO_INCREMENT,
	mail VARCHAR(128) NOT NULL UNIQUE,
	password VARCHAR(64) NOT NULL,
	salt VARCHAR(32) NOT NULL,
	user_name VARCHAR(32) NOT NULL,
	delete_flg bool NOT NULL DEFAULT false
);


CREATE TABLE userGroups(
	group_id INT(8) PRIMARY KEY AUTO_INCREMENT,
	user_id INT(10) NOT NULL,
	group_name VARCHAR(32) NOT NULL,
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE joiningGroups (
	joining_group_id INT(20) PRIMARY KEY AUTO_INCREMENT,
	user_id INT(11) NOT NULL,
	group_id INT(8) NOT NULL,
	FOREIGN KEY(user_id) REFERENCES users(user_id),
	FOREIGN KEY(group_id) REFERENCES userGroups (group_id)
);

CREATE TABLE jobInfos(
	job_id INT(10) PRIMARY KEY AUTO_INCREMENT,
	user_id INT(8) NOT NULL,
	job_name VARCHAR(30),
	color_code INT(8) NOT NULL,
	delete_flg bool DEFAULT 0 
);

CREATE TABLE schedules(
	schedule_id BIGINT(20) PRIMARY KEY AUTO_INCREMENT,
	job_id INT(10),
	color_code INT(8) DEFAULT 0 NOT NULL,
	schedule_title VARCHAR(32) NOT NULL,
	start_time datetime  NOT NULL,
	end_time DATETIME NOT NULL,
	private_flg bool DEFAULT 0,
	delete_flg bool DEFAULT 0,
	FOREIGN KEY(job_id) REFERENCES jobInfos(job_id)
);


ALTER TABLE usergroups ADD group_string VARCHAR(16) NOT NULL UNIQUE;

ALTER TABLE joininggroups DROP FOREIGN KEY joininggroups_ibfk_2;
ALTER TABLE joininggroups ADD FOREIGN KEY(group_id) REFERENCES usergroups (group_id) ON DELETE CASCADE;

EOSQL
