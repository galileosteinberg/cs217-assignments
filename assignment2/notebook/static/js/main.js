// JavaScript for the notebook application

document.addEventListener('DOMContentLoaded', function() {
  // Get the add comment button and form
  const addCommentBtn = document.getElementById('add-comment-btn');
  const commentForm = document.getElementById('comment-form');

  // If the button exists, add click handler to toggle form visibility
  if (addCommentBtn && commentForm) {
    addCommentBtn.addEventListener('click', function() {
      if (commentForm.style.display === 'none' || commentForm.style.display === '') {
        commentForm.style.display = 'block';
        addCommentBtn.textContent = 'Cancel';
      } else {
        commentForm.style.display = 'none';
        addCommentBtn.textContent = 'Add comment';
      }
    });
  }
});