import type { Actions } from "./$types";
import { fail } from "@sveltejs/kit";
import { object, string, number, date } from "yup";

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const name = formData.get("name");
    const email = formData.get("email");
    const message = formData.get("message");
    const contactFormSchema = object({
      name: string().required(),
      email: string().required().email(),
      message: string().required()
    });

    try {
      const result = await contactFormSchema.validate(
        { name, email, message },
        { abortEarly: false }
      );
      const googleForms = `https://docs.google.com/forms/d/e/1FAIpQLSdS_iKdUPNuvFTCYy7558jZHq6jHqw1hJu0apZIer8oWErYAw/formResponse?usp=pp_url&entry.2005620554=${name}&entry.1045781291=${email}&entry.839337160=${message}&submit=Submit`;
      const res = await fetch(googleForms);
      console.log(res.status)
      return {
        success: true,
        status: "Form is submitted"
      };
    } catch (err) {
      // console.log(err.inner);
      // @ts-ignore
      const errors = err.inner.reduce((acc, err) => {
        return { ...acc, [err.path]: err.message };
      }, {});
      console.log(errors);
      return {
        success: false,
        status: "cant",
        errors: errors,
        name,
        email,
        message
      };
    }
  }
};
