;(function(){
  $('.menu-table > tbody > tr').hover(function(e) {
   var disk = $(e.currentTarget).data('img')
   var imgURL = "../theme/img/menu/disks/" + disk

   $('img.disk').attr('src', imgURL)
  });
})(jQuery)
