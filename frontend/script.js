// Assuming you have an API endpoint for sending data to the backend
const backendUrl = "http://127.0.0.1:8000/generate-documentation/";

function sendData() {
    const projectName = document.getElementById("project-name").value;
    const projectDescription = document.getElementById(
      "project-description"
    ).value;
    const projectPath = document.getElementById("project-path").value;
    const additionalDetails = document.getElementById("additional-details").value;
  
    // Construct URL with query parameters
    const url = new URL(backendUrl);
    url.searchParams.append("project_directory", projectPath);
    url.searchParams.append("project_name", projectName);
    url.searchParams.append("project_description", projectDescription);
    // Additional details are not appended to the URL because they are optional for GET requests
  
    // Send GET request to the backend
    fetch(url, {
      method: "GET",
      headers: {
        "Accept": "application/json", // Adjust headers based on your backend requirements
      },
    })
      .then((response) => response.blob())
      .then((blob) => {
        const downloadUrl = window.URL.createObjectURL(blob);
        // console.log(downloadUrl);
        document.getElementById("download-button").removeAttribute("disabled");
        const downloadLink = document.getElementById("download-link");
        downloadLink.setAttribute("href", downloadUrl);
        // console.log(downloadLink)
      })
      .catch((error) => console.error("Error sending data:", error));
  }
  
