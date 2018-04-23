
$("a[name='spider_switch']").click(function(){
    //This stops the page scrolling to the top on a # link.
    if($(this).hasClass('button special')){
        if(confirm("是否停止爬虫？")){
            $(this).removeClass('button special');
            $(this).addClass('button');
            $(this).text('Start');
        }else{
            return false;
        }
    }
    else{
        if(confirm("是否开始爬虫？")){
            $(this).removeClass('button');
            $(this).addClass('button special');
            $(this).text('Stop');
        }else{
            return false;
        }
    }
});