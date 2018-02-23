
  $(document).ready(function() {
    $('.carousel').carousel({
      interval: 6000
    })
  });

  $(document).ready(function(){
    //Handles menu drop down
    $('.dropdown-menu').find('form').click(function (e) {
        e.stopPropagation();
    });
});