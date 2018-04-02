google.charts.load("current", {packages: ["corechart"]});
google.charts.setOnLoadCallback(drawChart);

window.onresize = function () {
    drawChart();
};

window.onload = function () {
    drawChart();
};

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Kandydat', 'Procentowa liczba głosów'],
        ['GRABOWSKI Dariusz', 89002],
        ['IKONOWICZ Piotr', 38672],
        ['KALINOWSKI Jarosław', 1047949],
        ['KORWIN-MIKKE Janusz', 252499],
        ['KRZAKLEWSKI Marian', 2739621],
        ['KWAŚNIEWSKI Aleksander', 9485224],
        ['LEPPER Andrzej', 537570],
        ['ŁOPUSZAŃSKI Jan', 139682],
        ['OLECHOWSKI Andrzej', 3044141],
        ['PAWŁOWSKI Bogdan', 17164],
        ['WAŁĘSA Lech', 178590],
        ['WILECKI Tadeusz', 28805]
    ]);

    var options = {
        height: 400,
        chartArea: {'width': '80%', 'height': '80%'},
        sliceVisibilityThreshold: .0,
        legend: {position: 'left'},
        fontName: 'Ubuntu'
    };

    var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
    chart.draw(data, options);

}