# Detecção de Doenças em Plantas com Visão Computacional

Este repositório contém um projeto que utiliza redes neurais convolucionais (CNNs) para a detecção e classificação de doenças em plantas. O objetivo é identificar automaticamente se uma planta está saudável ou apresentar uma doença específica, com base em imagens de folhas.

---

## Estrutura do Projeto

A organização do projeto segue uma estrutura modular, separando dados, modelos, resultados e scripts para facilitar o desenvolvimento e a análise.

### Diretórios Principais

1. **`data/`**  
   - Contém os dados brutos e processados. Esta pasta está ignorada pelo Git (`.gitignore`) devido ao seu grande tamanho.
   - Estrutura:
     ```plaintext
     data/
     ├── raw/
     │   ├── new-plant-diseases-dataset/
     │   │   ├── New Plant Diseases Dataset(Augmented)/
     │   │   │   ├── train/  # Imagens organizadas por classes para treinamento
     │   │   │   ├── valid/  # Imagens organizadas por classes para validação
     │   │   ├── test/       # Imagens soltas para teste final
     ```

2. **`models/`**  
   - Diretório onde são salvos os modelos treinados, gráficos de desempenho e arquitetura.
   - Estrutura:
     ```plaintext
     models/
     ├── model_Adam_relu_20241123_173845/
     │   ├── {ARQUIVOS RESULTANTES DO MODELO}
     ├── PlantNet-Conv3-Dense128-ReLU-RMSprop_20241123_180649/
     ├── PlantNet-DeepConv512-Robust_20241124_172312/
     ```

3. **`notebooks/`**  
   - Contém os notebooks utilizados para treinamento, teste e análise.
   - Arquivos principais:
     - `gerar_plot_model.ipynb`: Gera a visualização da arquitetura do modelo.
     - `treinar_extrair_dados.ipynb`: Executa o treinamento e extrai dados para análise.
     - `testar_modelo.ipynb`: Testa modelos treinados em imagens novas.

4. **`testes/`**  
   - Contém os resultados dos testes realizados com diferentes modelos.
   - Estrutura:
     ```plaintext
     testes/
     ├── model_Adam_relu_20241123_173845/
     ├── PlantNet-Conv3-Dense128-ReLU-RMSprop_20241123_180649/
     ├── PlantNet-DeepConv512-Robust_20241124_172312/
     ```

5. **Arquivos Raiz**
   - **`requirements.txt`**: Lista de bibliotecas e dependências.
   - **`download_and_unzip.py`**: Script para baixar e descompactar os dados.
   - **`.gitignore`**: Exclui arquivos grandes ou desnecessários do controle de versão.

---

## Configuração do Ambiente

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/Philipidev/PAI-Detecao-de-doencas-em-plantas-com-visao-computacional.git

   cd PAI-Detecao-de-doencas-em-plantas-com-visao-computacional
   ```

2. **Instale as Dependências**
   Use o arquivo `requirements.txt` para configurar o ambiente:
   ```bash
   pip install -r requirements.txt
   ```

3. **Baixe e Prepare os Dados**
   Certifique-se de que o dataset [New Plant Diseases Dataset (Kaggle)](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset) esteja disponível. Utilize o script abaixo para automatizar o download:
   ```bash
   python download_and_unzip.py
   ```

4. **Execute os Notebooks**
   Inicie o treinamento ou teste do modelo utilizando os notebooks na pasta `notebooks/`.

---

## Resultados

### Gráficos e Avaliações
Os seguintes gráficos são gerados automaticamente e salvos na pasta do modelo correspondente:

1. **Acurácia e Perda**
   - Mostra o desempenho do modelo ao longo das épocas.

2. **Matriz de Confusão**
   - Avalia os acertos e erros do modelo por classe.

3. **Relatório de Precisão, Recall e F1-Score**
   - Permite entender a performance em métricas detalhadas por classe.

4. **Predições Corretas e Erradas**
   - Exemplos visuais de imagens bem e mal classificadas pelo modelo.

### Modelos Treinados
Os modelos treinados são salvos como arquivos `.h5` e podem ser reutilizados para inferência em novos dados.

---

## Como Personalizar

- **Alteração de Hiperparâmetros**: Ajuste os parâmetros no notebook `treinar_extrair_dados.ipynb` para explorar diferentes configurações de treinamento.
- **Testar Novos Modelos**: Use o `testar_modelo.ipynb` para carregar e testar modelos em dados de teste.

---

## Observações

- **Armazenamento de Dados**: A pasta `data/` é ignorada no controle de versão para evitar problemas com arquivos grandes.
- **Contribuições**: Caso queira contribuir, sinta-se à vontade para enviar pull requests ou reportar problemas.