---
type: creature
group: ["Animal", "Swarm"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Centipede Swarm"
level: "3"
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
    desc: "+9; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +7, Stealth +9"
abilityMods: ["+2", "+4", "+3", "-5", "+0", "-4"]
abilities_top:
  - name: "Centipede Swarm Venom"
    desc: "**Saving Throw** DC 20 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Off Guard]] (1 round) <br>  <br> **Stage 2** 1d8 poison damage, [[Clumsy]] 1, and off-guard (1 round)"
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +11, **Will** +5"
health:
  - name: HP
    desc: "30; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, splash damage 5; **Resistances** bludgeoning 5, piercing 5, slashing 2"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Swarming Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes @Damage[1d8[piercing]|options:area-damage] damage (DC 20 [[Reflex]] save) plus centipede swarm venom."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Swarms of centipedes are dangerous indeed, ravenous carpets of skittering hunger capable of devouring a traveler whole in a matter of minutes. Kobolds and mitflits are both known to incorporate swarms of centipedes into cunning traps.

Hunters and scavengers that live amid dung and detritus, centipedes are a relatively common and often reviled threat faced by adventurers. Scurrying about with surprising speed on the scores of legs attached to their long, segmented bodies, centipedes strike with poisoned mandibles to slow and torment their prey with a vicious toxin before they settle down to feed in slow and disgusting leisure.

```statblock
creature: "Centipede Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
