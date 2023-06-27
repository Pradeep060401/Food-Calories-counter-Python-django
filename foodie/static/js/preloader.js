setTimeout(loading,800 );



function loading() {
    var loader = document.getElementById('preloader');
    loader.style.display = "none";

    window.addEventListener("load",  ()=>{

    loader.style.display = "none"
});
}