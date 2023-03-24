<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";
	import { supabase } from "../../lib/supabase";
    import {loadContent  } from "$lib/stores/contentStore";
    import { content } from '$lib/stores/contentStore';

    onMount(async ()=>{
        const {data,error} = await supabase.auth.getSession()
        console.log(data!.session)
        if(!data.session){
            goto("/login")
        }
        loadContent()
    })

</script>

<h1>Admin</h1>
{#if $content}
     <!-- content here -->
     {#each $content as item}
         <!-- content here -->
         <p>{item.title}</p>
     {/each}
{/if}