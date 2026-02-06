const input = document.getElementById("nameInput");
const button = document.getElementById("btn");
const result = document.getElementById("result");

button.addEventListener("click", () => {
  const name = input.value;
  result.textContent = "こんにちは！" + name + "さん！";
});