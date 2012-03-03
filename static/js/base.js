$(document).ready(function(){
    $("#menu li a.disabled").live("click", function(e){
        e.preventDefault(); 
    });
    $("#menu li a").tooltip({
        placement:"right",
    });    
});

