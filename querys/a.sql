CREATE TABLE circuits (
    circuitId SERIAL PRIMARY KEY,
    circuitRef TEXT,
    name TEXT,
    location TEXT,
    country TEXT,
    lat REAL,
    lng REAL,
    alt REAL,
    url TEXT
);
