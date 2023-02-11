<script lang="ts">
  import { goto } from "$app/navigation";

  const logout = () => {
    localStorage.removeItem("AuthorizationToken")
    goto("/");
  };
</script>

<nav>
  <a href="/">Home</a>
  <a href="/blog">Blog</a>
  <a href="/register">Register</a>
  <a href="/logout" on:click={logout}>Logout</a>
</nav>
