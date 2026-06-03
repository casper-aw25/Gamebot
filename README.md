Game rekomendations bot

#Funktion#
En lokal Ai som rekomenderar spel efter dina önskemål

#Teknik#
*Språk* Python
*Miljö* Visual Studio

#Varför jag gjorde detta val#
Jag valde att göra en spel rekomendations ai eftersom
jag gillar att spela, men det är svårt att välja spel ibland


#problem som uppstod#
Jag hade lite problem med att visa rätt spel i början trots mina önskemål var annat
Detta löstes genom att kommunciera med github co-pilot. line 226-232, line 218, 212 och 220. Detta då jag inte vetat hur jag skulle få det att funka utan error 
eller att jag inte visste alls hur jag skulle skriva

#Hur den funkar# 
Ai:n frågar vilken genre, platform och ålder som du önskar
använadaren svarar och baserat på vad användaren önskar kommer 4 spel rekomendationer dyka upp. Efter de 4 förslagen frågar ai om man är nöjd. 
om användaren säger ja, då så frågar ain vilket spel man gillade.
Användaren skriver in vilket spel och ai:n visar den listan, därefter 
slutar programmet. Säger användaren nej så kommer 4 nya förslag. Tills användaren är nöjd. Finns det inga spel som matchar frågar Ai:n om användaren vill ändra önskemål
Om ja, så börjar allt om, Om nej, då slutar programmet att köras


