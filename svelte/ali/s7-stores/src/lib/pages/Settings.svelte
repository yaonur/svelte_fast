<script lang="ts">
  import { settings } from "../stores/settings";
  import direction from "../stores/direction";
  
</script>

<h1>Settings</h1>
<button on:click={settings.toggleColorScheme}>Toggle Color Scheme</button>
<button on:click={settings.reset}>Reset</button>

<label
  ><input
    type="radio"
    bind:group={$settings.colorScheme}
    name="colorScheme"
    value="dark"
  />Dark</label
>
<label
  ><input
    type="radio"
    bind:group={$settings.colorScheme}
    name="colorScheme"
    value="light"
  />Light</label
>
<br />
{$direction}
<select name="lang" id="lang" bind:value={$settings.language}>
  <option value="en">English</option>
  <option value="ar">Arabic</option>
</select>
