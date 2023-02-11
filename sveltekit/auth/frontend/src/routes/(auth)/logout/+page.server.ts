import { error, redirect } from "@sveltejs/kit";
import type { PageServerLoad } from './$types';

export const load = (async ({cookies}) => {
  // cookies.delete("AuthorizationToken");
  console.log("logout success");
  // throw redirect(303, "/")

})
