<script>
    let hour = new Date().getHours();
    let min =  new Date().getMinutes();

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
    </div>
    <a class="write-btn" href="#/write">+글쓰기</a>
  </main>

  <footer>
    <div class="footer-box">
      <div class="footer-block">
        <div class="footer-icons">
          <div class="footer-icons__img">
            <img src="assets/home.svg" alt="" />
          </div>
          <div class="footer-icons__desc">홈</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img">
            <img src="assets/doc.svg" alt="" />
          </div>
          <div class="footer-icons__desc">동네생활</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img">
            <img src="assets/location.svg" alt="" />
          </div>
          <div class="footer-icons__desc">내 근처</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img">
            <img src="assets/chat.svg" alt="" />
          </div>
          <div class="footer-icons__desc">채팅</div>
        </div>
        <div class="footer-icons">
          <div class="footer-icons__img">
            <img src="assets/user.svg" alt="" />
          </div>
          <div class="footer-icons__desc">나의 당근</div>
        </div>
      </div>
    </div>
  </footer>
  <div class="media-info-msg">화면 사이즈를 줄여주세요</div>