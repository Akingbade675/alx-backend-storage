-- creates a trigger
-- decreases the quantity of an item after adding a new order
delimeter //

CREATE TRIGGER desc_qty AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END//

delimeter ;
