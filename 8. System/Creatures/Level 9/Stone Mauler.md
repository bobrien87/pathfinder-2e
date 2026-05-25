---
type: creature
group: ["Earth", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Stone Mauler"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Tremorsense]] (imprecise) 80 feet"
languages: "Petran"
skills:
  - name: Skills
    desc: "Athletics +21, Stealth +12"
abilityMods: ["+6", "-1", "+7", "-1", "+3", "-1"]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, a stone mauler is [[Slowed]] 1 and can't use reactions."
  - name: "Earth Glide"
    desc: "The stone mauler can Burrow through any earthen matter, including rock. When it does so, the stone mauler moves at its full burrow Speed, leaving no tunnels or signs of its passing."
armorclass:
  - name: AC
    desc: "27; **Fort** +23, **Ref** +15, **Will** +19"
health:
  - name: HP
    desc: "180; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Crumble"
    desc: "`pf2:r` **Trigger** The stone mauler takes damage from a hostile source while atop rock or earth <br>  <br> **Effect** The stone mauler crumbles into the ground, Burrowing down 15 feet. This Burrowing does not trigger reactions. <br>  <br> The stone mauler can't Crumble again for 1d4 rounds."
  - name: "Spike Stones"
    desc: "5 feet. <br>  <br> Spikes of rock rise up from all stone surfaces in the emanation, creating difficult terrain. A creature moving in the terrain takes 2d6 piercing damage for each square of spikes it moves into (a Large or larger creature takes damage only once for each square it moves, even if its space covers multiple squares of spikes). Creatures with the earth trait ignore all effects within the area. <br>  <br> The stone mauler can disable or activate this aura using a single action, which has the concentrate trait."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +21 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+10 bludgeoning plus [[Push]]"
  - name: "Ranged strike"
    desc: "Rock +21 (`pf2:1`) (brutal, range 80 ft.), **Damage** 2d12+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Push 10 feet"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Push in its damage entry <br>  <br> **Effect** The monster attempts to `act shove` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty. If Push lists a distance, change the distance the creature is pushed on a success to that distance."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These towering heaps of earth can inflict tremendous damage up close and from afar.

Earth elementals make excellent bodyguards for adventuresome spelunkers and are ideal protectors of important subterranean locations such as vaults and treasuries.

```statblock
creature: "Stone Mauler"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
