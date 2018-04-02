AmCharts.makeChart("map", {
    "type": "map",
    "dragMap": false,
    "zoomOnDoubleClick": false,
    "pathToImages": "http://www.amcharts.com/lib/3/images/",
    "addClassNames": true,
    "fontSize": 15,
    "color": "#000000",
    "projection": "mercator",
    "backgroundAlpha": 1,
    "backgroundColor": "rgba(255,255,255,1)",
    "dataProvider": {
        "map": "polandLow",
        "getAreasFromMap": true,
        "areas": [
            {
                "id": "PL-DS",
                "title": "Dolnośląskie",
                "url": "../output/województwa/Dolnośląskie.html"
            },
            {
                "id": "PL-KP",
                "title": "Kujawsko-Pomorskie",
                "url": "../output/województwa/Kujawsko-Pomorskie.html"
            },
            {
                "id": "PL-LD",
                "title": "Łódzkie",
                "url": "../output/województwa/Łódzkie.html"
            },
            {
                "id": "PL-LU",
                "title": "Lubelskie",
                "url": "../output/województwa/Lubelskie.html"
            },
            {
                "id": "PL-LB",
                "title": "Lubuskie",
                "url": "../output/województwa/Lubuskie.html"
            },
            {
                "id": "PL-MA",
                "title": "Małopolskie",
                "url": "../output/województwa/Małopolskie.html"
            },
            {
                "id": "PL-MZ",
                "title": "Mazowieckie",
                "url": "../output/województwa/Mazowieckie.html"
            },
            {
                "id": "PL-OP",
                "title": "Opolskie",
                "url": "../output/województwa/Opolskie.html"
            },
            {
                "id": "PL-PK",
                "title": "Podkarpackie",
                "url": "../output/województwa/Podkarpackie.html"
            },
            {
                "id": "PL-PD",
                "title": "Podlaskie",
                "url": "../output/województwa/Podlaskie.html"
            },
            {
                "id": "PL-PM",
                "title": "Pomorskie",
                "url": "../output/województwa/Pomorskie.html"
            },
            {
                "id": "PL-SL",
                "title": "Śląskie",
                "url": "../output/województwa/Śląskie.html"
            },
            {
                "id": "PL-SK",
                "title": "Świętokrzyskie",
                "url": "../output/województwa/Świętokrzyskie.html"
            },
            {
                "id": "PL-WN",
                "title": "Warmińsko-Mazurskie",
                "url": "../output/województwa/Warmińsko-Mazurskie.html"
            },
            {
                "id": "PL-WP",
                "title": "Wielkopolskie",
                "url": "../output/województwa/Wielkopolskie.html"
            },
            {
                "id": "PL-ZP",
                "title": "Zachodniopomorskie",
                "url": "../output/województwa/Zachodniopomorskie.html"
            }
        ],
        "images": [
            {
                "top": 40,
                "left": 60,
                "width": 80,
                "height": 40,
                "pixelMapperLogo": true,
                "imageURL": "http://pixelmap.amcharts.com/static/img/logo-black.svg",
                "url": "http://www.amcharts.com"
            }
        ]
    },
    "balloon": {
        "horizontalPadding": 15,
        "borderAlpha": 0,
        "borderThickness": 1,
        "verticalPadding": 15
    },
    "areasSettings": {
        "color": "rgba(16,78,139,1)",
        "outlineColor": "rgba(255,255,255,1)",
        "rollOverOutlineColor": "rgba(255,255,255,1)",
        "rollOverBrightness": 50,
        "selectedBrightness": 60,
        "selectable": true,
        "unlistedAreasAlpha": 0,
        "unlistedAreasOutlineAlpha": 0
    },
    "imagesSettings": {
        "alpha": 1,
        "color": "rgba(16,78,139,1)",
        "outlineAlpha": 0,
        "rollOverOutlineAlpha": 0,
        "outlineColor": "rgba(255,255,255,1)",
        "rollOverBrightness": 50,
        "selectedBrightness": 60,
        "selectable": true
    },
    "linesSettings": {
        "color": "rgba(16,78,139,1)",
        "selectable": true,
        "rollOverBrightness": 50,
        "selectedBrightness": 60
    },
    "zoomControl": {
        "zoomControlEnabled": false,
        "homeButtonEnabled": false,
        "panControlEnabled": false,
        "right": 38,
        "bottom": 30,
        "minZoomLevel": 1.00,
        "maxZoomLevel": 1.00,
        "gridHeight": 100,
        "gridAlpha": 0.1,
        "gridBackgroundAlpha": 0,
        "gridColor": "#FFFFFF",
        "draggerAlpha": 1,
        "buttonCornerRadius": 2
    }
});