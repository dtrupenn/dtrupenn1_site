$('a').click(function(){
        $('html, body').animate({
            scrollTop: $( $(this).attr('href') ).offset().top
        }, 1500);
        return false;
});



React.render(
  React.createElement(Dashboard, null),
  document.getElementById('content')
);

