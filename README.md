Retrieving Band Information with FastAPI and MusicBrainzNGS
English

This README describes a FastAPI endpoint that retrieves information about a music band from the MusicBrainz database based on the band's name.
Endpoint Functionality

The provided FastAPI endpoint is configured to handle GET requests at /{band_name}, where band_name is a path parameter representing the name of the band you want to search for.
Installation and Setup

Before using this endpoint, ensure that you have installed FastAPI and MusicBrainzNGS as described in the setup guide.
Usage

To use this endpoint, follow these steps:

    Start your FastAPI application (e.g., uvicorn main:app --reload assuming main.py is your main Python file).
    Make a GET request to /{band_name}, where band_name is replaced with the name of the band you want to search for.

The endpoint will query the MusicBrainz database using the provided band name and return the search results in JSON format.

Example:

    If you make a GET request to /metallica, the endpoint will search for the band named "Metallica" on MusicBrainz and return the JSON response containing information about the band.

Português

Este README descreve um endpoint do FastAPI que obtém informações sobre uma banda de música a partir do banco de dados do MusicBrainz com base no nome da banda.
Funcionalidade do Endpoint

O endpoint fornecido pelo FastAPI está configurado para lidar com requisições GET em /{band_name}, onde band_name é um parâmetro de caminho que representa o nome da banda que você deseja pesquisar.
Instalação e Configuração

Antes de usar este endpoint, certifique-se de ter instalado o FastAPI e o MusicBrainzNGS conforme descrito no guia de configuração.
Uso

Para utilizar este endpoint, siga estes passos:

    Inicie a sua aplicação FastAPI (por exemplo, uvicorn main:app --reload assumindo que main.py é o seu arquivo Python principal).
    Faça uma requisição GET para /{band_name}, onde band_name é substituído pelo nome da banda que você deseja pesquisar.

O endpoint irá consultar o banco de dados do MusicBrainz utilizando o nome da banda fornecido e retornará os resultados da busca no formato JSON.

Exemplo:

    Se você fizer uma requisição GET para /metallica, o endpoint irá pesquisar pela banda chamada "Metallica" no MusicBrainz e retornar a resposta JSON contendo informações sobre a banda.
