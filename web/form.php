<?php
$title = "";
$content = "";

function send()
{
global $title;
global $content;
$title = $_POST['title'];
$content = $_POST['content'];
echo $title;
echo "<br/><br/>".$content;
return false;
}

$html = '
<!DOCTYPE HTML>
<html lang="en">
<meta charset="UTF-8">
<head>
<title>Form Sweet Form</title>
</head>

<body align ="center" style=
"color:black;background-color:white;">

<form
align="center" method="POST"
onsubmit = "return false;">

<table align="center">
<tr>
<td>Title</td>
<td>      
<input size="25"
type="text" name="title" id="tit"
placeholder="Place your title here">
</td>
</tr>
<tr>
<td>Content</td>
<td>     
<input size="25"
type="text" name="content" id="con"
placeholder="place your content here">
</td>
</tr> 
</table>
<input type="submit" value="Submit" 
onclick="send();"/>

</form>
<br/><br/>
<a href="index.php"
style="text-decoration:none;">
Go Home</a>
</body>
</html>
';


echo $html;

?>
