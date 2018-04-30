// 用于点击侧边栏时对iframe进行跳转
$('.nav-link').click(function() {
        $("#iframe").attr('src', $(this).attr("href"));
    });

