<script lang="ts">
	import {createEventDispatcher} from "svelte";
	const dispatch=createEventDispatcher()
	export let user;
	const login=()=>{
		dispatch("login")
	}
</script>

<button on:click={login}>Login</button>

