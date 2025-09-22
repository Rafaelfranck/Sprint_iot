Rafael Franck (RM550875), Gabriela Trevisan (RM99500), Eduardo Araujo (RM99758) e Leonardo Bonini (RM551716)

## Objetivo
Aplicação local em Python que realiza **detecção facial em tempo real** usando **OpenCV + Haar Cascade**.  
O usuário pode ajustar parâmetros ao vivo (sliders) para visualizar o impacto no resultado da detecção.

## Estrutura do Projeto
facial-recognition-demo/
├─ .venv/ # ambiente virtual
├─ data/ # snapshots salvos
├─ src/ # códigos-fonte
│ └─ detect_haar.py # script principal com Haar Cascade
├─ .gitignore
├─ README.md
└─ requirements.txt

## Como Executar

Clonar e configurar o ambiente
bash
git clone https://github.com/Rafaelfranck/Sprint_iot.git
cd iot_project

### Criar e ativar ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate 

# Instalar dependências
pip install -r requirements.txt

# Rodar o detector facial
python src/detect_haar.py

### Sliders:

- scaleFactor: controla sensibilidade da detecção

- minNeighbors: ajusta rigor (menos falsos positivos x perda de faces)

- minSize: ignora rostos menores que o valor em pixels

### Teclas:

q → sair

s → salvar snapshot na pasta data/

### Limitações

- Sensível a iluminação e ângulos da câmera

- Haar Cascade é rápido, mas menos robusto que modelos modernos

- Não realiza identificação (quem é quem), apenas detecção

### Próximos Passos

- Adicionar reconhecimento de identidade (LBPH, embeddings)

- Criar interface gráfica amigável

### Nota Ética

- O uso de dados faciais deve respeitar a LGPD/GDPR

- Sempre obter consentimento antes de capturar/armazenar imagens

- Processar dados localmente, evitando envio a terceiros
