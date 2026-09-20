const runButton = document.getElementById("runButton");
const buttonText = document.getElementById("buttonText");

const resultBox = document.getElementById("resultBox");
const resultTitle = document.getElementById("resultTitle");
const resultMessage = document.getElementById("resultMessage");
const resultIcon = document.getElementById("resultIcon");

const fileList = document.getElementById("fileList");
const filesContainer = document.getElementById("files");

const sourceCount = document.getElementById("sourceCount");
const destinationCount = document.getElementById("destinationCount");


async function loadFolderStatus() {

    try {

        const response = await fetch("/folder-status");
        const data = await response.json();

        sourceCount.textContent = data.source_count;
        destinationCount.textContent = data.destination_count;

    } catch (error) {

        console.error("Could not load folder status:", error);

    }
}


async function runAutomation() {

    runButton.disabled = true;

    buttonText.textContent = "Running...";

    resultBox.classList.add("hidden");
    fileList.classList.add("hidden");

    try {

        const response = await fetch(
            "/run-automation",
            {
                method: "POST"
            }
        );

        const data = await response.json();


        resultBox.classList.remove("hidden");

        resultTitle.textContent =
            data.success
                ? "Automation Complete"
                : "Automation Failed";

        resultMessage.textContent = data.message;


        if (data.success) {

            resultIcon.textContent = "✓";

            if (data.moved_files.length > 0) {

                fileList.classList.remove("hidden");

                filesContainer.innerHTML = "";

                data.moved_files.forEach(function (filename) {

                    const li = document.createElement("li");

                    li.textContent = filename;

                    filesContainer.appendChild(li);

                });

            }

        } else {

            resultIcon.textContent = "!";

        }


        await loadFolderStatus();

    } catch (error) {

        resultBox.classList.remove("hidden");

        resultTitle.textContent = "Connection Error";

        resultMessage.textContent =
            "Could not connect to the Flask server.";

        resultIcon.textContent = "!";

    }


    runButton.disabled = false;

    buttonText.textContent = "Run Automation";
}


runButton.addEventListener(
    "click",
    runAutomation
);


loadFolderStatus();