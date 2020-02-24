function muda(filtertopatual) {
    var filterano = $('#filterano').val();
    var baseUrl   = 'http://localhost:8000/revenuerank/';
    window.location.href = baseUrl + '?filtertop='+ filtertopatual + '&filterano=' + filterano;
};

$( document ).ready(function() {
    var baseUrl   = 'http://localhost:8000/revenuerank/';
    var filterano = $('#filterano');
    $(filterano).change(function() {
        var filterano = $(this).val();
        var filtertop = $('#customSwitch1').val();
        if (!filtertop) {
            filtertop = 'off'
        }
        window.location.href = baseUrl + '?filterano=' + filterano + '&filtertop=' + filtertop;
    });
});
