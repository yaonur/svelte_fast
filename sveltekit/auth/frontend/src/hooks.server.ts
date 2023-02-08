import { redirect } from "@sveltejs/kit";

// @ts-ignore
export const handle = async ({ event, resolve }) => {
  // console.log(event.route);
  // console.log(event.route.id?.startsWith("/(app)"));
  const access = event.cookies.get("AuthorizationToken") ;
  if (!access && event.route.id?.startsWith("/(app)")) {
    throw redirect(302, "/login");
  }
		// const token = get_token();
		console.log('getting users');
  console.log(access)
		const auth = access.value;
		console.log(auth);
		console.log('-----------------------');
		const user =  fetch('http://127.0.0.1:8000/user', {
			method: 'GET',
			headers: { Authorization: auth }
		});

  const response = await resolve(event);
  return response;
};
