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
        xhttp.open('GET', `like-unlike/${post_id}`, true);
        xhttp.send()
}
