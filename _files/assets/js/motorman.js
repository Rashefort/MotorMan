const USD = 145;
const EUR = 292;
const RUB = 298;


function NowDate() {
    let WEEKDAYS = ["Воскресение", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    let MONTHS = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"];

    let date = new Date();

    let headerDate = WEEKDAYS[date.getDay()] + ", " + date.getDate() + " " + MONTHS[date.getMonth()] + " " + date.getFullYear();

    document.getElementById("header-date").innerHTML = headerDate;
}

function ColorRate(cy, rate, color) {
    var element = document.getElementById(cy);

    element.innerHTML = rate;

    if (color == true) {
        element.classList.add("green");

    } else if (color == false) {
        element.classList.add("red");

    } else {
        element.classList.add("gray");
    }
}

function JSONRate(cy) {
    let MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

    let dateToday = new Date();
    let dateYesterday = new Date();
    dateYesterday.setDate(dateToday.getDate() - 1);

    let address = "http://www.nbrb.by/API/ExRates/Rates/Dynamics/" + cy + "?startDate=" + dateYesterday.getDate() + "+" + MONTHS[dateYesterday.getMonth()] + "+" + dateToday.getFullYear() + "&endDate=" + dateToday.getDate() + "+" + MONTHS[dateToday.getMonth()] + "+" + dateToday.getFullYear();

    switch(cy) {
        case USD:
            cy = "usd";
            break;

        case EUR:
            cy = "eur";
            break;

        case RUB:
            cy = "rub";
    }

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText);

            if (response[0]['Cur_OfficialRate'] > response[1]['Cur_OfficialRate']) {
                ColorRate(cy, response[1]['Cur_OfficialRate'], true);

            } else if (response[0]['Cur_OfficialRate'] < response[1]['Cur_OfficialRate']) {
                ColorRate(cy, response[1]['Cur_OfficialRate'], false);

            } else {
                ColorRate(cy, response[1]['Cur_OfficialRate'], null);
            }

        }
    }

    xhr.open('GET', address, true);
    xhr.send();
}
