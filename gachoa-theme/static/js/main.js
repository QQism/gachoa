;(function(){
  $('.menu-table > tbody > tr').hover(function(e) {
    var disk = $(e.currentTarget).data('img')
    var imgURL = "../theme/img/menu/disks/" + disk

    $('img.disk').css('display', 'none')
    $('img.waiting').css('display', 'inline')

    $('img.disk').load(function() {
      $('img.disk').fadeIn()
      $('img.disk').css('display', 'inline')
      $('img.waiting').css('display', 'none')
    }).error(function() {
      $('img.waiting').css('display', 'none')
    })

    $('img.disk').attr('src', imgURL)
  });

  $('.menu-table > tbody > tr').mouseleave(function(e) {
      $('img.waiting').css('display', 'none')
  })

})(jQuery)
