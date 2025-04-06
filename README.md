# 🏆 Labirinto 3D - Computação Gráfica

## 📌 Sobre o Projeto
Este projeto faz parte da disciplina de **Computação Gráfica** e foi desenvolvido pelos alunos:

👤 **Luan Valentino**  
👤 **Mahelvson Bazilio**  
👤 **Jeasiel**  
👤 **Matheus Cavalcante**  

🎯 O objetivo do projeto é criar um **labirinto 3D interativo** utilizando **Python**, **Pygame** e **OpenGL**. O jogador pode explorar o ambiente em primeira pessoa, utilizando controles de teclado e mouse.

---

## 🔄 Contribuições dos Integrantes

👨‍💻 **Luan Valentino**  
- Criou a base do jogo e o repositório no GitHub  
- Desenvolveu o labirinto inicial (sem texturas)  
- Implementou os controles do jogador com mouse e teclado  
- Corrigiu bugs de colisão nas bordas do labirinto  
- Adicionou a função de corrida para o rato  
- Ajustou a altura da câmera para simular a perspectiva de um rato

🎨 **Mahelvson Chaves**  
- Inseriu os modelos de gato e queijo no labirinto  
- Aplicou texturas nos gatos, queijos, paredes e chão  
- Criou o sistema de pontuação e ranking exibido ao fim do jogo

🔊 **Matheus Cavalcante**  
- Implementou sons para eventos importantes do jogo (andar, coletar queijo, ser pego, fim do jogo)  
- Desenvolveu um HUD com contador de queijos e barra de vida do rato

💡 **Jeasiel**  
- (Em andamento) Está desenvolvendo a ampliação do labirinto e a lógica de saída ao pegar todos os queijos (possível buraco na parede ao estilo Tom e Jerry)

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
| **SHIFT** | Corre |
| **ESC** | Pausa o jogo |

---

## 🏗️ Estrutura do Código

```
Labirinto_3D_CG/
│── main.py           # Arquivo principal que inicia o jogo
│── config.py         # Configurações globais do projeto
│── player.py         # Classe do jogador (movimentação e câmera)
│── maze.py           # Geração e renderização do labirinto
│── cat.py            # Comportamento e movimentação dos gatos
│── renderer.py       # Configura e renderiza a cena com OpenGL
│── ranking.txt       # Armazena pontuações
│── README.md         # Documentação do projeto
│
├── assets/           # Recursos utilizados no jogo
│   ├── floor/        # Texturas de chão
│   ├── wall/         # Texturas de parede
│   ├── models/       # Modelos 3D utilizados
│   │   ├── cat/      # Modelo 3D do gato
│   │   ├── cheese/   # Modelo 3D do queijo
│   │   └── heart/    # Ícone de vida
│   └── sounds/       # Sons do jogo
```

📉 **Renderização 3D**: O labirinto é gerado a partir de uma matriz, onde **1** representa paredes e **0** representa caminhos livres.  
📉 **Movimentação do Jogador**: Utiliza trigonometria para permitir a navegação no ambiente 3D.  
📉 **Interação com o Mouse**: O jogador pode girar a câmera movimentando o mouse.

---



## 💡 Ideias de Melhorias Futuras

- 🔁 **Sistema de checkpoints** – permitir que o jogador retorne de onde parou após morrer, em vez de reiniciar tudo.
- 💾 **Salvar e carregar progresso** – criar arquivos de save que guardem posição, vida e queijos coletados.
- 🧠 **IA dos gatos** – tornar os gatos mais inteligentes, seguindo o jogador por som ou visão.
- ⏱️ **Modo Time Attack** – liberar um modo onde o jogador tem que pegar todos os queijos antes que o tempo acabe.
- 🕳️ **Animação de saída secreta** – ao pegar todos os queijos, abrir um buraco animado estilo “Tom e Jerry”.
- 🏅 **Sistema de conquistas** – desbloquear títulos ou medalhas por feitos no jogo (ex: “Pegador de Queijos”, “Ratinho Ninja”).
- 🌌 **Iluminação dinâmica** – lanternas, sombras realistas ou mudanças de luz com base na posição do jogador.
- 📱 **Versão mobile** – adaptar os controles para touchscreen e otimizar desempenho.
- 🕹️ **Suporte a joystick** – permitir jogar com controle USB.
- 🌍 **Geração procedural de labirintos** – criar novos labirintos aleatórios toda vez que o jogador iniciar.






---

## 📜 Licença
📉 Este projeto é de uso educacional e livre para modificação. Sinta-se à vontade para contribuir! 🎯🚀

