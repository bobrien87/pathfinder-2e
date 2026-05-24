---
statblock: true
layout: Basic Pathfinder 2e Layout
type: creature
group: ["Animal", "Swarm"]
name: "Spider Swarm"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: "Unaligned"
size: "Large"
trait_01: "Animal"
trait_02: "Swarm"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4; Darkvision, Web Sense"
languages: "None"
skills:
  - name: Skills
    desc: "Acrobatics +5, Stealth +5"
abilityMods: ["-2", "+3", "+0", "-5", "+0", "-4"]
abilities_top:
  - name: "Web Sense"
    desc: "The spider swarm has imprecise tremorsense to detect the vibrations of creatures touching its web."
armorclass:
  - name: AC
    desc: "15; **Fort** +4, **Ref** +7, **Will** +2"
health:
  - name: HP
    desc: "12; **Immunities** grabbed, precision, prone, restrained, swarm mind; **Resistances** bludgeoning 2, piercing 5, slashing 5; **Weaknesses** area damage 5, splash damage 5"
abilities_mid: []
speed: "20 feet, climb 20 feet"
attacks:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the spider swarm's space takes 1d4 piercing damage (DC 14 basic Reflex save) and is exposed to spider swarm venom."
  - name: "Spider Swarm Venom"
    desc: "**Poison** Saving Throw DC 14 Fortitude; Maximum Duration 4 rounds; Stage 1 1 poison damage and enfeebled 1 (1 round); Stage 2 1d4 poison damage and enfeebled 1 (1 round)."
spellcasting: []
abilities_bot: []
sourcebook: "Bestiary"
source-type: "Remaster"
---
### `= this.file.name`

A skittering mass of hundreds of venomous spiders.

```statblock
creature: "Spider Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
