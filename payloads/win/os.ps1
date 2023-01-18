$tagos=(Get-UICulture).Name
if ($tagos = "es-ES") {
    $tagos="Nombre del sistema operativo:"
}
else {
    $tagos="OS Name:"
}
$systemdata=systeminfo | findstr /B /C:$tagos; $systemdata=$systemdata.Split("M")[1]; $systemdata="on b4dboy : log -m:<id> system=M"+$systemdata; echo $systemdata