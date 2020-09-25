CREATE TABLE public."crimeByweather"
(
	"Date" date NOT NULL,
	unique_key bigint NOT NULL,
	description text COLLATE  pg_catalog."default",
	"TempHighF" real,
	"TempAvgF" real,
	"TempLowF" real,
	"Events" text COLLATE pg_catalog."default",
	index bigint NOT NULL DEFAULT nextval('"crimeByweather_index_seq"'::regclass),
	CONSTRAINT crime_pkey PRIMARY KEY (unique_key)
)

TABLESPACE pg_default;

ALTER TABLE public."crimeByweather"
	OWNER TO postgres;