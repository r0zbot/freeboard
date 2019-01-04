function saveToServer() {
    freeboard.showLoadingIndicator(true)
    $.ajax({
        url: "save.php", 
        success: function(result){
            console.log(result);
            freeboard.showLoadingIndicator(false)
        },
        error: function (request, error) {
            console.log(request)
            alert("Error while saving: " + error);
            freeboard.showLoadingIndicator(false)
        },
        data: "board="+JSON.stringify(freeboard.serialize(), null, '\t')
    });
}

function loadFromServer() {
    freeboard.showLoadingIndicator(true)
    $.ajax({
        url: "load.php", 
        success: function(result){
            freeboard.loadDashboard(JSON.parse(result), function () {
                freeboard.showLoadingIndicator(false)
            });
        },
    });
}