$(document).ready(function() {
    var botao = $('.bt');
    var dropDown = $('.ul_eventos');    
   
       botao.on('click', function(event){
           dropDown.stop(true,true).slideToggle();
           event.stopPropagation();
       });
   });

   $(document).ready(function() {
    var botao = $('.bt2');
    var dropDown = $('.ul_metas');    
   
       botao.on('click', function(event){
           dropDown.stop(true,true).slideToggle();
           event.stopPropagation();
       });
   });