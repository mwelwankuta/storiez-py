const addButton = document.getElementById("add-friend"); // show form
const add = document.getElementById("add"); // submit form
const addForm = document.getElementById("add-form");
const friends = document.getElementById("friends");

addButton.addEventListener("click", function () {
  addForm.style.display = "flex";
  addButton.style.display = "none";
  friends.style.display = "none";
});

add.addEventListener("click", function () {
  friends.style.display = "flex";
});