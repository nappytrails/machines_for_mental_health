-- DROP TABLE IF EXISTS mental_health_survey;

CREATE TABLE mental_health_survey(
	id SERIAL PRIMARY KEY,
	Age NUMERIC,
	Gender VARCHAR,
	Country VARCHAR,
	state VARCHAR,
	self_employed VARCHAR,
	family_history VARCHAR,
	treatment VARCHAR,
	remote_work VARCHAR,
	tech_company VARCHAR);
	
	
SELECT * FROM mental_health_survey;