$(document).ready(function(){

  $('.drop_menu_icon').click(function(){
    if ($('.drop_menu_options').css('display') == 'none'){
      $('.drop_menu_options').fadeIn(300)
    } else {
      $('.drop_menu_options').fadeOut(300)

    }

  })

})