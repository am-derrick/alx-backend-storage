-- creates a function SafeDiv that divides the first by the
-- the second number or returns 0 if second number = 0

DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
	RETURN (IF (b = 0, 0, a / b));
END
$$
DELIMITER ;
