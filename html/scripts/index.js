const noscript = document.querySelectorAll('noscript');
for (let i = 0; i < noscript.length; i++) {
	noscript[i].parentNode.removeChild(noscript[i]);
}

var inputFields = document.querySelectorAll('input');
for (let i = 0; i < inputFields.length; i++) {
		inputFields[i].addEventListener('change', function() {
			alert('Регистрация завершена, вы больше не можете быть зарегестрированы!');
		}
	);
}