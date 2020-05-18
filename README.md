# Análise do preco de imoveis
Raspagem de anúncios em sites de imóveis e análise dos dados.

![Gráfico do preço médio de imóveis de aluguel na cidade de Goiânia](./doc/regioes_aluguel.png)

## Funcionalidades:

Crawler:
- Coleta de dados por região
- Opção de seleção de venda ou aluguel
- Rotina de verificação diária

Análise dos dados:
- Mapa com estatísticas por bairro
- Histograma de preço médio de locação/venda
- Histograma do tempo de permanencia do anúncio na plataforma

## Instalação:

Para instalar os requisitos, execute:

```bash
pip3 install -r requirements.txt
```

## Execução do crawler:

O script do crawler baixa da Internet anúcios de aluguel ou venda de imoveis em determinada região.

Na pasta imoveis_crawling execute:

```bash
scrapy crawl IMOVEIS -a category=venda -a region=grande-goiania-e-anapolis -a state=go
```

Você também pode criar uma tarefa que roda em segundo plano e baixa diariamente os anúncios. Para isso execute o script **tasks.py**:

```bash
python3 tasks.py
```

Observação: a máquina que estiver executando o script deve ficar ligada 24h. 

## Análise dos dados:

Foram coletados dados da cidade de Goiânia no período de novembro de 2019 até fevereiro de 2020. O resultado da análise pode ser conferida abaixo:

Preço médio do aluguel dos imóveis:

![alt text](./doc/preco_medio_aluguel.png)


Tipo do imóvel de aluguel:

![alt text](./doc/tipo_imovel_aluguel.png)

Tempo médio do anúncio no ar:

![alt text](./doc/tempo_anuncio_no_ar_aluguel.png)
