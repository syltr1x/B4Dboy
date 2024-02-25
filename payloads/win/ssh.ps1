###### ADMIN NEEDED ######

# Deteccion de idioma
$language=(Get-UICulture).Name -split "-"
if ($language[0] -eq "es") {
    $adminGroup = "Administradores"
} elseif ($language[0] -eq "en") {
    $adminGroup = "Administrators"
} else {
    $adminGroup = Read-Host "Admin Groud for ($language): "
}

# Instalar SSH-Server
Add-WIndowsCapability -Online -Name OpenSSH.Server

# Inicia y automatiza el servicio
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic

# Crear un usuario Administrador para este servicio
New-LocalUser -Name "System" -Password (ConvertTo-SecureString -AsPlainText "SSH_Password" -Force) -Description "System Administrator User NO-DELETE"
Add-LocalGroupMember -Group $adminGroup -Member "SSH_Password"

Write-Host "SSH: User=System  |  Password=SSH_Password"