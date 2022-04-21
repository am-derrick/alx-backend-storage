-- creates a trigger that resets attribute valid_email
-- only when the email has been changed

DELIMETER $$
CREATE TRIGGER reset_attribute
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END$$
DELIMETER ;$$
