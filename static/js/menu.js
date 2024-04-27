// Obter o link do "Sócio" pelo ID
var socio = document.getElementById('socio');

// Adicionar um evento de clique ao link do "Sócio"
socio.addEventListener('click', function() {
    var submenu = document.querySelector('.submenu');
    console.log("Clicou no link 'Sócio'");

    // Alternar a exibição do submenu
    if (submenu.style.display === 'block') {
        submenu.style.display = 'none';
    } else {
        submenu.style.display = 'block';
    }

    // Remover a classe 'activate' de todos os links
    var links = document.querySelectorAll('.sidebar a');
    links.forEach(function(link) {
        link.classList.remove('activate');
    });

    // Adicionar a classe 'activate' ao link clicado (Sócio)
    socio.classList.add('activate');
});