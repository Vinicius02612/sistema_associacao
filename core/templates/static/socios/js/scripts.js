//abrir modela centralizado


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

// Função para definir o item do menu ativo com base na URL atual da página
function setActiveMenuItem() {
    // Obtém a URL atual da página
    var currentUrl = window.location.href;

    // Obtém todos os links do menu
    var menuLinks = document.querySelectorAll('.sidebar a');

    // Obtém o último item clicado do menu do armazenamento local
    var lastClickedItem = localStorage.getItem('lastClickedItem');

    // Itera sobre os links do menu
    menuLinks.forEach(function(link) {
        // Obtém o URL do link do menu
        var menuUrl = link.getAttribute('href');

        // Verifica se o URL atual da página contém o URL do link do menu
        if (currentUrl.includes(menuUrl)) {
            // Remove a classe 'activate' de todos os links do menu
            menuLinks.forEach(function(menuLink) {
                menuLink.classList.remove('activate');
            });

            // Adiciona a classe 'activate' ao link do menu correspondente
            link.classList.add('activate');

            // Se o link do menu tiver um submenu, mostra o submenu
            var submenu = link.nextElementSibling;
            if (submenu && submenu.classList.contains('submenu')) {
                submenu.style.display = "block";
            }
        }
    });

    // Se houver um último item clicado, define a classe 'activate' para ele
    if (lastClickedItem) {
        var lastClickedLink = document.getElementById(lastClickedItem);
        if (lastClickedLink) {
            lastClickedLink.classList.add('activate');

            // Se o último item clicado tiver um submenu e não for o 'inicio', mostra o submenu
            if (lastClickedItem !== 'inicio') {
                var submenu = lastClickedLink.nextElementSibling;
                if (submenu && submenu.classList.contains('submenu')) {
                    submenu.style.display = "block";
                }
            }
        }
    }
}

// Função para adicionar evento de clique aos links do menu
function addClickEvent(link, submenu) {
    link.addEventListener('click', function() {
        // Remove a classe 'activate' de todos os links do menu
        var links = document.querySelectorAll('.sidebar a');
        links.forEach(function(link) {
            link.classList.remove('activate');
        });

        // Esconde todos os submenus
        var submenus = document.querySelectorAll('.submenu');
        submenus.forEach(function(submenu) {
            submenu.style.display = "none";
        });

        // Adiciona a classe 'activate' ao link clicado
        link.classList.add('activate');

        // Mostra o submenu correspondente
        if (submenu) {
            submenu.style.display = "block";
        }

        // Salva o ID do link clicado no armazenamento local
        localStorage.setItem('lastClickedItem', link.id);
    });
}

$(document).ready(function() {
    $('#cadastrar').click(function() {
      // Remover classes de cores anteriores
      $('#alerta').removeClass('alert-success alert-warning alert-danger');
      
      // Verificar se o sócio foi cadastrado com sucesso
      var sucesso = true; // Troque isso pela sua lógica real
      if (sucesso) {
        $('#alerta').addClass('alert-success'); // Adiciona classe para cor verde
        $('#alert-text').text('Sócio cadastrado com sucesso');
      } else {
        // Verificar se já existe um sócio cadastrado com esse CPF
        var existe = true; // Troque isso pela sua lógica real
        if (existe) {
          $('#alerta').addClass('alert-warning'); // Adiciona classe para cor amarela
          $('#alert-text').text('Já existe um sócio cadastrado com esse CPF');
        } else {
          $('#alerta').addClass('alert-danger'); // Adiciona classe para cor vermelha
          $('#alert-text').text('Erro ao cadastrar sócio, verifique as informações');
        }
      }
      
      $('#alerta').addClass('show'); // Mostra a notificação
  
      // Remove a notificação após 5 segundos
      setTimeout(function() {
        $('#alerta').removeClass('show');
      }, 4000);
    });
});

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

$(document).on('click', '.btn-atualizar', function() {
    var row = $(this).closest('tr');
    row.find('td:not(:last-child)').prop('contenteditable', true);
    $(this).text('Salvar').removeClass('btn-primary').addClass('btn-success').removeClass('btn-atualizar').addClass('btn-salvar');
    
    row.find('td:not(:last-child)').on('input', function() {
      $(this).addClass('edited');
    });
  });

$(document).on('click', '.btn-salvar', function() {
    var row = $(this).closest('tr');
    row.find('td').prop('contenteditable', false);
    $(this).text('Atualizar').removeClass('btn-success').addClass('btn-primary').removeClass('btn-salvar').addClass('btn-atualizar');
    
    if (row.find('.edited').length > 0) {
      $('#alert-text').text('Alterações salvas com sucesso!');
      $('#alerta').removeClass('alert-warning').addClass('alert-success').removeClass('fade');
    } else {
      $('#alert-text').text('Nenhuma alteração foi feita!');
      $('#alerta').removeClass('alert-success').addClass('alert-warning').removeClass('fade');
    }
    
    row.find('td').removeClass('edited').off('input');
    
    setTimeout(function() {
      $('#alerta').addClass('fade');
    }, 4000);
});

$(document).on('click', '.btn-remover', function() {
    var row = $(this).closest('tr');
    var nome = row.find('td:eq(0)').text(); // obtém o nome do sócio
    if (confirm("Tem certeza que deseja remover o sócio '" + nome + "'?")) {
      row.remove(); // remove a linha da tabela
      $('#alert-text').text('Sócio removido com sucesso!');
      $('#alerta').removeClass('alert-warning').addClass('alert-success').removeClass('fade');
      setTimeout(function() {
        $('#alerta').addClass('fade');
      }, 4000);
    }
});

$('#meuModal').on('shown.bs.modal', function () {
  $('#meuInput').trigger('focus')
})