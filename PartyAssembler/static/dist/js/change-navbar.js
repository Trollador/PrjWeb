$(document).ready(function(){
      $(window).scroll(function() {
        if ($(document).scrollTop() > 10) {
          $(".skin-yellow .main-header .navbar").css("background-color", "#f8f8f8");
          $(".skin-yellow .main-header .navbar").css("background-color", "transparent");

        }
      }); console.log("oloco");
    });
