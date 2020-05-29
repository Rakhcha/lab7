var groupmates = [
    {
    "name": "Александр",
    "surname": "Иванов",
    "group": "БУТ1901",
    "marks": [4, 3, 5]
    },
    {
    "name": "Иван",
    "surname": "Петров",
    "group": "БАП1901",
    "marks": [4, 4, 4]
    },
    {
    "name": "Кирилл",
    "surname": "Смирнов",
    "group": "БАП1801",
    "marks": [5, 5, 5]
    },
    {
        "name": "Макс",
        "surname": "Гончаров",
        "group": "БВС5555",
        "marks": [4, 4, 5]
    }
];
   

var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
    str = str + ' ';
    return str;
};

var printStudents = function(students){
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );

    for (var i = 0; i<=students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};




let filterInGroup = function(grupa,group) {
    let result = grupa.find(item => item.group == group)
    printStudents([result])
}





let filterInMark = function(grupa,Mark) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Средняя оценка", 10)
    );

    for (i = 0; i< grupa.length; i++){
        let summa = 0
        for (f = 0; f < grupa[i].marks.length; f++){
            summa = summa + grupa[i].marks[f]
        }
        let srMark = summa / grupa[i].marks.length

        if (srMark >= Mark){
            console.log(
                rpad (grupa[i]['name'], 15),
                rpad (grupa[i]['surname'], 15),
                rpad (srMark, 10)
            )
        }
    }
}

var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++){
    foldBtns[i].addEventListener("click", function(event) {
    console.log("you clicked ",event.target);
    if(event.target.parentElement.className == "one-post"){
        event.target.parentElement.className = "one-post-folded";
        event.target.value = "Развернуть";
    }
    else if(event.target.parentElement.className == "one-post-folded"){
        event.target.parentElement.className = "one-post";
        event.target.value = "Свернуть";
    }
});
}

