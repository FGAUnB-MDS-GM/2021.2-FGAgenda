$(document).ready(function() {
    var totalCheckboxes = $('input:checkbox').length;
    var totalCheckboxesChecked = 0;

    function checker(elem) {
        if (elem.checked) { 
            totalCheckboxesChecked++;
        } else {
            totalCheckboxesChecked--;
        }
        
        
        if (totalCheckboxes == totalCheckboxesChecked){
            document.getElementsByClassName("checkboxmsg")[0].style.display = "block"
        } else {
            document.getElementsByClassName("checkboxmsg")[0].style.display = "none"
        }
    }  


    $("input[type='checkbox']").click(function(){
        checker(this)
    });

});


