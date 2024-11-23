import os
import zipfile
import kaggle

def baixar_dados(kaggle_dataset, output_dir):
    """
    Baixa um dataset do Kaggle e salva no diretório especificado.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    os.system(f"kaggle datasets download -d {kaggle_dataset} -p {output_dir}")
    print(f"Dataset baixado em: {output_dir}")

def descompactar_zip(zip_file, extract_to):
    """
    Descompacta o arquivo ZIP no diretório especificado.
    """
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Arquivos extraídos para: {extract_to}")

if __name__ == "__main__":
    # Configurações
    kaggle_dataset = "vipoooool/new-plant-diseases-dataset"  # Substitua pelo ID do dataset no Kaggle
    output_dir = "data/raw"  # Diretório para salvar o arquivo baixado
    zip_file_path = os.path.join(output_dir, "new-plant-diseases-dataset.zip")
    extract_to = "data/raw"  # Diretório para onde os arquivos serão extraídos

    # Baixar os dados do Kaggle
    print("Baixando dataset do Kaggle...")
    baixar_dados(kaggle_dataset, output_dir)

    # Descompactar o ZIP
    print("Descompactando os arquivos...")
    descompactar_zip(zip_file_path, extract_to)
