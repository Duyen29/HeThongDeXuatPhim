USE BTL1
CREATE DATABASE MovieDB;
GO

USE MovieDB;
GO

CREATE TABLE Movies (
    movie_id INT PRIMARY KEY,
    title NVARCHAR(255),
    release_date DATE,
    overview NVARCHAR(MAX),
    vote_average FLOAT,
    vote_count INT
);
GO


CREATE PROCEDURE InsertMovie 
    @movie_id INT,
    @title NVARCHAR(255),
    @release_date DATE,
    @overview NVARCHAR(MAX),
    @vote_average FLOAT,
    @vote_count INT
AS
BEGIN
    INSERT INTO Movies (movie_id, title, release_date, overview, vote_average, vote_count)
    VALUES (@movie_id, @title, @release_date, @overview, @vote_average, @vote_count);
END
GO