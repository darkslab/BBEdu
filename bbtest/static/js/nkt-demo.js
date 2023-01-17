

// element.scrollIntoView();
// element.scrollIntoView(false);
// element.scrollIntoView({block: "end"});
// element.scrollIntoView({behavior: "smooth", block: "end", inline: "nearest"});

function scroll2two(){
    const element = document.getElementById("scroll_2");
    element.scrollIntoView({behavior: "smooth", block: "center", inline: "nearest"});
};