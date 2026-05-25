---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Scorpion Swarm"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
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
    desc: "+11; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +6, Stealth +11"
abilityMods: ["+0", "+5", "+2", "-5", "+0", "-4"]
abilities_top:
  - name: "Scorpion Venom"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Enfeebled]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "21; **Fort** +10, **Ref** +13, **Will** +8"
health:
  - name: HP
    desc: "55; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 3, piercing 7, slashing 7"
abilities_mid: []
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Stings"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d8 piercing damage (DC 21 [[Reflex]] save) and is exposed to scorpion venom."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These massive, terrifying arachnids are typically 8 feet long from head to the base of the tail. Giant scorpions are the favored pack animals and war beasts of various desert-dwelling creatures, particularly kholos. They are most commonly encountered in the wild, however. There they lair in mountainside caves or burrow beneath shallow layers of sand where they lie in wait for prey to wander near.

Chitinous scourges of deserts, forests, savannas, and badlands, scorpions are deadly arachnids with powerful pincers and a painful sting. Scorpions can be found in nearly every climate, where they hunt their prey with a mixture of patient stealth and raw strength. Most scorpions live in underground burrows, either as lone hunters or part of a larger colony. These arachnids are so feared and dangerous that in many cultures, they are treated as deities or dualistic symbols of both death and protection from said death.

```statblock
creature: "Scorpion Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
