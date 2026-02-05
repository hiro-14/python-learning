console.log("JavaScriptが読み込まれました");

const button = document.getElementById("btn");
console.log(button);
const message = document.getElementById("message");

button.addEventListener("click", function () { 
  console.log("ボタンがクリックされました");
  message.textContent = "こんにちは! JavaScript成功! 🎉";
});
