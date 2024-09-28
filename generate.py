import subprocess
import json
import time

# Remplacez par votre adresse Bitcoin
adresse_bitcoin = "bc1qldk44m8udltddn5ahpshkh68785l2sx8ue62q7"

def miner_et_afficher_infos():
    try:
        # Mine un seul bloc à la fois
        subprocess.call(["./bitcoin-cli", "generatetoaddress", "1", adresse_bitcoin])

        # Récupérer les informations sur la blockchain et le portefeuille
        info_blockchain = subprocess.check_output(["./bitcoin-cli", "getblockchaininfo"]).decode()
        info_wallet = subprocess.check_output(["./bitcoin-cli", "getwalletinfo"]).decode()

        # Parser les réponses JSON
        data_blockchain = json.loads(info_blockchain)
        data_wallet = json.loads(info_wallet)

        # Extraire les informations pertinentes
        hauteur = data_blockchain['blocks']
        solde = data_wallet['balance']
        solde_non_confirme = data_wallet['unconfirmed_balance']
        solde_immature = data_wallet['immature_balance']

        # Afficher les informations dans la console
        print(f"Bloc trouvé ! Hauteur : {hauteur}")
        print(f"Solde total : {solde}")
        print(f"Solde non confirmé : {solde_non_confirme}")
        print(f"Solde immature : {solde_immature}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
    except json.JSONDecodeError as e:
        print(f"Erreur lors du parsing du JSON : {e}")

while True:
    # Appeler la fonction pour miner et afficher les infos
    miner_et_afficher_infos()

    # Écrire dans le fichier log
    with open('log.txt', 'a') as log_file:
        log_file.write('Le programme est en cours d\'exécution...\n')
    
    # Pause de 10 secondes avant de miner à nouveau
    time.sleep(10)
