<script lang=ts>
	import { goto } from '$app/navigation';
	import  supabase  from '$lib/utils/supabase';

  let email = 'ya_onur@hotmail.com';
  let password="123123"
  let user_id=""
	// your script goes here
 
	async function signInWithEmail() {
    let resp = await supabase.auth.signInWithPassword({
  email: email,
  password: password
})
 goto("/")

}
</script>

<input type="text" bind:value={email}>
<input type="text" bind:value={password}>
<button on:click={signInWithEmail}>Login</button>
<br>
<h2>Current user id is:</h2>
<h2>{user_id}</h2>