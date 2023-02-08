<script lang="ts">
  import {goto} from "$app/navigation"
  
  const logout=()=>{
    goto('/')
  }
</script>
<nav>
  <a href="/">Home</a>
  <a href="/blog">Blog</a>
  <a href="/register">Register</a>
  <a href="/" on:click={logout}>Logout</a>
</nav>