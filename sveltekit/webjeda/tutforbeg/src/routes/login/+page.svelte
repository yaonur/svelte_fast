<script>
  export let form
  console.log(form)
</script>
<div class="container">
  <h1>Login</h1>
  {#if form?.error}
    <p class="error">{form.error}</p>
  {/if}
  <form method="POST">
    <div>
      <input type="text" name="email" placeholder="username" value="someuser">
    </div>
    <div><input type="password" name="password" placeholder="password" value="somepassword"></div>
    <button type="submit">Login</button>
  </form>
</div>

<style>
  .error{
    color:red
  }
</style>