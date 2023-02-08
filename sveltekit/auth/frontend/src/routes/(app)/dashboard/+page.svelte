<script lang="ts">
  async function get_user() {
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
	}
</script>

<h2>Dashboard</h2>
