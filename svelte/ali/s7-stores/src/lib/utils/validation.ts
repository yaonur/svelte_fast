export const validateRequiredField = (value: any, label = "Field") => {
  console.log("validating required field")
  if (value === undefined || value === null || value === "") {
    return `${label} is required`;
  }
};
export const validateEmail = (value: any, label = "Email") => {
  // console.log(value)
  if (!value.match(/^([\w.%+-]+)@([\w-]+\.)+([\w]{2,})$/i)) {
    return `${label} is not valid`;
  }
};
