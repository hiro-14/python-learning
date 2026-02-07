const btn = document.getElementById("btn");
const result = document.getElementById("result");

btn.addEventListener("click", () => {
  fetch("https://jsonplaceholder.typicode.com/users/1")
  .then(response => response.json())
  .then(data => {
    console.log(data);
    result.textContent = `
    名前: ${data.name}
    メール: ${data.email}
    `;
  })
  .catch(error => {
    console.error("エラー：", error);
  });
});
