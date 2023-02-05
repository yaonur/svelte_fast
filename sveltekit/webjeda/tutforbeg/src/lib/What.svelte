<div class="container grid">
	<div class="what">
		<h3>What We Do?</h3>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi blanditiis dolor, dolores est
			excepturi facere fugit impedit ipsa ipsam molestiae nihil praesentium quia quibusdam quidem,
			rem sed ullam veritatis. Unde!
		</p>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipisicing elit. Error esse illum, laudantium non
			omnis quod tenetur. Aspernatur atque cupiditate et illum iste minima nam necessitatibus porro,
			repellendus sequi similique temporibus!
		</p>
	</div>
	<div class="contact">
		<h3>Contact Us</h3>
		<p><strong>Start Bootstrap</strong></p>
		<p>Some place 32124</p>
		<p>In Hills, ASAP 89867</p>
		<p>P: (+90) 323-1212</p>
		<p>E: <a href="mailto:some@mail.com">some@mail.com</a></p>
	</div>
</div>

<style>
	.grid {
		display: grid;
		grid-template-columns: repeat(12, 1fr);
		gap: 2em;
	}
	.what {
		grid-column: span 8;
	}
	.contact {
		grid-column: span 4;
	}
	h3 {
		padding-bottom: 0.5em;
		margin-bottom: 0.5em;
		font-size: 2em;
		font-width: 500;
		border-bottom: 1px solid #ddd;
	}
	h3,
	a,
	p {
		color: var(--color-primary);
	}
	a {
		text-decoration: none;
		color: var(--color-hero-background);
	}
</style>
