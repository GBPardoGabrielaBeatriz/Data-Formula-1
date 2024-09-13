
CREATE TABLE constructors (
    constructorId SERIAL PRIMARY KEY,
    constructorRef TEXT,
    name TEXT,
    nationality TEXT,
    url TEXT
);



CREATE TABLE drivers (
    driverId SERIAL PRIMARY KEY,
    driverRef TEXT,
    number INT,
    code TEXT,
    forename TEXT,
    surname TEXT,
    dob DATE,
    nationality TEXT,
    url TEXT
);


CREATE TABLE status (
    statusId SERIAL PRIMARY KEY,
    status TEXT
);



CREATE TABLE seasons (
    year INT PRIMARY KEY,
    url TEXT
);


CREATE TABLE races (
    raceId SERIAL PRIMARY KEY,
    year INT,
    round INT,
    circuitId INT REFERENCES circuits(circuitId),
    name TEXT,
    date DATE,
    time TIME,
    url TEXT,
    fp1_date DATE,
    fp1_time TIME,
    fp2_date DATE,
    fp2_time TIME,
    fp3_date DATE,
    fp3_time TIME,
    quali_date DATE,
    quali_time TIME,
    sprint_date DATE,
    sprint_time TIME
);


CREATE TABLE constructor_results (
    constructorResultsId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    constructorId INT REFERENCES constructors(constructorId),
    points REAL,
    status TEXT
);


CREATE TABLE constructor_standings (
    constructorStandingsId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    constructorId INT REFERENCES constructors(constructorId),
    points REAL,
    position INT,
    positionText TEXT,
    wins INT
);


CREATE TABLE driver_standings (
    driverStandingsId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    points REAL,
    position INT,
    positionText TEXT,
    wins INT
);


CREATE TABLE results (
    resultId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    constructorId INT REFERENCES constructors(constructorId),
    number INT,
    grid INT,
    position INT,
    positionText TEXT,
    positionOrder INT,
    points REAL,
    laps INT,
    time TEXT,
    milliseconds INT,
    fastestLap INT,
    rank INT,
    fastestLapTime TEXT,
    fastestLapSpeed REAL,
    statusId INT REFERENCES status(statusId)
);

CREATE TABLE sprint_results (
    resultId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    constructorId INT REFERENCES constructors(constructorId),
    number INT,
    grid INT,
    position INT,
    positionText TEXT,
    positionOrder INT,
    points REAL,
    laps INT,
    time TEXT,
    milliseconds INT,
    fastestLap INT,
    rank INT,
    fastestLapTime TEXT,
    fastestLapSpeed REAL,
    statusId INT REFERENCES status(statusId)
);



CREATE TABLE qualifying (
    qualifyId SERIAL PRIMARY KEY,
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    constructorId INT REFERENCES constructors(constructorId),
    number INT,
    position INT,
    q1 TEXT,
    q2 TEXT,
    q3 TEXT
);



CREATE TABLE lap_times (
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    lap INT,
    position INT,
    time TEXT,
    milliseconds INT,
    PRIMARY KEY (raceId, driverId, lap)
);


CREATE TABLE pit_stops (
    raceId INT REFERENCES races(raceId),
    driverId INT REFERENCES drivers(driverId),
    stop INT,
    lap INT,
    time TIME,
    duration TEXT,
    milliseconds INT,
    PRIMARY KEY (raceId, driverId, stop)
);

