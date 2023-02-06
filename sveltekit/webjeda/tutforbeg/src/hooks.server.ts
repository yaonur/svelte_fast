import type { Handle } from "@sveltejs/kit";
import { redirect } from "@sveltejs/kit";

// @ts-ignore
export const handle = async ({ event, resolve }) => {
  // console.log(event.route);
  // console.log(event.route.id?.startsWith("/(app)"));
  const access = event.cookies.get("access") === "true";
  const theme = event.cookies.get("siteTheme");
  if (!access && event.route.id?.startsWith("/(app)")){
    throw redirect(302,"/login")
  }

  // @ts-ignore
  const response = await resolve(event, {
    transformPageChunk: ({ html }) => html.replace("data-theme=\"\"", `data-theme="${theme}"`)
  });
  return response;
};
