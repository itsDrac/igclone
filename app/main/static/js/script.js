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

const comment = (post_id, button) => {
        console.log(post_id, button)
        body = document.getElementById('comment '+post_id).value
        console.log(body)
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = () => {
        };
        const url = `comment/${post_id}?comment=${body}`
        console.log(url)
        xhttp.open('GET', url, true);
        xhttp.send()
}
