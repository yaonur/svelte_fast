<script>
    import Hero from '$lib/Hero.svelte';
    import What from '$lib/What.svelte';
    export let data;
</script>

<Hero />
<What />
<div class="container">
    <div class="grid ">
        {#each data.posts as { title, url }}
            <div>
                <img src={url} alt={title} />
                <p>{title}</p>
            </div>
        {/each}
    </div>
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2em;
        padding: 2em 0;
    }
    img {
        height: 250px;
        width: auto;
        object-fit: cover;
        object-position: center;
    }
</style>
