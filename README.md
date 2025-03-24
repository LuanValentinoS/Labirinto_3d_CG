# Labirinto 3D - Computação Gráfica

## Sobre o Projeto
Este projeto faz parte da disciplina de **Computação Gráfica** e foi desenvolvido pelos alunos:

- **Luan Valentino**
- **Mahelvson Bazilio**
- **Jeasiel**
- **Matheus Cavalcante**

O objetivo do projeto é criar um **labirinto 3D interativo** utilizando **Python**, **Pygame** e **OpenGL**. O jogador pode navegar pelo labirinto em primeira pessoa com controles de teclado e mouse.

---

## Tecnologias Utilizadas
- **Python**
- **Pygame** (para manipulação de eventos e janelas)
- **OpenGL** (para renderização 3D)
- **NumPy** (para manipulação da matriz do labirinto)

---

## Como Executar o Projeto
### **1. Instale as dependências**
Antes de rodar o projeto, certifique-se de ter o Python instalado e instale as bibliotecas necessárias com o seguinte comando:
```bash
pip install pygame PyOpenGL numpy
```

### **2. Execute o script**
Após instalar as dependências, execute o seguinte comando:
```bash
python main.py
```

---

## Controles do Jogo
- **W** - Move para frente
- **S** - Move para trás
- **A** - Move para a esquerda
- **D** - Move para a direita
- **Mouse** - Controla a direção da câmera
- **ESC** - Fecha o jogo

---

## Estrutura do Código
O projeto conta com os seguintes componentes principais:

- **Renderização 3D**: O labirinto é gerado a partir de uma matriz, onde **1** representa paredes e **0** representa caminhos livres.
- **Movimentação do jogador**: Utiliza trigonometria para permitir a navegação em um ambiente 3D.
- **Interação com o mouse**: O jogador pode girar a câmera movimentando o mouse.

---

## Melhorias Futuras
- Adicionar objetos.
- Adicionar texturas nas paredes.
- Adicionar textura no personagem (para que pelo menos apareça as mãos).
- Adicionar um céu e um chão texturizados (se possível).
- Adicionar alguns efeitos sonoros.
- Colocar a tela inicial de jogo.
- Colocar um início e fim para o labirinto (além de aumentar o tamanho do mesmo).

---

## Licença
Este projeto é de uso educacional e livre para modificação.

