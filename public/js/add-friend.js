const addButton = document.getElementById("add-friend"); // show form
const add = document.getElementById("add"); // submit form
const addForm = document.getElementById("add-form");
const friends = document.getElementById("friends");

// view post
const post = document.getElementById("post");
const modal = document.getElementById("modal");
const image = document.getElementById("image");

addButton.addEventListener("click", function () {
  addForm.style.display = "flex";
  addButton.style.display = "none";
  friends.style.display = "none";
});

add.addEventListener("click", function () {
  friends.style.display = "flex";
});

post.addEventListener("click", function () {
  alert(image.src);
  // modal.style.display = 'flex'
});
