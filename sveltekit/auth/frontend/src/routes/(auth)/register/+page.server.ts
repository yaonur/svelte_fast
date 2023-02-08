import type { Actions } from "@sveltejs/kit";
import { redirect } from "@sveltejs/kit";

export const actions: Actions = {
  default: async ({ cookies, request }) => {
    const formData = await request.formData();
    const username = formData.get("username");
    const password = formData.get("password");
    const payload ={username,password}
    const response = await fetch("http://127.0.0.1:8000/user", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    }).catch((err) => {
      console.log(err);

    });
    console.log(response)
    throw redirect(303,'/login')
  },
};
