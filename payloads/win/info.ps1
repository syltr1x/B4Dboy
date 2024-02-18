$auser = $env:USERNAME
$usersl = Get-WmiObject Win32_UserAccount | Select-Object Name
$usersl = $usersl -split "\n"
$adminv = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")
$users = "["

foreach ($user in $usersl) {
    $user = $user -split "="
    $user = $user[1]
    $user = $user.Substring(0, $user.Length - 1)
    $users += '"' + $user + '", '
}

$users = $users.Substring(0, $users.Length - 2)
$users = $users + ']'
Write-Host "run>log -m:<id> admin=$($adminv.ToString()) user=$auser users=$users"
