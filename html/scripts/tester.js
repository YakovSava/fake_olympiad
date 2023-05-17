alert('Demo active!');

async function searchTest(failed) {
	let mainDiv = document.getElementById('sertificate');
	if (failed) {
		mainDiv.innerHTML = 'Такого сертификата не существует!';
	} else {
		mainDiv.innerHTML = `<hr><object data="sertificates/example.html" type="text/html" width="1500px" height="1500px"></object>`;
	}
}