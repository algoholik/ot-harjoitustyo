CREATE TABLE Notes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    content TEXT,
    timestamp TIMESTAMP
);

CREATE TABLE Snips (
    id INTEGER PRIMARY KEY,
    name TEXT,
    content TEXT,
    timestamp TIMESTAMP
);

CREATE TABLE Tags (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    timestamp TIMESTAMP
);

CREATE TABLE Tagging (
    id INTEGER PRIMARY KEY,
    snip_id INTEGER REFERENCES Snips,
    tag_id INTEGER REFERENCES Tags,
    timestamp TIMESTAMP
);

CREATE TABLE Cats (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    timestamp TIMESTAMP
);

CREATE TABLE Catting (
    id INTEGER PRIMARY KEY,
    note_id INTEGER REFERENCES Notes,
    cat_id INTEGER REFERENCES Cats,
    timestamp TIMESTAMP
);
