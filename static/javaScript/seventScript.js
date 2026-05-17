const weatherForm=document.querySelector("form");
const weatherButton=document.querySelector("button");
weatherForm.addEventListener("submit",()=>{
    weatherButton.innerText="Wait,Fetching Data...";
    weatherButton.disabled=true;});