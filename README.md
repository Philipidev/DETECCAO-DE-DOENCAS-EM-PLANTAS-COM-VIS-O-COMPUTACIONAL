# Projeto de Detecção de Doenças em Plantas

Este projeto tem como objetivo desenvolver um modelo de aprendizado de máquina para detectar e classificar doenças em plantas utilizando imagens. A solução utiliza redes neurais convolucionais (CNNs) e o dataset **New Plant Diseases Dataset** disponível no Kaggle.

---

## **Estrutura do Projeto**

O projeto está organizado nas seguintes pastas:

```
meu_projeto/
├── data/
│   ├── raw/             # Contém os dados brutos (baixados do Kaggle)
│   ├── processed/       # Contém os dados pré-processados
├── notebooks/           # Notebooks Jupyter para exploração e prototipagem
├── src/
│   ├── data/            # Scripts para carregamento e pré-processamento dos dados
│   ├── models/          # Scripts para definição e treinamento dos modelos
│   ├── utils/           # Scripts utilitários
│   ├── visualization/   # Scripts para gerar visualizações
├── models/              # Modelos treinados e checkpoints
├── reports/             # Relatórios e resultados gerados
│   ├── figures/         # Gráficos e imagens geradas
├── download_and_unzip.py # Script para baixar e descompactar os dados do Kaggle
├── README.md            # Documentação do projeto
├── requirements.txt     # Dependências do projeto
└── .gitignore           # Arquivo para ignorar arquivos/pastas desnecessários no Git
```

---

## **Como Iniciar o Projeto**

Siga os passos abaixo para configurar e executar o projeto:

### **1. Instale o Python**

Certifique-se de que o Python **3.6+** está instalado. Você pode baixá-lo [aqui](https://www.python.org/downloads/).

---

### **2. Instale as Bibliotecas Necessárias**

Instale as dependências do projeto com o seguinte comando:

```bash
pip install -r requirements.txt
```

---

### **3. Configure a API do Kaggle**

Para baixar os dados diretamente do Kaggle:

1. Faça login na sua conta do Kaggle.
2. Acesse [My Account](https://www.kaggle.com/account).
3. Na seção **API**, clique em **Create New API Token**.
4. Um arquivo chamado `kaggle.json` será baixado.
5. Mova o arquivo `kaggle.json` para o local apropriado:
   - **Windows**: `%USERPROFILE%\.kaggle\`
   - **Linux/Mac**: `/home/<seu-usuário>/.kaggle/`
6. Certifique-se de que o arquivo possui as permissões corretas:
   - **Linux/Mac**:
     ```bash
     chmod 600 ~/.kaggle/kaggle.json
     ```

---

### **4. Baixe e Prepare os Dados**

Execute o script para baixar e descompactar os dados:

```bash
python download_and_unzip.py
```

O script irá:
- Baixar o dataset do Kaggle.
- Salvar o arquivo ZIP na pasta `data/raw/`.
- Descompactar os dados na pasta `data/raw/`.

---

### **5. Explore os Notebooks**

Use os notebooks na pasta `notebooks/` para explorar os dados e testar os modelos. Para iniciar o Jupyter Notebook, execute:

```bash
jupyter notebook
```

---

### **6. Treine o Modelo**

Após os dados estarem pré-processados e prontos:
- Use os scripts na pasta `src/` para definir, treinar e avaliar o modelo.

---

## **Dependências**

O projeto utiliza as seguintes bibliotecas Python:

- `tensorflow`
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `opencv-python`
- `jupyter`
- `kaggle`

Todas as dependências estão listadas no arquivo `requirements.txt`.

---

## **Próximos Passos**

- Implementar técnicas avançadas de aumento de dados (data augmentation).
- Otimizar a arquitetura do modelo para melhor desempenho.
- Implantar o modelo como uma API web para uso prático.

---

## **Contribuições**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## **Licença**

Este projeto está licenciado sob a licença MIT.

---

## **Contato**

- **Autor**: Philipi Gariglio
- **E-mail**: philipigariglio@gmail.com