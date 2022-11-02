CREATE DATABASE solar_system_development;
CREATE TABLE Planet (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT,
    description TEXT,
    size VARCHAR(20)

);
