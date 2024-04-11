const form = document.querySelector("#login-form");

const handleSubmit = async (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const sha256Password = sha256(formData.get("password"));
  formData.set("password", sha256Password);

  const res = await fetch("/login", {
    method: "post",
    body: formData,
  });
  const data = await res.json();
  const accessToken = data.access_token;
  window.localStorage.setItem("token", accessToken);
  window.location.pathname = "/";
};

form.addEventListener("submit", handleSubmit);
