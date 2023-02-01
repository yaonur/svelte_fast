<script>
  import user from "../user.ts";
  import Login from "../lib/Login.svelte";
  
  $: isLoggedIn = $user === null ? false : true;
  const logout = () => {
    user.update(val => val = null);
  };
</script>

<h1>Welcome to login app</h1>
{#if isLoggedIn}
  <h2>Thank you {$user.firstname} for logging in</h2>
  <input type="button" value="Logout!" on:click={logout}>
{:else}
  <h2>Login plz</h2>
  <Login />
{/if}