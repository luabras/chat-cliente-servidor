# chat-cliente-servidor
Aplicação de chat cliente e servidor no formato de sala de bate papo, ou seja, quando um cliente envia uma mensagem todos os outros clientes a recebem. 

* O servidor suporta múltiplos clientes simultâneos; 

* Existem duas versões, uma utilizando socket bloqueante e outra não bloqueante;

* Feito em python 2.7;

* Roda somente em Linux, pois a função select do não-bloqueante não é reconhecida pelo Windows;

* O client do não-bloqueante deve ser rodado especificando o localhost 5000.


