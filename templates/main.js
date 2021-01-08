console.log("test")


// http://localhost:5000/interactive_message?inquiry=Who%20will%20be%20the%20next%20US%20president%3F

btn = document.getElementById("send-button");
chatbox = document.getElementById("chatbox");
textMessage = document.getElementById("text-message");

const addMessageToChatbox = message => {
	chatbox.insertAdjacentHTML('beforeend', `
		<a href="#" class="list-group-item list-group-item-action active">
            <div class="d-flex w-100 justify-content-between">
               <h5 class="mb-1">The Great Trump</h5>
               <small>${(new Date()).toLocaleString()}</small>
            </div>
            <p class="mb-1">${message}</p>
         </a>`)
}

const addOurMessageToChatbox = message => {
	chatbox.insertAdjacentHTML('beforeend', `
		<a href="#" class="list-group-item list-group-item-action">
            <div class="d-flex w-100 justify-content-between">
               <h5 class="mb-1">Cute Cat</h5>
               <small class="text-muted">${(new Date()).toLocaleString()}</small>
            </div>
            <p class="mb-1">${message}</p>
         </a>`)
}


const getTrumpResponse = () => {

	message = document.getElementById("text-message").value

	fetch(`/interactive_message?inquiry=${message}`)
		.then(response => response.text()
			.then(text => {
				addOurMessageToChatbox(message)
				addMessageToChatbox(text)
			}))
}

const doOnEnter = event => {
   if (event.keyCode === 13) {
      event.preventDefault();
      btn.click();
   }
}

btn.addEventListener("click", getTrumpResponse, false)
textMessage.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    btn.click();
  }
});