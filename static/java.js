function copyText() {

    let text = document.getElementById("resultText");

    text.select();

    text.setSelectionRange(0, 99999);

    navigator.clipboard.writeText(text.value);

    alert("Copied to Clipboard!");
}