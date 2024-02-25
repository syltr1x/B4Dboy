#Instalar SSH-Server
Add-WIndowsCapability -Online -Name OpenSSH.Server

# Iniciamos y automatizamos servicio
Start-Service sshd
Set-Service -Name sshd -StartupType Automatic