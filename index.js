
// load the scripts
storagename = 'kilianscripts.v1';
scripts = undefined;
results = document.getElementById('results');
fetch('./scripts.json').then(response => {
    if (response.status !== 200) {
    	scripts = JSON.parse(window.localStorage.getItem(storagename));
        buildthepage();
    } else {
    	response.json().then( data => {
    		scripts = data;
    		window.localStorage.setItem(storagename, JSON.stringify(scripts));
            buildthepage();
    	});
    }
}).catch(function(err) {
    scripts = JSON.parse(window.localStorage.getItem(storagename));
    buildthepage();
});

// display the scripts
function buildthepage() {
    setTimeout(() => {
        for (let i=0; i < scripts.length; i++) {
            let episode = document.createElement('div');
            episode.id = i; episode.class = 'episode';
            let link = document.createElement('a');
            link.href = scripts[i].link;
            let title = document.createElement('h1');
            title.innerText = scripts[i].title;
            link.appendChild(title);
            episode.appendChild(link);
            let date = document.createElement('h5');
            date.innerText = scripts[i].date;
            episode.appendChild(date);
            for (let j=0; j < scripts[i].script.length; j++) {
                let paragraph = document.createElement('p');
                paragraph.innerText = scripts[i].script[j].line;
                episode.appendChild(paragraph);
            }
            results.appendChild(episode);
        }
    }, 500);
}
//search operation
searchbar = document.getElementById('searchbar');
searchbox = document.getElementById('searchbox');
demo = document.getElementById('demo');
boxmoved = false;
searchbox.addEventListener('input', event => {
    searchbar.style.marginTop = "var(--searchbar-input)";
	let query = event.target.value.replace(/[^a-zA-Z0-9\s]*/gi, '').split(' ');
	document.getElementById('0').style.display = 'none';
});


// // register service workers
// if ('serviceWorker' in navigator) {
// 	navigator.serviceWorker.register('./install.js');
// } else {
// 	console.log('serice worker not supported');
// }