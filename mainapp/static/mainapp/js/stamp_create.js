document.addEventListener("DOMContentLoaded", () => {
    const imageInput = document.getElementById("image");
    const previewImage = document.getElementById("previewImage");
    const previewContainer = document.getElementById("previewContainer");

    imageInput.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                previewImage.src = reader.result;
                previewImage.style.display = "block";
                previewContainer.querySelector("p").style.display = "none";
            };
            reader.readAsDataURL(file);
        }
    });

    // フォーム送信時の軽いアニメーション
    const form = document.getElementById("stampForm");
    form.addEventListener("submit", () => {
        form.classList.add("sending");
        form.querySelector(".submit-btn").textContent = "送信中...";
    });
});
