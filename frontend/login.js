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

  console.log("액서스토큰!!", data.access_token);

  if (res.status === 200) {
    alert("로그인성공");
    window.location.pathname = "/";
  } else if (res.status === 401) {
    alert("아이디 혹은 비밀번호 틀림");
  }
};

form.addEventListener("submit", handleSubmit);
