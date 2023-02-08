import type { Actions } from "@sveltejs/kit";
import { redirect } from "@sveltejs/kit";

export const actions: Actions = {
  default: async ({ cookies, request }) => {
    const formData = await request.formData();
    const username = formData.get("username");
    const password = formData.get("password");
    const payload = { username, password };
    console.log(formData);
    const response = await fetch("http://127.0.0.1:8000/user/login", {
      method: "POST",
      headers: { "Content-Type": "application/json"},

      // headers: { "Content-Type": "application/x-www-form-urlencoded" },
      // body: `grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`,
      body: JSON.stringify(payload),
    }).catch((err) => {
      // console.log(err);
      return err;
    });

    if (!response?.ok) {
      // throw new Error("Failed to get token");
      return response;
    } else {
      const token = await response.json();
      console.log("login success setting cookies");
      cookies.set("AuthorizationToken", `Bearer ${token}`, {
        httpOnly: true,
        path: "/",
        secure: true,
        sameSite: "strict",
        maxAge: 60 * 60 * 24, // 1 day
      });
      throw redirect(303, "/dashboard");
    }
  },
};
