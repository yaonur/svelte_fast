<div class="container">
	<div class="a card" />
	<div class="b card" />
	<div class="c card" />
	<div class="d card" />
</div>

<style lang="postcss">
	:global(body) {
		margin: 0;
	}
	.container {
		display: flex;
		margin: 0;
		padding-top: 25px;
		height: 100vh;
		background: #191919;
		align-items: center;
		justify-content: center;
		div {
			position: relative;
			border: 20px solid #8f8f8f;
			width: 40px;
			height: 40px;
			margin-inline: 1px;
			border-radius: 50%;
		}
		.a {
			border-color: #553a62;
		}
    .b::after{
      position:absolute;
      content:'';
      right:-20px;
      bottom:10px;
      width:20px;
      height:70px;
      border-radius:100vw;
      background: #8f8f8f;
    }
	}
</style>
