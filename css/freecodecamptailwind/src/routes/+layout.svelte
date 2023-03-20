<script>
  import "../app.css";
  
  let hidden = true;
</script>

<div class="main-container h-screen bg-gray-50">
  <nav class="flex justify-center gap-x-4 bg-gray-300">
    <a href="/" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Home</a>
    <a href="/typography" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Typo</a>
    <a href="/spacesize" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Spaces & Sizes</a>
    <a href="/flex" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Flex</a>
    <a href="/grid" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Grid</a>
    <a href="/layouts" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Layouts</a>
    <a href="/design" class="bg-gray-400 p-1 text-gray-50 hover:bg-gray-200 hover:text-gray-500">Design</a>
    
    <div class="flex justify-center">
      <div>
        <div class="relative">
          <button
            class="bg-primary hover:bg-primary-600 focus:bg-primary-600
						active:bg-primary-700 flex items-center whitespace-nowrap 
						rounded px-6 pt-2.5 pb-2 text-xs font-medium uppercase 
						leading-normal text-white shadow-[0_4px_9px_-4px_#3b71ca] 
						transition duration-150 ease-in-out 
						hover:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] 
					focus:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] 
					focus:outline-none focus:ring-0 active:shadow-[0_8px_9px_-4px_rgba(59,113,202,0.3),0_4px_18px_0_rgba(59,113,202,0.2)] 
					motion-reduce:transition-none"
            on:click={() => (hidden = !hidden)}
            type="button"
            id="dropdownMenuButton1"
            aria-expanded="false"
            data-te-ripple-color="light"
          >
            Exercises
            <span class="ml-2 w-2">
							<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5">
								<path
                  fill-rule="evenodd"
                  d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
                  clip-rule="evenodd"
                />
							</svg>
						</span>
          </button>
          <ul
            class="absolute float-left m-0  min-w-max list-none overflow-hidden rounded-lg border-none bg-white bg-clip-padding text-left text-base shadow-lg dark:bg-neutral-700 [&[data-te-dropdown-show]]:block"
            class:hidden
          >
            {#each { length: 13 } as _, i}
              <li>
                <a
                  class="block w-full whitespace-nowrap bg-transparent py-2 px-4 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-neutral-600"
                  href="/exercises/exercise-{i + 1}">e-{i + 1}</a
                >
              </li>
            {/each}
          </ul>
        </div>
      </div>
    </div>
  </nav>
  
  <slot />
</div>

<style lang="postcss">
</style>
