<div class="container">
	<header>
		<div><img src="favicon.png" alt="" /></div>
	</header>
	<nav>
		<ul>
			<li><a href="/"><span>Home</span></a></li>
			<li><a href="/b1"><span>B1</span></a></li>
		</ul>
	</nav>
</div>

<style lang="postcss">
	.container {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	ul {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		gap: var(--gap, 1rem);
		justify-content: center;
		span {
			color: white;
		}
    a{
      text-decoration: none;
    }
	}
	img {
		margin: 2rem;
		width: 2.5rem;
	}
</style>
