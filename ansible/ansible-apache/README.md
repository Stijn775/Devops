# Ansible Apache Webserver Project

## Overzicht
Dit project installeert en configureert een Apache2 webserver op Linux-systemen met behulp van Ansible. Het demonstreert basis Ansible-functionaliteiten zoals tasks, handlers en file management.

## Bestandbeschrijving

### Configuratiebestanden

| Bestand | Functie |
|---------|---------|
| `playbook.yaml` | Ansible playbook met alle configuratietaken |
| `hosts` | Inventory bestand met doelservers |
| `ansible.cfg` | Ansible configuratie instellingen |
| `index.html` | Aangepaste HTML startpagina voor Apache |
| `servers` | Extra server configuratie (afhankelijk van setup) |
| `checklocalinfo.yml` | Playbook voor lokale info controle |

## Vereisten

- **Ansible** geïnstalleerd op de host machine
- **SSH-connectiviteit** naar doelservers
- **Python** op doelservers (voor Ansible modules)
- **Sudo/Root privileges** nodig voor Apache installatie

## Configuratie

### Inventory (hosts bestand)
```ini
[webservers]
192.0.2.3 ansible_ssh_user=devasc ansible_ssh_pass=Cisco123!
```

**Opties:**
- `ansible_ssh_user` - SSH gebruiker
- `ansible_ssh_pass` - SSH wachtwoord
- Gebruik SSH-keys in plaats van wachtwoorden voor productie!

### Ansible Configuratie (ansible.cfg)
```ini
[defaults]
inventory=hosts                    # Inventory bestand
host_key_checking=False            # SSH host key accepteren
retry_files_enabled=False          # Geen retry bestanden
```

## Playbook Uitleg

Het `playbook.yaml` voert deze taken uit:

### 1. Apache2 Installatie
```yaml
- name: INSTALL APACHE2
  apt: name=apache2 update_cache=yes state=latest
```
- Installeert Apache2 pakket
- Update package cache
- Zorgt voor nieuwste versie

### 2. ModRewrite Enableren
```yaml
- name: ENABLE MOD_REWRITE
  apache2_module: name=rewrite state=present
  notify:
    - RESTART APACHE2
```
- Activeert Apache rewrite module (nodig voor URL herschrijving)
- Trigger handler voor Apache restart

### 3. Aangepaste Index Pagina
```yaml
- name: Copy file with owner and permissions
  ansible.builtin.copy:
    src: /home/devasc/labs/devnet-src/ansible/ansible-apache/index.html
    dest: /var/www/html/index.html
    owner: root
    group: root
    mode: '0644'
```
- Kopieert aangepaste index.html naar webroot
- Zet juiste eigenaar en permissies

### 4. Handlers
```yaml
handlers:
  - name: RESTART APACHE2
    service: name=apache2 state=restarted
```
- Herstart Apache2 service
- Wordt alleen uitgevoerd als notified

## Gebruik

### Playbook uitvoeren
```bash
# Tegen specifieke host
ansible-playbook playbook.yaml -i hosts

# Tegen specifieke groep
ansible-playbook playbook.yaml --limit webservers

# Verbose output (debug)
ansible-playbook playbook.yaml -v

# Dry-run (simulatie)
ansible-playbook playbook.yaml --check
```

### Connectivity testen
```bash
# Test connectiviteit met hosts
ansible all -i hosts -m ping

# Controleer specifieke host
ansible webservers -i hosts -m ping
```

### Ad-hoc commands uitvoeren
```bash
# Informatie over doelhost
ansible webservers -i hosts -m setup

# Commando op doelhost
ansible webservers -i hosts -m shell -a "systemctl status apache2"

# Bestand kopiëren
ansible webservers -i hosts -m copy -a "src=index.html dest=/var/www/html/"
```

## Modules Gebruikt

| Module | Functie |
|--------|---------|
| `apt` | Pakket management (Debian/Ubuntu) |
| `apache2_module` | Apache module management |
| `ansible.builtin.copy` | Bestanden kopiëren naar doelhost |
| `service` | Service management (start, stop, restart) |

## Troubleshooting

### SSH Connectie Fouten
```bash
# Test SSH connectie handmatig
ssh devasc@192.0.2.3

# Gebruik SSH key in plaats van wachtwoord
ansible-playbook playbook.yaml --private-key=/path/to/key
```

### Permissie Fouten
- Zorg dat gebruiker sudo rechten heeft
- Voeg `become: yes` toe voor root privileges
- Controleer `sudoers` bestand op doelhost

### Module Niet Gevonden
```bash
# Update Ansible collections
ansible-galaxy collection install ansible.posix
```

## Best Practices

1. **Inventory Management**
   - Gebruik groepen voor organisatie
   - Definieer variabelen in inventory

2. **Security**
   - Gebruik SSH keys in plaats van wachtwoorden
   - Gebruik Ansible Vault voor gevoelige data
   - Beperk permissies in ansible.cfg

3. **Idempotentie**
   - Zorg dat playbook meerdere keren veilig kan draaien
   - Controleer huidige state voor wijzigingen

4. **Error Handling**
   - Voeg error handlers toe
   - Test met `--check` mode
   - Zet versies van packages vast waar nodig

## Gerelateerde Projecten

- `ansible-csr1000v/` - Cisco CSR1000v netwerk configuratie
- `checklocalinfo.yml` - Lokale systeem info checkup

## Resources

- [Ansible Documentation](https://docs.ansible.com/)
- [Apache2 Module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_module.html)
- [Handlers](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_handlers.html)
