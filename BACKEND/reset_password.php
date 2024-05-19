<?php
// Verificar si se ha enviado un correo electrónico
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtener la dirección de correo electrónico del formulario
    $email = $_POST['email'];

    // Generar un token de restablecimiento de contraseña único
    $token = bin2hex(random_bytes(32));

    // Guardar el token en una base de datos o en otro lugar seguro

    // Enviar un correo electrónico al usuario con el enlace de restablecimiento de contraseña
    $reset_link = "http://example.com/reset_password.php?token=$token";
    $subject = "Reset Your Password";
    $message = "Click the following link to reset your password: $reset_link";
    $headers = "From: webmaster@example.com";

    // Enviar el correo electrónico
    mail($email, $subject, $message, $headers);

    // Mostrar un mensaje de éxito al usuario
    echo "An email has been sent to $email with instructions to reset your password.";
}
?>