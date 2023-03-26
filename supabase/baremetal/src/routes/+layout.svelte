<script>
	import '../app.css';
	import { onMount } from 'svelte';
  import { goto } from '$app/navigation'
  
	onMount(async () => {
		const data=localStorage.getItem("sb-ddqaubsophmlnpataogt-auth-token")
		if (data) {
			console.log(data);
		} else{
      goto('/login',)
    }
	});
</script>

<slot />
