---------------------------------------------------------------

-- TASK 5

--------------------------------------------------------------
-- Create related tables

-- Create table for blog posts
CREATE TABLE BlogPosts (
    PostID INT PRIMARY KEY,
    Title VARCHAR(255),
    Content TEXT,
    AuthorID INT,
    Category VARCHAR(50) DEFAULT 'Uncategorized',
    PublishedDate DATETIME,
    Status VARCHAR(10) DEFAULT 'Draft',
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID)
);
-- Create table for users
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(50) NOT NULL UNIQUE,
    Email VARCHAR(100),
    FullName VARCHAR(255),
    Gender VARCHAR(1) DEFAULT 'M',
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- Create table for comments
CREATE TABLE Comments (
    CommentID INT PRIMARY KEY,
    PostID INT,
    AuthorID INT,
    CommentText TEXT,
    CommentDate DATETIME,
    FOREIGN KEY (PostID) REFERENCES BlogPosts(PostID),
    FOREIGN KEY (AuthorID) REFERENCES Users(UserID)
);

--------------------------------------------------------------
-- Create stored procedures

-- Blog posts related procedures
-- Procedure for adding a new post
CREATE PROCEDURE AddBlogPost(
    @Title VARCHAR(255),
    @Content TEXT,
    @AuthorID INT,
    @Category VARCHAR(50) = 'Uncategorized',
    @Status VARCHAR(10) = 'Draft'
)
AS
BEGIN
    INSERT INTO BlogPosts (Title, Content, AuthorID, PublishedDate)
    VALUES (@Title, @Content, @AuthorID, GETDATE());
END;
-- Procedure for getting posts with pagination
CREATE PROCEDURE GetBlogPosts(
    @NumOfPosts INT = 10,
    @Offset INT = 0,
    @Category VARCHAR(50) = NULL,
    @Status VARCHAR(10) = NULL
    @AuthorID INT = NULL
)
AS
BEGIN
    SELECT *
    FROM BlogPosts
    WHERE Category = @Category
        AND Status = @Status
        AND AuthorID = @AuthorID
    ORDER BY PublishedDate DESC
    OFFSET @Offset ROWS
    FETCH NEXT @NumOfPosts ROWS ONLY;
END;

-- Get all posts by id
CREATE PROCEDURE GetBlogPostById(
    @PostID INT
)
AS
BEGIN
    SELECT *
    FROM BlogPosts
    WHERE PostID = @PostID;
END;

-- Update post
CREATE PROCEDURE UpdateBlogPost(
    @PostID INT,
    @Title VARCHAR(255),
    @Content TEXT
)
AS
BEGIN
    UPDATE BlogPosts
    SET Title = @Title,
        Content = @Content
    WHERE PostID = @PostID;
END;

-- Delete post
CREATE PROCEDURE DeleteBlogPost(
    @PostID INT
)
AS
BEGIN
    DELETE FROM BlogPosts
    WHERE PostID = @PostID;
END;

-- Get all posts by user
CREATE PROCEDURE GetAllBlogPostsByUser(
    @AuthorID INT,
)
AS
BEGIN
    SELECT *
    FROM BlogPosts
    WHERE AuthorID = @AuthorID;
END;

-- Set post status to published
CREATE PROCEDURE PublishPost(
    @PostID INT
)
AS
BEGIN
    UPDATE BlogPosts
    SET Status = 'Published'
    WHERE PostID = @PostID;
END;

-- Set post status to draft
CREATE PROCEDURE UnpublishPost(
    @PostID INT
)
AS
BEGIN
    UPDATE BlogPosts
    SET Status = 'Draft'
    WHERE PostID = @PostID;
END;
-------------------
-- Comments related procedures

-- Get number of comments by post
CREATE PROCEDURE GetNumOfCommentsByPost(
    @PostID INT
)
AS
BEGIN
    SELECT COUNT(*) AS NumOfComments
    FROM Comments
    WHERE PostID = @PostID;
END;

-- Add comment
CREATE PROCEDURE AddComment(
    @PostID INT,
    @AuthorID INT,
    @CommentText TEXT
)
AS
BEGIN
    INSERT INTO Comments (PostID, AuthorID, CommentText, CommentDate)
    VALUES (@PostID, @AuthorID, @CommentText, GETDATE());
END;

-- Get comments with pagination
CREATE PROCEDURE GetComments(
    @NumOfComments INT = 10,
    @Offset INT = 0,
    @PostID INT
)
AS
BEGIN
    SELECT *
    FROM Comments
    WHERE PostID = @PostID
    ORDER BY CommentDate DESC
    OFFSET @Offset ROWS
    FETCH NEXT @NumOfComments ROWS ONLY;
END;

-- Get all comments by post
CREATE PROCEDURE GetAllCommentsById(
    @PostID INT
)
AS
BEGIN
    SELECT *
    FROM Comments
    WHERE PostID = @PostID;
END;

-- Get all comments by post id
CREATE PROCEDURE DeleteComment(
    @CommentID INT
)
AS
BEGIN
    DELETE FROM Comments
    WHERE CommentID = @CommentID;
END;

-- Update comment
CREATE PROCEDURE UpdateComment(
    @CommentID INT,
    @CommentText TEXT
)
AS
BEGIN
    UPDATE Comments
    SET CommentText = @CommentText
    WHERE CommentID = @CommentID;
END;