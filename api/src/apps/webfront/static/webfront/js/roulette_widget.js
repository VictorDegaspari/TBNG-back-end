const getIdByUrl = async () => {
  const answered = getCookie("answered");
  if (answered) {
    console.log("Não vamos oferecer mais, já 'respondeu'");
    const divRoletas = document.getElementById("rouletteWidget");
    divRoletas.setAttribute("style", "display:none");
    const iframe = document.getElementById("iframeRoleta");

    iframe.setAttribute("style", "display:none");
    return;
  }
  const req = new XMLHttpRequest();

  req.onreadystatechange = function () {
    try {
      if (req.readyState == XMLHttpRequest.DONE && req.status == 200) {
        var data = JSON.parse(req.responseText);
        createRoulette(data);
      }
    } catch (err) {
      alert("Caught Exception: " + err.description);
    }
  };
  req.open("GET", "https://roleta-api.digitalsys.com.br/api/get-id", true);
  // req.crossOrigin = "anonymous"
  req.send();
};

const setCookie = (name, value, daysToExpire) => {
  const day = 24 * 3600 * 1000;
  const date = new Date(Date.now() + daysToExpire * day);
  document.cookie =
    name +
    "=" +
    value +
    "; expires=" +
    date.toUTCString() +
    "; path=/;" +
    "SameSite=None; Secure";
};

const getCookie = (name) => {
  const search = name + "=";
  const decodedCookie = decodeURIComponent(document.cookie);
  const allCookies = decodedCookie.split("; ");
  const foundCookie = allCookies.find((cookie) => cookie.startsWith(search));
  return foundCookie ? foundCookie.replace(search, "") : "";
};

const createRoulette = (id) => {
  const base_front_url = "https://roleta-front.digitalsys.com.br";
  // const base_front_url = "http://localhost:3000";

  const divRoleta = document.createElement("div");
  divRoleta.setAttribute("id", "rouletteWidget");
  divRoleta.setAttribute(
    "style",
    "position: fixed; height: 100%; width: 100%; top: 0; left:0;z-index:100000;"
  );

  const iframeTag = document.createElement("iframe");
  iframeTag.src = base_front_url + "/roleta/?id=" + id;
  // console.log("base_front_url + '/roleta/?id=' + id")
  // console.log(base_front_url + '/roleta/?id=' + id)
  iframeTag.setAttribute("id", "iframeRoleta");
  iframeTag.setAttribute(
    "style",
    "position: fixed; z-index:100000;height: 100%; width: 100%; top: 0; left:0; border:none"
  );
  const answered = getCookie("answered");
  if (answered) {
    console.log("Não vamos oferecer mais, já 'respondeu'");
    iframeTag.setAttribute("style", "display:none;");
    return;
  }

  const shown = getCookie("shown");
  if (shown) {
    divRoleta.appendChild(iframeTag);
    document.body.appendChild(divRoleta);
    // mostrar minimizado
    console.log("mostrar minimizado");
    setCookie("shown", true, 9999999);

    // const minuteInDay = 1 / (24 * 60);
    const divRoletas = document.getElementById("rouletteWidget");
    divRoletas.setAttribute(
      "style",
      "position: fixed;z-index:10000;top:0; height: 30px; width: 100%;display:flex;justify-content:center;"
    );
    const iframe = document.getElementById("iframeRoleta");

    iframe.setAttribute(
      "style",
      "position: absolute; height: 30px; width: 100%; top: 0; left:0;z-index:99999;border:none;"
    );
    return;
  }
  setCookie("shown", false, 9999999);
  divRoleta.appendChild(iframeTag);
  document.body.appendChild(divRoleta);
};

getIdByUrl();

window.onmessage = (e) => {
  const divRoleta = document.getElementById("rouletteWidget");
  const iframe = document.getElementById("iframeRoleta");
  if (e.data == "minimizar") {
    setTimeout(() => {
      divRoleta.setAttribute(
        "style",
        "position: fixed; height: 30px; width: 100%; top: 0; left:0;z-index:99999;"
      );
      iframe.setAttribute(
        "style",
        "position: absolute; height: 30px; width: 100%; top: 0; left:0;z-index:99999;border:none;"
      );
    }, 300);
  }
  if (e.data == "fechar") {
    divRoleta.setAttribute("style", "display: none;");
  }
  if (e.data == "abrir") {
    divRoleta.setAttribute(
      "style",
      "position: fixed; height: 100vh; width: 100%; top: 0; left:0;z-index:99999;"
    );
    iframe.setAttribute(
      "style",
      "position: absolute; height: 100vh; width: 100%; top: 0; left:0;z-index:99999;border:none;"
    );
  }
  if (e.data == "answeredCookie") {
    setCookie("answered", true, 9999999);
  }
};
