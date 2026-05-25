---
type: creature
group: ["Amphibious", "Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Brood Leech Swarm"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Animal"
trait_03: "Swarm"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +11"
abilityMods: ["+0", "+3", "+4", "-5", "+1", "-5"]
abilities_top:
  - name: "Brood Leech Swarm Venom"
    desc: "**Saving Throw** DC 21 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Clumsy]] 1, [[Sickened]] 1, and -5-foot status penalty to Speed (1 round) <br>  <br> **Stage 2** [[Clumsy]] 1, [[Sickened]] 1, and -10-foot status penalty to Speed (1 round)."
armorclass:
  - name: AC
    desc: "19; **Fort** +12, **Ref** +11, **Will** +9"
health:
  - name: HP
    desc: "50; **Immunities** precision, swarm mind; **Weaknesses** area damage 5, salt 5, splash damage 5; **Resistances** bludgeoning 2, piercing 5, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Blood Draining Bites"
    desc: "`pf2:1` Each enemy in the swarm's space takes 2d6 piercing damage (DC 21 [[Reflex]] save). A creature who fails the Reflex save also takes 1d6 persistent,bleed damage and is exposed to brood leech swarm venom."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Most smaller species of leeches do not tend to swarm, but brood leeches are prone to gathering in seething, undulant mats of squirming gluttony. When they gather in sufficient numbers to swarm, they eschew the stealth of a lone leech's feeding methods in favor of swift and merciless feeding. In these situations, their mild venom can affect much larger creatures than their usual prey.

```statblock
creature: "Brood Leech Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
