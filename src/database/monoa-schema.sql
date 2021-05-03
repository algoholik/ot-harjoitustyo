CREATE TABLE Notes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    contents TEXT,
    modified TIMESTAMP
);

CREATE TABLE Snips (
    id INTEGER PRIMARY KEY,
    sniptype INTEGER DEFAULT 0,
    content TEXT,
    modified TIMESTAMP
);

CREATE TABLE Categories (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    modified TIMESTAMP
);

CREATE TABLE Categorisation (
    id INTEGER PRIMARY KEY,
    note_id INTEGER REFERENCES Notes,
    category_id INTEGER REFERENCES Categories
);

CREATE TABLE Tags (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    modified TIMESTAMP
);

CREATE TABLE Tagging (
    id INTEGER PRIMARY KEY,
    snip_id INTEGER REFERENCES Snips,
    tag_id INTEGER REFERENCES Tags
);
