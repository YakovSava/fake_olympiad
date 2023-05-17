async function get(method, data) {
	let resp = await fetch(`api?method=${method}&data=${JSON.stringify(data)}`);
	return await resp.json();
}

async function search() {
	let input = document.getElementById('inp');
	const searched = await get('checkSertificate', {number: input.value});
	console.log(searched);

	let mainDiv = document.getElementById('sertificate');
	if (searched.response) {
		mainDiv.innerHTML = `<hr><object data="${searched.sertificate}.html" type="text/html" width="1500px" height="1500px"></object>`;
	} else {
		mainDiv.innerHTML = 'Такого сертификата не существует!';
	}
}

var inputFields = document.querySelectorAll('input');
for (let i = 0; i < inputFields.length; i++) {
		inputFields[i].addEventListener('change', function() {
			search().then()
		}
	);
}