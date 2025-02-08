document.getElementById("predictForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    
    const playerData = {
        Overall: parseFloat(document.getElementById("Overall").value),
        Finishing: parseFloat(document.getElementById("Finishing").value),
        Wage: parseFloat(document.getElementById("Wage").value),
        Potential: parseFloat(document.getElementById("Potential").value),
        Reactions: parseFloat(document.getElementById("Reactions").value),
        Weight: parseFloat(document.getElementById("Weight").value),
        Age: parseFloat(document.getElementById("Age").value),
        BallControl: parseFloat(document.getElementById("BallControl").value),
        Dribbling: parseFloat(document.getElementById("Dribbling").value),
        Stamina: parseFloat(document.getElementById("Stamina").value),
        Vision: parseFloat(document.getElementById("Vision").value),
        PreferredFoot: parseFloat(document.getElementById("PreferredFoot").value),
        Height: parseFloat(document.getElementById("Height").value),
    };

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(playerData),
        });

        const result = await response.json();
        document.getElementById("result").innerText = `Predicted Value: €${result["Predicted Value (€)"]}`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error fetching prediction.";
    }
});
