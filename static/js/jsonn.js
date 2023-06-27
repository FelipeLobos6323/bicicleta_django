$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://bicicleta-388ef-default-rtdb.firebaseio.com/",
        function(data){
            $.each(data.categories,function(i,item){
                $("#categorias").append("<tr><td>" + item.idCategory + "</td><td>" + 
                item.strCategory + "</td><td><img src='" + item.strCategoryThumb+
                "'></td><td>" + item.strCategoryDescription+"</td></tr>");
            });
        });
    });
});