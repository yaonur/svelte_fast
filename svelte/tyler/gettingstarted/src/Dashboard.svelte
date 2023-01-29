<script lang="ts">
	import {createEventDispatcher} from "svelte";
	const dispatch=createEventDispatcher()
	
	export let name;
	export let username;
	export let loggedin = true;
	let logout=()=>{
		dispatch("logout",{
			timestamp:Date.now()
		})
	};
</script>

<h1>Welcome Back! {name}</h1>
<h2>username : {username}</h2>
<br>
<button on:click={logout}>Logout</button>