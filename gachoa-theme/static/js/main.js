;(function(){
  buildMail = function() {
    return ['ma', 'ilt', 'o', ':m', 'e', '@', 'qua', 'ng.b', 'e'].join('')
  }
  $('li.mail-footer')
  .on('mouseenter', function(e){
    var mail = $(e.currentTarget)
    if (mail.find('a').length === 0) {
      mail.html('<a href="'+ buildMail() + '">mail</a>')
    }
  })

  blinkContact = function(depth) {
    console.log('blink')
    var contact = $('#contact')
    if (contact.hasClass('contact-active')) {
      contact.removeClass('contact-active')
    } else {
      contact.addClass('contact-active')
    }
    window.setTimeout(function(){
      if (depth < 5) {
        console.log(depth)
        blinkContact(depth+1)
      }
    }, 100)
  }

  $('a.link-contact').on('click', function(e) {
    var depth = 0
    blinkContact(depth)
  })

})(jQuery)
