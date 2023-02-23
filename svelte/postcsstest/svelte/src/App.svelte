<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import Counter from './lib/Counter.svelte'
</script>

<h1>Hey there</h1>

<style lang="postcss">
  h1 {
    color: red;
    transition: transform 10s ease;
    &:hover {
      transform:rotate(2turn);
    }
  }

</style>
