<!--
  Add "text-indigo-600 border-indigo-500" as @activeClass
-->
<script lang="ts">
  let active = null;
  const setActive = (num) => {
    active = num;
  };
</script>

<div class="mx-8 border-b border-gray-200">
  <nav class="flex -mb-px">
    <a
      href=""
      class="{active==1 ? 'active' : 'inactive'} px-1 py-4 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300"
      on:click={()=>setActive(1)}
    >
      My Account
    </a>
    <a
      href="/exercises/exercise-3"
      class="{active==2 ? 'active' : 'inactive'} px-1 py-4 ml-8 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300"
      on:click={()=>setActive(2)}
    
    >
      Company
    </a>
    <a
      href="/exercises/exercise-3"
      class="{active==3 ? 'active' : 'inactive'} px-1 py-4 ml-8 text-sm font-medium leading-5 text-gray-500 whitespace-no-wrap border-b-2 border-transparent hover:text-gray-700 hover:border-gray-300"
      on:click="{()=>setActive(3)}"
    >
      Team Members
    </a>
  </nav>
</div>
<style lang="postcss">
  .active {
    @apply text-indigo-600 border-indigo-500;
  }
  
  .inactive {
    @apply text-gray-500 hover:text-gray-700 hover:border-gray-300;
  }
</style>
