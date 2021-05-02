const like_unlike = (post_id, button) => {
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = () => {
                if (button.className.search('is-dark') >= 0) {
                        button.classList.replace('is-dark','is-danger')
                }
                else {
                        button.classList.replace('is-danger','is-dark')
                }
        };
        xhttp.open('GET', `${window.location.origin}/like-unlike/${post_id}`, true);
        xhttp.send()
}

const comment = (post_id, button) => {
        body = document.getElementById('comment '+post_id).value
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = () => {
        };
        const url = `comment/${post_id}?comment=${body}`
        xhttp.open('GET', url, true);
        xhttp.send()
}

document.addEventListener('DOMContentLoaded', () => {
  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
    const $notification = $delete.parentNode;

    $delete.addEventListener('click', () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});
