-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- computes and store the average weighted score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN users_id INT)
BEGIN
  DECLARE weighted_average FLOAT;

  SET weighted_average = (SELECT SUM(score * weight)/SUM(weight) FROM corrections JOIN projects ON projects.id = corrections.project_id WHERE user_id = users_id);

  UPDATE users SET average_score = weighted_average WHERE id = users_id;
END//

DELIMITER ;
