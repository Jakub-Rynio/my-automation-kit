

# Getting folder path
Function Get-Folder($desc="Select a folder", $initialDirectory="") {
    [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") | Out-Null

    $folderDialog = New-Object System.Windows.Forms.FolderBrowserDialog
    $folderDialog.Description = $desc
    $folderDialog.RootFolder = "MyComputer"
    $folderDialog.SelectedPath = $initialDirectory

    if ($folderDialog.ShowDialog() -eq "OK") {
        return $folderDialog.SelectedPath
    }
    return $null
}

$forSorting = Get-Folder "Wybierz folder do posortowania"
$sortedIn = Get-Folder "Wybierz folder, w którym mają się znaleźć posortowane dane (najlepiej pusty!)"

cls

if ($sortedIn -and $forSorting -and ($sortedIn -ne $forSorting)) {
    # Set the extension list
    Set-Location $forSorting
    $filesForSort = Get-ChildItem
    $fileExtList = $filesForSort | Where-Object { $_.Extension -ne '' } | Select-Object -ExpandProperty Extension | Sort-Object -Unique

    # Create folders
    Set-Location $sortedIn
    foreach ($ext in $fileExtList) {
        New-Item -ItemType Directory -Name $ext | Out-Null
    }

    # Sorting
    Set-Location $forSorting
    foreach ($file in $filesForSort) {
        if ($file.Extension -ne '') {
            $src = $file.FullName
            $des = Join-Path -Path $sortedIn -ChildPath $file.Extension
            Move-Item -Path $src -Destination $des
        }
    }
} else {
    Write-Output "Musisz wybrać dwa różne foldery."
}
