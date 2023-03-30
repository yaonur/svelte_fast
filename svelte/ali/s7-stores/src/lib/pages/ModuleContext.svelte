<script lang="ts">
  import Button, {getTotalButtons} from "../components/Button.svelte";
  let showButton = false;
  let total
</script>

<h1>Module</h1>
{getTotalButtons()}
<br>
<input type="checkbox" bind:checked={showButton} />
<br>

<Button />
<Button />
{#if showButton}
  <!-- content here -->
  <Button />
{/if}
{total}
<button on:click={()=>{total=getTotalButtons()}} >Update buttons counts</button>