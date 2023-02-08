<script lang="ts">
  import type { PageData } from "./$types";

  export let data: PageData;
  console.log("inside template")
  console.log(data)
</script>

<h1>Blogs page</h1>

{#each data.blog as blog}
  <h1>Title:{blog.title}</h1>
{/each}