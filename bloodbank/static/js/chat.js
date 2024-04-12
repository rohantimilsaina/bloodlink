$(document).ready(function(){
    // Function to load users list
    function loadUsers() {
        // Make AJAX request to get list of users
        $.get('/get_users/', function(data){
            $('#usersList').empty();
            data.forEach(function(user) {
                $('#usersList').append(`<li class="list-group-item">${user}</li>`);
            });
        });
    }

    // Function to load chat messages between current user and selected user
    function loadChatMessages(selectedUser) {
        // Make AJAX request to get chat messages
        $.get(`/get_chat_messages/?user=${selectedUser}`, function(data){
            $('#chatMessages').empty();
            data.forEach(function(message) {
                $('#chatMessages').append(`<p><strong>${message.sender}</strong>: ${message.content}</p>`);
            });
        });
    }

    // Load users list on page load
    loadUsers();

    // Click event handler for selecting a user
    $('#usersList').on('click', 'li', function(){
        var selectedUser = $(this).text();
        loadChatMessages(selectedUser);
    });

    // Click event handler for sending a message
    $('#sendMessageBtn').click(function(){
        var message = $('#messageInput').val();
        var selectedUser = $('#usersList li.active').text(); // Assumes you mark active user in the list
        // Make AJAX request to send message
        $.post('/send_message/', {recipient: selectedUser, message: message}, function(data){
            // Clear input field after sending message
            $('#messageInput').val('');
            // Append sent message to chat window
            $('#chatMessages').append(`<p><strong>You</strong>: ${message}</p>`);
        });
    });
});
