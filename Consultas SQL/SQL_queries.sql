--retornar todos os clientes cadastrados

SELECT COUNT(*) AS todos_clientes FROM clientes;

--retornar a quantidade de clientes por cidade

SELECT cidade, COUNT(*) AS qntd_clientes FROM clientes GROUP BY cidade;

--retornar os 5 estados com mais clientes

SELECT estado, COUNT(*) AS qntd_clientes
FROM clientes
GROUP BY estado
ORDER BY qntd_clientes DESC
LIMIT 5;
