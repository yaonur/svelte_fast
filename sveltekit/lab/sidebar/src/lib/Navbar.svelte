<script>
	const icon_font = 32;
	let rotation = '0deg';
	let closed = false;
	const slide = () => {
		rotation = closed ? '0deg' : '180deg';
		closed = !closed;
		console.log(rotation);
	};
</script>

<div class:closed>
	<nav>
		<span class="arrow" class:arr-closed={closed}>
			<a href="#"
				><iconify-icon
					icon="ic:baseline-keyboard-double-arrow-left"
					width="34"
					height="34"
					class="arrow"
					rotate={rotation}
					on:click={slide}
				/></a
			>
		</span>
		<ul>
			<li>
				<a href="/">
					<iconify-icon icon="line-md:home-md-twotone" width={icon_font} height={icon_font} />
				</a>
			</li>
			<li>
				<a href="/band">
					<iconify-icon icon="uil:band-aid" width={icon_font} height={icon_font} />
				</a>
			</li>
			<li>
				<a href="/setlist">
					<iconify-icon icon="ic:baseline-playlist-play" width={icon_font} height={icon_font} />
				</a>
			</li>
		</ul>
	</nav>
</div>

<style>
	nav {
		transition: var(--transition-slow);
    padding: 4px;
	}
  iconify-icon{
    color:var(--navbar-icon);
  }

	.closed {
		width: 5px;
    overflow: hidden;
	}
  .arrow{
    position:absolute;
		left: .5rem;
    top:50%;
    
  }

	.arr-closed {
    left:-1.5rem;
	}
</style>
