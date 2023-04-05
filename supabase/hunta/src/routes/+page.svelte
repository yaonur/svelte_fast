<script lang="ts">
	import { supabaseClient } from '$lib/supabase';
	import type { PageData } from './$types';
	export let data: PageData;
	// console.log(data.session);
	if (data.session) {
		console.log(data)
	}
</script>

<main>
	<h1>SvelteKit & Supabase Auth</h1>
	<p>Let's learn how to register and login users!</p>
	{#if data.session}
		<!-- content here -->
		<p>Welcome ,{data.session}</p>
		<a href="/todos">Todos</a>
		<form action="/logout" method="POST">
			<button type="submit" class="btn btn-primary">Logout</button>
		</form>
	{:else}
		<div class="auth-buttons">
			<a href="/login" class="btn btn-primary">Login</a>
			<a href="/register" class="btn btn-secondary">Register</a>
		</div>
	{/if}
</main>
