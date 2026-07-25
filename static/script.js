async function analyze() {

    const url = document.getElementById("url").value;

    const result = document.getElementById("result");

    result.innerHTML = "<p>Analyzing...</p>";

    try {

        const response = await fetch("/analyze", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                url: url
            })

        });

        const data = await response.json();

        if (data.error) {

            result.innerHTML =
                `<p class="error">${data.error}</p>`;

            return;
        }

        result.innerHTML = `

<div class="card">
<b>HTTP Status:</b> ${data.status}
</div>

<div class="card">
<b>Response Time:</b> ${data.response_time} seconds
</div>

<div class="card">
<b>Title:</b> ${data.title}
</div>

<div class="card">
<b>Description:</b> ${data.description}
</div>

<div class="card">
<b>H1 Count:</b> ${data.h1_count}
</div>

<div class="card">
<b>Images without Alt:</b> ${data.images_without_alt}
</div>

<div class="card">
<b>Word Count:</b> ${data.word_count}
</div>

`;

    }

    catch (error) {

        result.innerHTML =
            `<p class="error">Something went wrong.</p>`;

    }

}