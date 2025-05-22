Set-ExecutionPolicy bypass
$rel_path_to_folder = "\AppData\Roaming\" # Zaczynamy zawsze w C:\Users\[UserName] | gdzie [UserName] jest brane automatycznie
$copy_folder = "C:\Users\[UserName]\Desktop\KOPIA" # Folder DO ktorego kopiujemy
$copy_to = "Name_of_dest_folder" 


$create_folder_logs = "C:\Users\[UserName]\Desktop\logs\create_folder_logs.txt"
$copy_folder_logs = "C:\Users\[UserName]\Desktop\logs\Skopiowane_foldery.txt"
$users_without_folder_logs = "C:\Users\[UserName]\Desktop\logs\uzytkownicy_bez_tety.txt"

#Folder logow
cd C:\Users\[UserName]\Desktop
mkdir logs

cd C:\Users

$users_folders = Get-ChildItem
foreach ($user_folder in $users_folders) {

    $test_src_path = "C:\Users\" + $user_folder.Name + $rel_path_to_folder
    
    if (Test-Path $test_src_path){
    
        #Robienie folderow docelowych 
        try{
            cd $copy_folder
            mkdir $user_folder.Name
            cd $user_folder.Name
            mkdir $copy_to
            
            "++Zrobiono folder++ : " + $user_folder.Name | Out-File -Append $create_folder_logs
            
        }catch{
            Set-ExecutionPolicy Restricted
            "--Przenoszenie folderu uzytkownika--: " + $user_folder.Name + "  NIE POWIODLO SIE !! " | Out-File -Append $create_folder_logs
            throw "Wystapil blad sprawdz logi"
        }
        
        #Kopiowanie
        
        try{
            cd C:\Users
            
        
            $src_path = "C:\Users\" + $user_folder.Name + $rel_path_to_folder + "\*"
            $copy_path = $copy_folder + "\" + $user_folder.Name + "\" + $copy_to
            
            Copy-Item -Path $src_path -Destination $copy_path -Recurse
             "++skopiowano folder++ : " + $src_path + " ==> " + $copy_path | Out-File -Append $copy_folder_logs
         
                  
       }catch{
           Set-ExecutionPolicy Restricted
           "--Kopiowanie folderu uzytkownika--: " + $user_folder.Name + "  NIE POWIODLO SIE !! " | Out-File -Append $create_folder_logs
            throw "Wystapil blad sprawdz logi"
       }    
   
   }else{
            
            "Uzytkownik: " + $user_folder.Name + " NIE MA PLIKU " + $copy_to | Out-File -Append $users_without_folder_logs
         }
}
Set-ExecutionPolicy Restricted