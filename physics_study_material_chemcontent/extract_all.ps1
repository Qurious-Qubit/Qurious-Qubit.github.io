Write-Host "Extracting all physics study materials..." -ForegroundColor Cyan

$sevenZip = "C:\Program Files\7-Zip\7z.exe"
if (-not (Test-Path $sevenZip)) {
    if (Get-Command 7z -ErrorAction SilentlyContinue) {
        $sevenZip = "7z"
    } else {
        Write-Error "7-Zip is not installed or not found in PATH. Please install 7-Zip from https://www.7-zip.org/"
        exit 1
    }
}

Get-ChildItem -Directory | ForEach-Object {
    $folderName = $_.Name
    $archive = Get-ChildItem -Path $_.FullName -Filter "$folderName.7z.001"
    if (-not $archive) {
        $archive = Get-ChildItem -Path $_.FullName -Filter "$folderName.7z"
    }
    if ($archive) {
        Write-Host "Extracting $folderName..." -ForegroundColor Green
        & $sevenZip x -y "-o$($_.FullName)" "$($archive.FullName)"
    }
}

Write-Host "All archives extracted successfully!" -ForegroundColor Green
