-- creates a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN users_id INT)
BEGIN
  DECLARE average_score FLOAT;

  SET average_score = (SELECT AVG(score) FROM `corrections` WHERE `user_id` = users_id);
  
  UPDATE `users` SET average_score = average_score WHERE `id` = users_id;
END//
DELIMITER ;
