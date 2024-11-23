# Detecção de Doenças em Plantas com Visão Computacional

Este repositório contém um projeto de detecção de doenças em plantas utilizando redes neurais convolucionais (CNNs) e o dataset de doenças em plantas disponível no Kaggle. O objetivo é treinar e avaliar modelos para classificar imagens de plantas em saudáveis ou com doenças específicas.

---

## Estrutura do Projeto

A organização do projeto está dividida em várias pastas e arquivos para facilitar a manipulação de dados, treinamento de modelos e análise dos resultados.

### Diretórios Principais

1. **`data/`**  
   - Pasta destinada aos dados brutos e processados. **Esta pasta está ignorada no Git (`.gitignore`) devido ao seu grande tamanho.**
   - Estrutura:
     ```
     data/
     ├── raw/
     │   ├── new-plant-diseases-dataset/
     │   │   ├── New Plant Diseases Dataset(Augmented)/
     │   │   │   ├── train/  # Dados de treino organizados por classes
     │   │   │   ├── valid/  # Dados de validação organizados por classes
     │   │   ├── test/       # Dados de teste com imagens soltas
     ├── processed/          # Dados pré-processados (em desenvolvimento)
     ```
   - **`raw/new-plant-diseases-dataset/train/`**: Contém imagens organizadas em subpastas, onde cada subpasta corresponde a uma classe (exemplo: `Corn_(maize)___healthy`, `Tomato___Early_blight`).
   - **`raw/new-plant-diseases-dataset/test/`**: Imagens soltas para validação posterior do modelo.

2. **`models/`**  
   - Diretório para armazenar os modelos treinados e gráficos gerados.
   - Estrutura:
     ```
     models/
     ├── model_Adam_relu_20241123_173845/
     │   ├── accuracy_by_class.png
     │   ├── accuracy.png
     │   ├── confusion_matrix.png
     │   ├── loss.png
     │   ├── model_architecture.png
     │   ├── plant_disease_model_20241123_174332.h5
     ├── PlantNet-Conv3-Dense128-ReLU-RMSprop_20241123_180649/
     │   ├── accuracy_by_class.png
     │   ├── accuracy.png
     │   ├── confusion_matrix.png
     │   ├── loss.png
     │   ├── model_architecture.png
     │   ├── plant_disease_model_20241123_180928.h5
     ```
   - Cada subpasta contém:
     - **Modelos treinados** (`*.h5`).
     - **Gráficos de performance**:
       - `accuracy.png`, `loss.png`: Acurácia e perda ao longo das épocas.
       - `confusion_matrix.png`: Matriz de confusão.
       - `accuracy_by_class.png`: Acurácia por classe.
       - `precision_recall_f1.png`: Precisão, recall e F1-Score por classe.
       - `predicoes_corretas.png` e `predicoes_erradas.png`: Exemplos de predições corretas e incorretas.
     - **Arquitetura do modelo** (`model_architecture.png`).

3. **`notebooks/`**  
   - Contém notebooks interativos usados para explorar os dados, treinar os modelos e gerar os gráficos.
   - Arquivos principais:
     - `gerar_plot_model.ipynb`: Gera os gráficos da arquitetura do modelo.
     - `treinar_extrair_dados.ipynb`: Treina o modelo e salva os resultados.

4. **Arquivos Raiz**
   - **`requirements.txt`**: Lista de dependências para reproduzir o ambiente do projeto.
   - **`README.md`**: Documentação principal do projeto.
   - **`download_and_unzip.py`**: Script para baixar e descompactar os dados do Kaggle.

---

## Dependências

As dependências necessárias para executar o projeto estão listadas no arquivo `requirements.txt`. Instale-as com o comando:

```bash
pip install -r requirements.txt
```

---

## Como Configurar o Projeto

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-repositorio.git
   cd PAI-Detecao-de-doencas-em-plantas-com-visao-computacional
   ```

2. **Baixar e Preparar os Dados**
   - Certifique-se de ter acesso ao dataset do [Kaggle](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset).
   - Use o script `download_and_unzip.py` para baixar e descompactar os dados:
     ```bash
     python download_and_unzip.py
     ```

3. **Organizar os Dados**
   - Os dados serão salvos na pasta `data/raw/new-plant-diseases-dataset/`. Certifique-se de que a estrutura esteja correta antes de executar os notebooks.

4. **Executar os Notebooks**
   - Abra os notebooks no Jupyter Notebook ou no VSCode.
   - Execute os blocos de código para treinar os modelos e gerar os gráficos.

---

## Resultados Salvos

Os resultados do treinamento (modelos e gráficos) são salvos automaticamente em subpastas do diretório `models/`. Cada subpasta corresponde a um modelo específico, com detalhes sobre:

- Desempenho (gráficos de perda, acurácia e matriz de confusão).
- Arquitetura do modelo.
- Modelos treinados (`*.h5`) para reutilização.

---

## Estrutura de Gráficos

### Exemplos de Gráficos Gerados:

1. **Acurácia e Perda**
   - Mostra o desempenho do modelo ao longo das épocas.

2. **Matriz de Confusão**
   - Avalia a performance de classificação entre classes.

3. **Acurácia por Classe**
   - Permite verificar em quais classes o modelo tem melhor desempenho.

4. **Predições**
   - Exemplos de imagens corretamente e incorretamente classificadas.

5. **Relatório de Métricas**
   - Gráfico de precisão, recall e F1-Score por classe.

---

## Observações

- **Armazenamento de Dados**: A pasta `data/` está no `.gitignore` e não será versionada.
- **Personalização**: Ajuste os hiperparâmetros no notebook `treinar_extrair_dados.ipynb` para explorar diferentes arquiteturas e otimizadores.