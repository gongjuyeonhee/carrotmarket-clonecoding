const calcTime = (timestamp) => {
  const curTime = new Date();
  const diff = curTime.getTime() - timestamp;

  const hour = Math.floor(diff / (1000 * 60 * 60));
  const minute = Math.floor((diff / (1000 * 60)) % 60);
  const second = Math.floor((diff / 1000) % 60);

  if (hour > 0) return `${hour}시간 전`;
  else if (minute > 0) return `${minute}분 전`;
  else if (second >= 0) return `${second}초 전`;
  else return "방금 전";
};

const renderData = (data) => {
  const main = document.querySelector(".items-box");

  data.reverse().forEach(async (obj) => {
    const div = document.createElement("div");
    div.className = "items-list";

    const ImgDiv = document.createElement("div");
    ImgDiv.className = "items-list__img";

    const img = document.createElement("img");
    const res = await fetch(`/images/${obj.id}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    img.src = url;

    const InfoDiv = document.createElement("div");
    InfoDiv.className = "items-list__info";

    const InfoTitleDiv = document.createElement("div");
    InfoTitleDiv.className = "items-list__info-title";
    InfoTitleDiv.innerText = obj.title;

    const InfoMetaDiv = document.createElement("div");
    InfoMetaDiv.className = "items-list__info-meta";
    InfoMetaDiv.innerText = obj.place + " " + calcTime(obj.insertAt);

    const InfoPriceDiv = document.createElement("div");
    InfoPriceDiv.className = "items-list__info-price";
    InfoPriceDiv.innerText = obj.price;

    ImgDiv.appendChild(img);
    InfoDiv.appendChild(InfoTitleDiv);
    InfoDiv.appendChild(InfoMetaDiv);
    InfoDiv.appendChild(InfoPriceDiv);

    div.appendChild(ImgDiv);
    div.appendChild(InfoDiv);
    main.appendChild(div);
  });
};

const fetchList = async () => {
  const accessToken = window.localStorage.getItem("token");
  const res = await fetch("/items", {
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
  });
  if (res.status === 401) {
    alert("로그인이 필요");
    window.location.pathname = "/login.html";
    return;
  }
  const data = await res.json();
  renderData(data);
};

fetchList();
