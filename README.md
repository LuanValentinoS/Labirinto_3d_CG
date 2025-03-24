# 🏆 Labirinto 3D - Computação Gráfica

## 📌 Sobre o Projeto
Este projeto faz parte da disciplina de **Computação Gráfica** e foi desenvolvido pelos alunos:

👤 **Luan Valentino**  
👤 **Mahelvson Bazilio**  
👤 **Jeasiel**  
👤 **Matheus Cavalcante**  

🎯 O objetivo do projeto é criar um **labirinto 3D interativo** utilizando **Python**, **Pygame** e **OpenGL**. O jogador pode explorar o ambiente em primeira pessoa, utilizando controles de teclado e mouse.

---

## 🛠️ Tecnologias Utilizadas
- 🐍 **Python**
- 🎮 **Pygame** (manipulação de eventos e janelas)
- 🎥 **OpenGL** (renderização 3D)
- 📊 **NumPy** (manipulação da matriz do labirinto)

---

## 🚀 Como Executar o Projeto
### **1⃣ Instale as dependências**
Certifique-se de ter o Python instalado e execute o seguinte comando:
```bash
pip install pygame PyOpenGL numpy
```

### **2⃣ Execute o jogo**
Após instalar as dependências, rode o jogo com:
```bash
python main.py
```

---

## 🎮 Controles do Jogo
| Tecla  | Ação |
|--------|------|
| **W**  | Move para frente |
| **S**  | Move para trás |
| **A**  | Move para a esquerda |
| **D**  | Move para a direita |
| **Mouse** | Controla a direção da câmera |
| **ESC** | Fecha o jogo |

---

## 🏗️ Estrutura do Código
Para melhorar a organização, o projeto foi dividido nos seguintes arquivos:

```
Labirinto_3D_CG/
│── main.py          # Arquivo principal que inicia o jogo
│── config.py        # Configurações globais (tamanho da tela, FOV, etc.)
│── player.py        # Classe do jogador (posição, movimentação e câmera)
│── maze.py          # Geração e renderização do labirinto
│── renderer.py      # Configura e renderiza a cena OpenGL
│── README.md        # Documentação do projeto
```

📉 **Renderização 3D**: O labirinto é gerado a partir de uma matriz, onde **1** representa paredes e **0** representa caminhos livres.  
📉 **Movimentação do Jogador**: Utiliza trigonometria para permitir a navegação no ambiente 3D.  
📉 **Interação com o Mouse**: O jogador pode girar a câmera movimentando o mouse.

---

## 🚧 Melhorias Futuras
✅ Adicionar objetos no cenário.  
✅ Adicionar texturas nas paredes.  
✅ Adicionar textura no personagem (para que pelo menos apareçam as mãos).  
✅ Criar um céu e um chão texturizados.  
✅ Adicionar efeitos sonoros.  
✅ Implementar uma tela inicial para o jogo.  
✅ Criar um início e fim para o labirinto (e aumentar seu tamanho).  

---

## 📜 Licença
📉 Este projeto é de uso educacional e livre para modificação. Sinta-se à vontade para contribuir! 🎯🚀

