<?php 

    try{
        require "../checkSession.php";

        //Encrypt file
        $key = file_get_contents("key.txt");
        $plaintext = $_REQUEST["board"];
        $ivlen = openssl_cipher_iv_length($cipher="AES-128-CBC");
        $iv = openssl_random_pseudo_bytes($ivlen);
        $ciphertext_raw = openssl_encrypt($plaintext, $cipher, $key, $options=OPENSSL_RAW_DATA, $iv);
        $hmac = hash_hmac('sha256', $ciphertext_raw, $key, $as_binary=true);
        $ciphertext = base64_encode( $iv.$hmac.$ciphertext_raw );

        $file = fopen("board.json", "w");
        fwrite($file, $ciphertext);
        fclose($file);
        echo "success";
    }
    catch (Exception $e){
        echo $e->getMessage();
    }
?>