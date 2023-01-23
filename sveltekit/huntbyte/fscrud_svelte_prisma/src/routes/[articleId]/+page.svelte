<script lang="ts">
	import type {PageData, article} from "../../../.svelte-kit/types/src/routes/$types";
	
	export let data: PageData
	let article: article
	
	$: ({article} = data)
</script>
<form action="?/updateArticle" method="POST">
	<h3>Editing article</h3>
	<label for="title">Title</label>
	<input type="text" id="title" name="title" value="{article.title}">
	<label for="content">Content</label>
	<textarea id="content" name="content" rows="{5}" value="{article.content}"/>
	<button type="submit">Update Article</button>
</form>