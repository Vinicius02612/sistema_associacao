      
$(document).ready(function() {
      $('#cadastrar').click(function() {
        $('#alerta').addClass('show'); // Mostra a notificação
    
        // Remove a notificação após 5 segundos
        setTimeout(function() {
          $('#alerta').removeClass('show');
        }, 4000);
      });
});