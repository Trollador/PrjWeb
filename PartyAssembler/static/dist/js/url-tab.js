var setCurrentPage = function(url) {
    $('h2 span').html(url || "/");
    $("#menu-nav a[href='" + url + "']").fadeTo(500, 0.3);
};

$('#menu-nav a').click(function(e){
    e.preventDefault();
    var targetUrl = $(this).attr('href'),
        targetTitle = $(this).attr('title');

    $("#menu-nav a[href='" + window.location.pathname + "']").fadeTo(500, 1.0);

    window.history.pushState({url: "" + targetUrl + ""}, targetTitle, targetUrl);
    setCurrentPage(targetUrl);
});

window.onpopstate = function(e) {
    $("#menu-nav a").fadeTo('fast', 1.0);
    setCurrentPage(e.state ? e.state.url : null);
};
