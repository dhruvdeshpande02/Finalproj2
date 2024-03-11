document.getElementById("deleteButton").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default action of the link
    var confirmation = confirm("Are you sure you want to delete the document?");
    if (confirmation) {
        alert("Document deleted!"); // Perform delete action here
    } else {
        alert("Operation canceled."); // Handle cancel action here
    }
});