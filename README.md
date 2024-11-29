# Spotify Paradigmas

## Configuração do Ambiente

1. **Criar o arquivo `.env`**  
   No diretório do projeto, crie um arquivo chamado `.env` e preencha com as seguintes variáveis de ambiente:  

   ```
   SPOTIPY_CLIENT_ID=
   SPOTIPY_CLIENT_SECRET=
   SPOTIPY_REDIRECT_URI=
   SPOTIPY_SCOPE=
   ```

   Preencha os valores conforme as instruções abaixo.

2. **Configuração na Dashboard do Spotify**  
   Acesse o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) e siga os passos:  
   - Crie um projeto com um nome e descrição à sua escolha.  
   - Após a criação, copie o **Client ID** e o **Client Secret** para o `.env`.  
   - Configure o campo "Redirect URI" com o valor: `http://localhost:8888/callback` na API e no arquivo `.env` .  
   - Marque a opção **WEB API**.  
   - No campo de escopos (SPOTIPY_SCOPE), inclua:  
     ```
     user-modify-playback-state user-read-playback-state
     ```

3. **Instalação das Dependências**  
   Certifique-se de ter o `pip` configurado e execute o seguinte comando para instalar as dependências:  
   ```
   pip install python-dotenv spotipy threading time
   ```

## Uso do Programa

- Certifique-se de que sua conta Spotify esteja ligada.
- Escolha uma música e ela será reproduzida diretamente na conta autenticada.  
