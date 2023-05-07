-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- computes and store the average weighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
  DECLARE user_count, i INT DEFAULT 0;
  SET user_count = (SELECT COUNT(id) FROM users);

  REPEAT

    CALL ComputeAverageWeightedScoreForUser(user_count);
    SET user_count = user_count - 1;

  UNTIL user_count = 0 END REPEAT;

END//

DELIMITER ;
