<article class="mt-4 px-4 flex flex-col items-center">
	<h1 class="mx-auto w-full max-w-md text-xl  font-bold">Lowest Common Ancestor</h1>

	<p class="mt-4">
		One of the biggest challenges when writing a JavaScript application is keeping multiple parts of the interface in
		sync. A user interaction in one part of the interface often affects data in another. If not managed well, this data
		can end up in multiple places, but with inconsistent values.
	</p>

	<div class="">
		<img
			class="my-6 h-48  object-cover object-bottom"
			src="https://images.unsplash.com/photo-1677247191292-4e1791c4ebef?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1631&q=80"
		/>
	</div>

	<p class="mt-4 font-medium text-gray-700">
		In the past few years, the JavaScript community has learned a lot about how to deal with this problem. The solution
		involves the principle of the Lowest Common Ancestor. To explain this principle, let's look at some interface
		elements you might build while working on a real-world application.
	</p>

	<p class="mt-4 font-medium text-gray-700">
		Let's say we're building an app with a collapsible panel. If the panel isOpen, we'll show the body. Clicking the
		title triggers the toggleIsOpen action.
	</p>

	<p class="mt-4 font-medium text-gray-700">
		Currently, our application looks like this. isOpen is the only piece of state in our application that changes.
		Further, the collapsible panel is the only part of the interface that needs to know about it. Because of this, it
		makes sense for the panel itself to "own" this piece of application state. So, we'll leave isOpen right where it is
		- as a simple property on the component.
	</p>
</article>
