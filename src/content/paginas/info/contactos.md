Title: Contactos
Slug: contactos
Category: info 
Lang: pt
Save_as: contactos.php

<?php
	// Start session.
	session_start();
	
	// Set a key, checked in mailer, prevents against spammers trying to hijack the mailer.
	$security_token = $_SESSION['security_token'] = uniqid(rand());
	
	if ( ! isset($_SESSION['formMessage'])) {
		$_SESSION['formMessage'] = 'Para enviar um email ao autor, por favor preencha o seguinte formul&aacute;rio. Em alternativa, se preferir, envie email para <strong><em>info </em></strong><em>[ arroba ] </em><strong><em>victordomingos</em></strong><em> [ponto] </em><strong><em>com</em></strong><em>.</em>';	
	}
	
	if ( ! isset($_SESSION['formFooter'])) {
		$_SESSION['formFooter'] = '';
	}
	
	if ( ! isset($_SESSION['form'])) {
		$_SESSION['form'] = array();
	}
	
	function check($field, $type = '', $value = '') {
		$string = "";
		if (isset($_SESSION['form'][$field])) {
			switch($type) {
				case 'checkbox':
					$string = 'checked="checked"';
					break;
				case 'radio':
					if($_SESSION['form'][$field] === $value) {
						$string = 'checked="checked"';
					}
					break;
				case 'select':
					if($_SESSION['form'][$field] === $value) {
						$string = 'selected="selected"';
					}
					break;
				default:
					$string = $_SESSION['form'][$field];
			}
		}
		return $string;
	}
?><!DOCTYPE html>


PPPPara enviar um email ao autor, por favor preencha o seguinte formulário. Em alternativa, se preferir, envie email para **info** [ arroba ] **victordomingos** [ponto] **com**.


<div class="message-text"><?php echo $_SESSION['formMessage']; unset($_SESSION['formMessage']); ?></div><br />

<form class="rw-contact-form" action="./mailer.php" method="post" enctype="multipart/form-data">
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
<div class="form-footer"><?php echo $_SESSION['formFooter']; unset($_SESSION['formFooter']); ?></div><br />

<?php unset($_SESSION['form']); ?>