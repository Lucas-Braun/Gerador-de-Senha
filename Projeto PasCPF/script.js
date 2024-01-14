function copyPassword() {
    var passwordText = document.getElementById("generatedPassword").innerText;
    navigator.clipboard.writeText(passwordText)
        .then(function() {
            // Mudar a cor do botão ou ícone para indicar sucesso
            var copyButton = document.querySelector('button[onclick="copyPassword()"]');
            copyButton.classList.add('copied');
            setTimeout(function() { // Remove a classe depois de 2 segundos
                copyButton.classList.remove('copied');
            }, 2000);
        })
        .catch(function(error) {
            console.error('Erro ao copiar senha: ', error);
        });
}
