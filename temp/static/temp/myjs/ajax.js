$('.nav-link').click(function() {
        $("#iframe").attr('src', $(this).attr("href"));
    });