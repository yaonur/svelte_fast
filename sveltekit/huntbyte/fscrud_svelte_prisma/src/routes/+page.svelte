<script lang="ts">
	import type {PageData, article} from "../../.svelte-kit/types/src/routes/$types"
	
	export let data: PageData
	let articles: Array<article>
	
	$: ({articles} = data)
</script>
<div class="grid">
	<div>
		<h2>Articles:</h2>
		{#each articles as article }
			<article>
				<header>
					<h4>{article.title}</h4>
					<p>{article.content}</p>
					<form action="?/deleteArticle&id={article.id}" method="POST">
						<button class="outline secondary" type="submit">Delete Article</button>
					</form>
					<a href="/{article.id}" role="button" class="outline contrast" style="width: 100%">Edit Article</a>
				</header>
			</article>
		
		{/each}
	</div>
	<form action="?/createArticle" method="POST">
		<h3>New Article</h3>
		<label for="title">Title</label>
		<input type="text" id="title" name="title">
		<label for="content">Content</label>
		<textarea id="content" name="content" rows="{5}"/>
		<button type="submit">Add Article</button>
	</form>
</div>