<script>
	import user from '../user.ts';

	let username = '';
	let password = '';
	let currentError = null;

	const login = () => {
		fetch('http://localhost:8000/user/login', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ username: username, password: password })
		})
			.then((res) => {
				if (res.status < 299) return res.json();
				if (res.status > 299) currentError = 'Something went wrong';
			})
			.then((data) => {
				if (data) {
					user.update((val) => (val = { ...data }));
				} else {
					console.log(data);
				}
			})
			.catch((error) => console.log(error));
	};
	const signup = () => {
		fetch('http://localhost:8000/user/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ username: username, password: password })
		})
			.then((res) => {
				if (res.status < 299) return res.json();
				if (res.status > 299) currentError = 'Something went wrong';
			})
			.then((data) => {
				if (data) {
					user.update((val) => (val = { ...data }));
				} else {
					console.log(data);
				}
			})
			.catch((error) => console.log(error));
	};
</script>

<form on:submit|preventDefault={login}>
	<input type="text" bind:value={username} placeholder="username" />
	<input type="text" bind:value={password} placeholder="password" />
	<button type="submit">Login</button>
</form>
<form on:submit|preventDefault={signup}>
	<input type="text" bind:value={username} placeholder="username" />
	<input type="text" bind:value={password} placeholder="password" />
	<button type="submit">signup</button>
</form>
