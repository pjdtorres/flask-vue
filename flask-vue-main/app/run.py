from my_app import app

if __name__ == "__main__":
    # Força o Flask a recarregar templates HTML sem precisar reiniciar
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.jinja_env.auto_reload = True
    
    # Define o cache de ficheiros (CSS/JS) como zero para veres as cores mudarem na hora
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    
    print(app.url_map)
    # O comando correto para rodar o servidor
    # Removi o segundo app.run() porque ele entraria em conflito
    app.run(host="127.0.0.1", port=5000, debug=True)