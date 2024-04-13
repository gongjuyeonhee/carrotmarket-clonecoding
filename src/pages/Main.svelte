<script>
  import { onMount } from "svelte";
  import { getDatabase, ref, onValue } from "firebase/database";
  import Nav from "../components/Nav.svelte";

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  $: items = []; //반응형 변수

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

  const db = getDatabase();
  const itemsRef = ref(db, "items/");

  onMount(() => {
    //화면이 렌더링될 때마다 onValue가 호출이 될 수 있도록
    onValue(itemsRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse(); //reverse함수로 최신순 정렬
    });
  });
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="bar" />
      <img src="assets/wifi.svg" alt="bar" />
      <img src="assets/battery.svg" alt="bar" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div>역삼1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow.svg" alt="arrow" />
      </div>
    </div>
    <div class="menu-bar__icons">
      <img src="assets/search.svg" alt="search" />
      <img src="assets/menu.svg" alt="menu" />
      <div class="arrange">
        <img src="assets/alert.svg" alt="alert" />
        <div class="alert-notification">
          <div class="noti-font">1</div>
        </div>
      </div>
    </div>
  </div>
</header>

<main>
  <div class="items-box">
    {#each items as item}
      <div class="items-list">
        <div class="items-list__img">
          <img alt={item.title} src={item.imgUrl} />
        </div>
        <div class="items-list__info">
          <div class="items-list__info-title">{item.title}</div>
          <div class="items-list__info-meta">
            {item.place}
            {calcTime(item.insertAt)}
          </div>
          <div class="items-list__info-price">{item.price}</div>
          <div>{item.description}</div>
        </div>
      </div>
    {/each}
  </div>
  <a class="write-btn" href="#/write">+글쓰기</a>
</main>

<Nav location="home" />
<div class="media-info-msg">화면 사이즈를 줄여주세요</div>
