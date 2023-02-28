<div class="h-full overflow-y-auto bg-blue-300 p-4">
	<article class="mx-auto mt-8 mb-12 max-w-lg rounded bg-white p-8 text-gray-700 shadow-xl">
		<h1 class="text-center text-4xl font-bold leading-8 text-gray-800">Utility-First</h1>
		<p class="mt-12">
			Traditionally, whenever you need to style something on the web, you write CSS. With Tailwind, you style elements
			by applying pre-existing classes directly in your HTML.
		</p>
		<p class="mt-4">
			Once you've actually built something this way, you'll quickly notice some really important benefits:
		</p>
		<ul class="mt-4 ml-8 list-disc">
			<li>You aren't wasting energy inventing class names.</li>
			<li>Your CSS stops growing.</li>
			<li>Making changes feels safer.</li>
		</ul>
		<p class="mt-4">
			When you realize how productive you can be working exclusively in HTML with predefined utility classes, working
			any other way will feel like torture.
		</p>
		<p class="mt-4">
			The biggest maintainability concern when using a utility-first approach is managing commonly repeated utility
			combinations. This is easily solved by extracting components, either as template partials/JavaScript components,
			or using Tailwind's @apply feature to create abstractions around common utility patterns.
		</p>
		<p class="mt-4">
			Aside from that, maintaining a utility-first CSS project turns out to be a lot easier than maintaining a large CSS
			codebase, simply because HTML is so much easier to maintain than CSS. Large companies like GitHub, Heroku,
			Kickstarter, Twitch, Segment, and more are using this approach with great success.
		</p>
	</article>
</div>
