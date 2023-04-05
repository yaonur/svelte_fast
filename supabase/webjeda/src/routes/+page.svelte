<script lang="ts">
	import { onMount } from 'svelte';
	import type { PageData } from './$types';
	export let data: PageData;
  console.log("client side pagedata>>>>")
  console.log(data.session)
	onMount(async () => {
		const resp= await data.supabase.auth.getSession();

		if (resp.error) {
			console.log(resp.error);
		} else {
      console.log("client side session>>>>")
			console.log(resp.data);
		}
	});
	const handleLogin = async () => {
		const resp= await data.supabase.auth.signInWithPassword({
			email: 'ya_onur@hotmail.com',
			password: '123123'
		});
		if (resp.error) {
			console.log(resp.error);
		} else {
			console.log('login success>>>>');
			console.log(resp.data);
		}
	};
  const handleShowTodos = async () => {
    const resp= await data.supabase
      .from('Todos')
      .select('*')
    if (resp.error) {
      console.log(resp.error);
    } else {
      console.log('todos>>>>');
      console.table(resp.data);
    }
  };
</script>

<div>Home</div>
<button on:click={handleLogin}>Login</button>
<button on:click={handleShowTodos}>Show todos</button>
