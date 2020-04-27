## Enunciado

Considere um sistema de apoio ao serviço de embalagem de peças de uma fábrica de porcelana.

O sistema tem um tapete rolante A que recebe as peças à medida que vão sendo produzidas, nomeadamente pratos e chávenas de chá e de café. Os pratos e chávenas de chá são maiores do que os pratos e chávenas de café. O sistema tem também, um tapete B que recebe as embalagens com os pares de peças (prato, chávena).

O sistema tem ainda um robô com dois braços que faz o emparelhamento dos pratos e das chávenas de chá e de café, colocando cada par numa embalagem no tapete B.

As peças chegam ao tapete A por ordem arbitrária e são recolhidas pelo robô por ordem de chegada ao tapete. O robô tem uma mesa de apoio com duas zonas distintas para poder empilhar as peças que vão chegando e que não conseguem ser logo emparelhadas. Cada braço do robô pode manusear uma única peça de cada vez.

O robô deve ser capaz de executar as seguintes ações:

- recolher com o braço direito uma peça do tapete A e:
  - colocá-la na mesa, se não conseguir emparelhar;
  - recolher com o braço esquerdo uma peça da mesa para fazer o emparelhamento das duas peças;
- quando estiver a segurar nos dois braços um par (prato, chávena) de café ou de chá, deve colocar as peças numa embalagem no tapete B.

Pretendemos que desenvolvas uma aplicação em Python que considere o funcionamento do sistema descrito acima.  
Deves adotar o paradigma orientado a objetos, considerando as classes Sistema, Robô, Mesa e as implementações dos TDAs Pilha e Fila, não obstante possas acrescentar mais classes.

* [ ] System
* [ ] Robot
* [ ] Queue
* [ ] Stack (Mesa)

Esta aplicação deve disponibilizar as seguintes funcionalidades, através de um menu:

* [x] F1 – Gerar a fila de peças do tapete A, garantindo que é gerado o mesmo número dos vários tipos de peça.
* [ ] F2 - Mostrar no ecrã o estado dos tapetes, das pilhas e do robô: para o tapete A deve ser mostrada a fila de peças que aguardam ser recolhidas; para o tapete B deve ser mostrada a fila dos pares embalados; para o robô deve ser mostrada a peça que tenha em cada braço e as peças que estão nas duas pilhas de peças da mesa.
* [ ] F3 – Efetuar a recolha de n (n > 0) peças do tapete A para emparelhar.
  * Na recolha de cada peça deve ser mostrada no ecrã:
    * a ação feita pelo robô
      * prato de café recolhido no tapete A é colocado na pilha X da mesa
      * prato de café recolhido no tapete A é emparelhado com chávena de café retirada da pilha Y da mesa
  * Deve haver ainda a possibilidade de recolher todas as peças do tapete A.
* [x] F4 – Mostrar no ecrã o total de peças recolhido pelo robô e o número de embalagens que foram colocadas no tapete B.

https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
