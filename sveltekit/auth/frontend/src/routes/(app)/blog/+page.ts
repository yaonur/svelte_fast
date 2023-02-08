import type { PageLoad } from './$types';

export const load = (async ({ fetch, params }) => {
  const res = await fetch(`http://localhost:8000/blog/all`);
  const blog = await res.json()
  console.log("inside page.ts")
  console.log(blog)

  return { blog };
})