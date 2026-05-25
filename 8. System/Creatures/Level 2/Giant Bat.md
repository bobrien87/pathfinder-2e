---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Bat"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Echolocation]] (precise) 40 feet, [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Stealth +8"
abilityMods: ["+4", "+2", "+3", "-4", "+3", "-2"]
abilities_top:
  - name: "Echolocation (Precise) 40 feet"
    desc: "A bat can use its hearing as a precise sense at the listed range."
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +8, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Wing Thrash"
    desc: "`pf2:r` **Trigger** An adjacent enemy damages the giant bat <br>  <br> **Effect** The bat makes one or two wing Strikes—one against the triggering creature and one against another adjacent creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +9 (`pf2:1`), **Damage** 1d10+4 piercing"
  - name: "Melee strike"
    desc: "Wing +9 (`pf2:1`) (agile), **Damage** 1d6+4 slashing"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

While big bats are certainly not uncommon in dark caves and abandoned ruins and may instill fear in squeamish spelunkers, the so-called giant bat is a true monster, weighing well over 100 pounds and having a wingspan of nearly 15 feet. It primarily eats fruit and bugs, but can be incited to violence through fear or hunger. Giant bat attacks can quickly give rise to rumors of more dangerous monsters—many mistake these massive animals for some sort of demon or vampiric monster. But like other bats, giant bats are simply social and intelligent mammals. They are sometimes used as mounts by smaller humanoids, commonly those who hail from or dwell in mountainous or underground regions.

A wide range of bats dwell throughout the world. Most of these nocturnal animals are harmless insectivores, but deadly breeds of vampire bats and oversized bats the size of horses pose much more significant threats to adventurers.

```statblock
creature: "Giant Bat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
