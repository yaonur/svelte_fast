<script lang="ts">
	import { redirect } from '@sveltejs/kit';

	let users: [] = null;
	let username = 'string';
	let password = 'string';
	let token = '';

	const get_token = async () => {
		const response = await fetch('http://localhost:8000/token', {
			method: 'POST',
			headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
			body: `grant_type=password&username=${username}&password=${password}`
		});
		if (!response.ok) {
			throw new Error('Failed to get token');
		}
		const data = await response.json();
		console.log(data);
		token = data.access_token;
		console.log(token);
	};

	const get_users = async () => {
		// const token = get_token();
		console.log('getting users');
		const auth = `Bearer ${token}`;
		console.log(auth);
		console.log('-----------------------');
		const response = await fetch('http://localhost:8000/user', {
			method: 'GET',
			headers: { Authorization: auth }
		});
		const data = await response.json();
		users = data;
		console.log(users[0]);
	};
	if (token) {
		get_users();
	} else {
		redirect(301, '/login');
	}
</script>

<div>
	<input type="text" bind:value={username} placeholder="username" />
	<input type="text" bind:value={password} placeholder="userpassword" />
	<p>Users are</p>
	{#if users}
		<p>{users[0].username}</p>
	{/if}
	<button on:click={get_users}>Get users</button>
	<button on:click={get_token}>Login</button>
</div>
