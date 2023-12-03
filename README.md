# Computer_Networking_Project2
Projekti implementon një sistem klient-server duke përdorur gjuhën e programimit Python.
Serveri lidhet me klientët duke pranuar kërkesa për lexim, shkrim, dhe ekzekutim të skedarëve.
Për të siguruar një nivel të kufizuar të aksesit, klienti i parë ka privilegje të plota, duke lejuar veprime të tilla 
si shkrim dhe ekzekutim, ndërsa klientët e tjerë kanë vetëm të drejtën e leximit. 
Sistemi gjithashtu lejon shkëmbimin e mesazheve tekstuale midis klientëve dhe serverit, 
duke përfshirë edhe mundësinë për të marrë përgjigje nga serveri për secilën mesazh të dërguar. Ky projekt ofron një 
zgjidhje të thjeshtë për shkëmbimin e të dhënave dhe kontrollin e aksesit nëpërmjet një lidhjeje të rrjetit.

Projekti përdor disa libra standard të Python dhe modulat e përfshira janë:

socket: Kjo është një librari standard e Python që ofron ndihmë për programimin e soketave. 
Përmes kësaj librarie, mund të krijoni, lidhni dhe përdorni soketa për komunikim në rrjet.

threading: Ky modul lejon krijimin dhe menaxhimin e thredave. Në këtë projekt, thredat përdoren për të përpunuar 
lidhjet nga klientët, duke lejuar që një server të mund të pranojë një numër të madh të klientëve njëkohësisht.

os: Ky modul ofron funksionalitete lidhur me sistemin operativ, duke përfshirë shpërndarjen e komandave nëpërmjet 
os.popen për të ekzekutuar komanda në server.

global: Përveç modulave të përfshira, projekti përdor edhe një variabël globale (first_client) për të ndarë aksesin 
midis klientëve. Kjo përdor mund të jetë e këqija në disa raste, por në këtë projekt, përshembull, ajo shërben për 
të ndarë aksesin midis klientëve të parë dhe klientëve të tjerë.

Anëtaret e grupit:

Arjesa Muja

Arianit Gashi

Astrit Krasniqi

Ardit Gjyrevci
