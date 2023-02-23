<script lang="ts">
  export let initialCount: number = 0;
  export let maxCount: number = 10;
  let count: number = initialCount;
  $: stringVar = `count is ${count}`;
  const increment = () => {
    if (count < maxCount) count += 1;
  };
</script>

<div>
<!--  <h1>{stringVar}</h1>-->
  <button on:click={increment}>
    count is {count}
  </button>
</div>

<style>
  button {
    background-color: #4caf50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-decoration: none;
    font-size: 16px;
  }
</style>
