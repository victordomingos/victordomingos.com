Title: Contactos
Slug: contactos
Category: info 
Lang: pt
Save_as: info/contactos.php
Message: Para enviar um email ao autor, por favor preencha o seguinte formulário. Em alternativa, se preferir, envie email para <strong>info</strong> [ arroba ] <strong>victordomingos</strong> [ponto] <strong>com</strong>.


<div class="message-text"><?php echo $_SESSION['formMessage']; unset($_SESSION['formMessage']); ?></div><br />

<form class="rw-contact-form" action="biblioteca/form/mailer.php" method="post" enctype="multipart/form-data">
	 <div>
		<label>Nome:</label> *<br>
		<input class="form-input-field" type="text" value="" name="form[element0]" size="40"><br>

		<label>Email:</label> *<br>
		<input class="form-input-field" type="text" value="" name="form[element1]" size="40"><br>

		<label>Site ou blog:</label> <br>
		<input class="form-input-field" type="text" value="" name="form[element2]" size="40"><br>

		<label>Assunto:</label> *<br>
		<input class="form-input-field" type="text" value="" name="form[element4]" size="40"><br>

		<label>Mensagem:</label> *<br>
		<textarea class="form-input-field" name="form[element5]" rows="8" cols="38"></textarea><br>

		<div style="display: none;">
			<label>Spam Protection: Please don't fill this in:</label>
			<textarea name="comment" rows="1" cols="1"></textarea>
		</div>
		<input type="hidden" name="form_token" value="8580222605c46773fa7332">
		<input class="form-input-button" type="reset" name="resetButton" value="Limpar">
		<input class="form-input-button" type="submit" name="submitButton" value="Enviar">
	</div>
</form>

<br />
