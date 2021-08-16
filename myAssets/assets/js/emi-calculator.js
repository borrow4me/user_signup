(function($) {

    $("#amount-slide", "#amount-slide2").slider({
        range: "min",
        min: 5000, // set minimun amount
        max: 5000000, // set maximum amount
        value: 50000, // set default amount value
        step: 1000, // set amount step
        slide: function(event, ui) {
            $("#amount", "#amount2").text(ui.value);
            emicalculate();
        }
    });
    $("#amount", "#amount2").text($("#amount-slide", "#amount-slide2").slider("value"));

    $("#duration-slide", "#duration-slide2").slider({
        range: "min",
        min: 1, // set minimun month
        max: 12, // set maximum month
        step: 1, // set month step
        value: 1, // set default month value
        slide: function(event, ui) {
            $("#duration", "#duration2").text(ui.value);
            emicalculate();
        }
    });
    $("#duration", "#duration2").text($("#duration-slide", "#duration-slide2").slider("value"));

    $("#intrest-slide", "#intrest-slide2").slider({
        range: "min",
        min: 6.10, // set minimun rate of interest
        max: 16.20, // set maximum rate of interest
        step: 0.01, // set rate of interest step
        value: 10, // set default rate of interest
        slide: function(event, ui) {
            $("#intrest", "#intrest2").text(ui.value);
            emicalculate();
        }
    });
    $("#intrest", "#intrest2").text($("#intrest-slide", "#intrest-slide2").slider("value"));

    emicalculate();
})(jQuery);

function emicalculate() {
    var loanAmount = $("#amount", "#amount2").text();
    var numberOfMonths = $("#duration", "#duration2").text();
    var rateOfInterest = $("#intrest", "#intrest2").text();
    var monthlyInterestRatio = (rateOfInterest / 100) / 12;
    var top = Math.pow((1 + monthlyInterestRatio), numberOfMonths);
    var bottom = top - 1;
    var sp = top / bottom;
    var emi = ((loanAmount * monthlyInterestRatio) * sp);
    var full = numberOfMonths * emi;
    var interest = full - loanAmount;
    var int_pge = (interest / full) * 100;
    var emi_str = emi.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var loanAmount_str = loanAmount.toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var full_str = full.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    var int_str = interest.toFixed(2).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",");

    $("#emi", "#emi2").html(emi_str);
    $("#tbl_emi", "#tbl_emi2").html(int_str);
    $("#tbl_la", "#tbl_la").html(full_str);
}