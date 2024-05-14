$(document).ready(function() {
    // Adiciona um evento de clique ao primeiro card
    $('#card1').click(function() {
        // Remove a classe 'activate' de todos os itens de menu
        $('.sidebar a').removeClass('activate');
        // Adiciona a classe 'activate' ao item 'Sócio' e ao submenu 'Adicionar'
        $('#socio').addClass('activate');
        $('#submenu-socio').addClass('activate');
        // Salva o último item clicado no armazenamento local
        localStorage.setItem('lastClickedItem', 'socio');
    });

    // Define o item de menu ativo com base no armazenamento local
    var lastClickedItem = localStorage.getItem('lastClickedItem');
    if (lastClickedItem) {
        $('#' + lastClickedItem).addClass('activate');
        $('#submenu-' + lastClickedItem).addClass('activate');
    }
});

 // Obter os links e submenus pelo ID e adicionar eventos de clique
 window.addEventListener('load', function() {
    var inicio = document.getElementById('inicio');
    var socio = document.getElementById('socio');
    var projetos = document.getElementById('projetos');
    var mensalidade = document.getElementById('mensalidade');

    var submenuSocio = document.getElementById('submenu-socio');
    var submenuProjetos = document.getElementById('submenu-projetos');
    var submenuMensalidade = document.getElementById('submenu-mensalidade');

    addClickEvent(inicio);
    addClickEvent(socio, submenuSocio);
    addClickEvent(projetos, submenuProjetos);
    addClickEvent(mensalidade, submenuMensalidade);

    setActiveMenuItem();
});