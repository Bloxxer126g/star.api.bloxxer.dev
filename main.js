document.getElementById("UpdateButton").addEventListener("click", async () => {
    console.log("Click");

    const colour = document.getElementById("ColourPicker").value;
    console.log(colour);

    try {
        const res = await fetch("https://starstore.bloxxer.dev/api/colour.json", {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ colour })
        });

        console.log("Status:", res.status);
        console.log("Response:", await res.text());
    } catch (err) {
        console.error("Fetch error:", err);
    }
});
