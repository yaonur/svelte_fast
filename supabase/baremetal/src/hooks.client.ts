import type { HandleClientError } from '@sveltejs/kit';
 
 
export const handle = (({ error, event }) => {
  // example integration with https://sentry.io/
  console.log("hook running")
 
  return {
    message: 'Whoops!',
  };
}) satisfies HandleClientError;