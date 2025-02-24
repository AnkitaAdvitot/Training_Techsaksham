create schema if not exists countries;
USE COUNTRIES;
DROP TABLE IF EXISTS countries.COUNTRIES;
CREATE TABLE countries.COUNTRIES(
	COUNTRY_ID INT,
    NAME VARCHAR(255),
    NATIONALITY VARCHAR(255),
    COUNTRY_CODE VARCHAR(3),
    ISO_ALPHA VARCHAR(2),
    CAPITAL VARCHAR(255),
    POPULATION INT,
    AREA_KM2 INT,
    REGION_ID INT);
INSERT INTO countries.COUNTRIES (COUNTRY_ID, NAME, NATIONALITY, COUNTRY_CODE, ISO_ALPHA, CAPITAL) VALUES
(1, 'United States', 'American', 'USA', 'US', 'Washington, D.C.'),
(2, 'India', 'Indian', 'IND', 'IN', 'New Delhi'),
(3, 'United Kingdom', 'British', 'GBR', 'GB', 'London'),
(4, 'Canada', 'Canadian', 'CAN', 'CA', 'Ottawa'),
(5, 'Australia', 'Australian', 'AUS', 'AU', 'Canberra'),
(6, 'Germany', 'German', 'DEU', 'DE', 'Berlin'),
(7, 'France', 'French', 'FRA', 'FR', 'Paris'),
(8, 'Italy', 'Italian', 'ITA', 'IT', 'Rome'),
(9, 'Japan', 'Japanese', 'JPN', 'JP', 'Tokyo'),
(10, 'Brazil', 'Brazilian', 'BRA', 'BR', 'Brasília'),
(11, 'China', 'Chinese', 'CHN', 'CN', 'Beijing'),
(12, 'Russia', 'Russian', 'RUS', 'RU', 'Moscow'),
(13, 'South Africa', 'South African', 'ZAF', 'ZA', 'Pretoria'),
(14, 'Mexico', 'Mexican', 'MEX', 'MX', 'Mexico City'),
(15, 'Spain', 'Spanish', 'ESP', 'ES', 'Madrid'),
(16, 'Argentina', 'Argentinian', 'ARG', 'AR', 'Buenos Aires'),
(17, 'South Korea', 'South Korean', 'KOR', 'KR', 'Seoul'),
(18, 'Saudi Arabia', 'Saudi', 'SAU', 'SA', 'Riyadh'),
(19, 'Turkey', 'Turkish', 'TUR', 'TR', 'Ankara'),
(20, 'Indonesia', 'Indonesian', 'IDN', 'ID', 'Jakarta');
