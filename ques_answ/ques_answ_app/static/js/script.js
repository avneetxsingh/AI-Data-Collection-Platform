const dropdownMenu = document.getElementById("dropdown-menu");
const selectedTopicLabel = document.getElementById("selected-topic-label");
const chatInput = document.getElementById("chat-input");
const clearBtn = document.getElementById("clear-btn");

dropdownMenu.addEventListener("change", function() {
  selectedTopicLabel.textContent = "Selected Topic: " + dropdownMenu.value;
});

clearBtn.addEventListener("click", function() {
  chatInput.value = ""; // Clear the text in the chat input
});
