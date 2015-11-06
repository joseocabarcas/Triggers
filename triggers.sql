DELIMITER // 
CREATE TRIGGER insert_auditorias 
AFTER INSERT ON empleados_empleado FOR EACH ROW 
BEGIN 
INSERT INTO auditorias_auditoria 
(operacion, fechahora, usuario) 
VALUES ("INSERT",NOW(),NEW.usuario);
END// 
DELIMITER ; 




DELIMITER // 
CREATE TRIGGER update_auditorias 
AFTER UPDATE ON empleados_empleado FOR EACH ROW 
BEGIN 
INSERT INTO auditorias_auditoria 
(operacion, fechahora, usuario) 
VALUES ("UPDATE",NOW(),NEW.usuario);
END// 
DELIMITER ; 



DELIMITER // 
CREATE TRIGGER delete_auditorias 
AFTER DELETE ON empleados_empleado FOR EACH ROW 
BEGIN 
INSERT INTO auditorias_auditoria 
(operacion, fechahora, usuario) 
VALUES ("DELETE",NOW(),OLD.usuario);
END// 
DELIMITER ; 



