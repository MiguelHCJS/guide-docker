# Anotações Docker

## 1.Estrutura

    ├── Dockerfile
    ├── docs
    │   ├── assets
    │   │   └── logo.png
    │   ├── index.md
    │   └── main.md
    ├── guide_docker
    │   ├── _dev.ipynb
    │   ├── __init__.py
    │   └── main.py
    ├── mkdocs.yml
    ├── poetry.lock
    ├── pyproject.toml
    └── README.md

## Containers

### Gerenciamento de contêineres

- docker container ls: Lista os contêineres em execução, parados e todos.
- docker container start **container_name_or_id**: Inicia um contêiner parado.
- docker container stop **container_name_or_id**: Para um contêiner em execução.
- docker container restart **container_name_or_id**: Reinicia um contêiner em execução.
- docker container pause **container_name_or_id**: Pausa um contêiner em execução (congela todos os processos).
- docker container unpause **container_name_or_id**: Retoma um contêiner pausado.
- docker container kill **container_name_or_id**: Envia um sinal SIGKILL para o processo principal do contêiner, parando-o imediatamente.
- docker container rm **container_name_or_id**: Remove um contêiner, mesmo que esteja parado.

### Inspeção de contêineres:

- docker container inspect **container_name_or_id**: Exibe informações detalhadas sobre um contêiner.
- docker container logs **container_name_or_id**: Mostra os logs do contêiner.
- docker container top **container_name_or_id**: Exibe os processos em execução dentro do contêiner.

- Executando comandos em contêineres:
- docker run -it **image_name**: Inicia um contêiner interativo a partir de uma imagem.
- docker container exec -it **container_name_or_id** **command**: Executa um comando no terminal interativo dentro de um contêiner em execução.

## Image

### Gerenciando imagens

- docker images: Lista todas as imagens Docker locais, incluindo repositório, tag, ID da imagem e tamanho.
- docker image pull **nome_da_imagem**: Baixa uma imagem de um registro Docker (como o Docker Hub) para a sua máquina local.
- docker image push **nome_da_imagem**: Envia uma imagem que você construiu para um registro Docker.
- docker image tag **nome_da_imagem** **novo_nome_da_imagem**: Cria uma tag para uma imagem existente.
- docker image rmi **nome_da_imagem**: Remove uma imagem da sua máquina local.

### Inspecionando imagens

- docker image inspect **nome_da_imagem**: Exibe informações detalhadas sobre uma imagem, incluindo suas camadas, variáveis de ambiente e histórico.
- docker image history **nome_da_imagem**: Mostra o histórico de uma imagem, incluindo os comandos usados para construir cada camada.

### Construindo imagens

- docker build -t **nome_da_imagem** .: Constrói uma imagem Docker a partir do Dockerfile presente no diretório de trabalho atual. Você pode especificar uma tag para a imagem usando a opção -t.

### Outros comandos úteis

- docker image load **arquivo_tar_da_imagem**: Carrega uma imagem de um arquivo tar para o daemon Docker local.
- docker image save **nome_da_imagem** [**arquivo_tar_de_destino**]: Salva uma imagem em um arquivo tar.
- docker image search **termo_de_busca**: Procura por imagens no Docker Hub com base em uma palavra-chave.

## Volumes

Faz a persistência de dados em um container.

### Tipos

BIND

Estes volumes mapeiam um diretório do host para um diretório dentro do container. Isso significa que qualquer alteração feita nos arquivos dentro do container também será refletida no diretório do host. São ideais para situações em que você precisa acessar arquivos do host dentro do container. Por exemplo, se você estiver desenvolvendo um aplicativo web, você pode usar um volume bind para mapear o diretório do seu código fonte para dentro do container.

      docker container run -ti --mount type=bind,src=/nome/diretorio/bind,dst=/nome/diretorio/destino/montagem [imagem]

VOLUME

Estes volumes são gerenciados pelo Docker e não estão diretamente ligados a nenhum diretório no host. Isso significa que os dados dentro do volume são persistentes, mesmo que o container seja removido. São ideais para situações em que você precisa armazenar dados persistentes que não precisam ser acessados diretamente do host. Por exemplo, se você estiver executando um banco de dados MySQL, você pode usar um volume volume para armazenar os dados do banco de dados.

      docker volume create [nome]
      docker container run -ti --mount type=volume,src=[nome],dst=[path_destino_montagem] [imagem]

### Gerenciando volumes

- docker volume ls: Lista todos os volumes conhecidos pelo Docker.
- docker volume create [nome_do_volume]: Cria um novo volume.
- docker volume inspect [nome_do_volume]: Exibe informações detalhadas sobre um volume.
- docker volume prune: Remove volumes que não estão sendo usados por nenhum contêiner.
- docker volume rm [nome_do_volume]: Remove um volume manualmente (desde que não esteja em uso).

### Montando volumes em contêineres

Ao executar um contêiner, você pode usar a opção -v para montar um volume no contêiner. Por exemplo, docker run -v meu_volume:/app minha_imagem monta o volume meu_volume no diretório /app dentro do contêiner.
