const DATA = {
    light_1 : ["kepek/fényfüzer1.jpg", "Karácsonyi fényfüzér", 4500],
    light_2 : ["kepek/fenyfüzer2.jpg", "Karácsonyi fényfüzér", 4500],
    light_3 : ["kepek/fenyfüzer3.jpg", "Karácsonyi fényfüzér", 5500],
    light_4 : ["kepek/fenyfüzer4.jpg", "Karácsonyi fényfüzér", 8500],
    light_5 : ["kepek/fenyfüzer5.jpg", "Karácsonyi fényfüzér", 6000],
    light_6 : ["kepek/fenyfüzer6.jpg", "Karácsonyi fényfüzér", 6000],
    light_7 : ["kepek/fenyfüzer7.jpg", "Karácsonyi fényfüzér", 10000],
    light_8 : ["kepek/fenyfüzer8.jpg", "Karácsonyi fényfüzér", 7000],
    light_9 : ["kepek/fenyfüzer8.jpg", "Karácsonyi fényfüzér", 6500],
    light_10: ["kepek/fenyfüzer2.jpg", "Karácsonyi fényfüzér", 3500],
    ball_1 : ["kepek/kalsszik_karacsonyfadisz.jpg", "Klasszikus piros karácsonyfadísz", 4500],
    ball_2 : ["kepek/fabábu_karacsonyfadisz.webp", "Fából készült karácsonfadíszek", 3500],
    ball_3 : ["kepek/arany_karacsonyfadisz.jpg", "Arany színű karácsonyfadísz", 5500],
    ball_4 : ["kepek/kek karacsonyfadisz.webp", "Kék színű karácsonyfadísz", 5500],
    ball_5 : ["kepek/sünis_karácsonfadisz.jpg", "Sündisznós, kedvenc állatos karácsonyfadísz", 6000],
    ball_6 : ["kepek/rébszarvasos karacsonyfadisz.jpg", "Rénszarvasos karácsonyfadísz", 6000],
    ball_7 : ["kepek/kutyas karacsonyfadisz.jpeg", "Tacskós, kuytás karácsonyfadísz", 6000],
    ball_8 : ["kepek/egyedi1karacsonyfadisz.webp", "Egyedi fényképes karácsonyfadísz", 7000], 
    ball_9 : ["kepek/fabábu_karacsonyfadisz.webp", "Fából készült karácsonfadíszek", 2350],
    ball_10 : ["kepek/kalsszik_karacsonyfadisz.jpg", "Klasszikus piros karácsonyfadísz", 3250]
    
};


function addToBasket(passData) {
    console.log(passData)
    let sessionData = getBasketData()

    if (sessionData == null){
        let newBasket = []
        newBasket.push(passData)
        sessionStorage.setItem("basket", newBasket);
    }

    else {
        if (!basketDataIsExist(passData)){
            let currentSessionData = []

            currentSessionData.push(getBasketData());
            currentSessionData.push(passData);
            sessionStorage.setItem("basket", currentSessionData);
        }
    }
}

function basketDataIsExist(item){
    let sessionData = getBasketData()
    if (sessionData.includes(item)){
        return true
    }
    return false
}

function removeBasketData(item){
    let sessionData = []
    sessionData.push(getBasketData())
    console.log(sessionData)
    if (sessionData.length <= 1){
        removeAllBasketData()
        console.log("remove all .........................................")
    }
    else{
        sessionData.pop(item)
        sessionStorage.setItem("basket", sessionData);
    }
}

function getBasketData(){
    let sessionData = sessionStorage.getItem("basket");
    return sessionData;
}

function removeAllBasketData(){
    sessionStorage.removeItem("basket");
}

function createBasketUI(){
    const main_row = document.getElementById("main_row");
    let sessionData = []
    sessionData.push(getBasketData());
    let splitedDatas = sessionData[0].split(",");

    console.log(splitedDatas)

    for(var i = 0; i <= splitedDatas.length; i++){
        const div_1 = document.createElement("div");
        const card = document.createElement("div");
        const image = document.createElement("img");
        const card_body = document.createElement("div");
        const name = document.createElement("p");
        const price = document.createElement("p");

        div_1.className += "col h-100 col-lg-3";
        card.className += "card";
        image.className += "card-img-top";
        card_body.className += "card-body";
        name.className += "card-text";
        price.className += "card-text";

        card.style.marginTop = "25px";

        console.log(DATA[splitedDatas[i]])
        image.src = DATA[splitedDatas[i]][0];
        name.innerHTML = DATA[splitedDatas[i]][1];
        price.innerHTML = DATA[splitedDatas[i]][2];


        main_row.appendChild(div_1);
        div_1.appendChild(card);
        card.appendChild(image);
        card.appendChild(card_body);
        card_body.appendChild(name);
        card_body.appendChild(price);
    }
}

function getItemInfo(item){
    console.log(DATA[item]);
}

function refreshPage() {
    location.reload();
}
