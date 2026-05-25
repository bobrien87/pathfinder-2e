---
type: creature
group: ["Dromaar", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dromaar Mountaineer"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dromaar"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Orc"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Common, Orcish"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +7, Survival +8"
abilityMods: ["+3", "+3", "+1", "+0", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "19; **Fort** +7, **Ref** +9, **Will** +8"
health:
  - name: HP
    desc: "28"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pick +9 (`pf2:1`) (fatal d10), **Damage** 1d6+3 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, shove, unarmed), **Damage** 1d6+3 bludgeoning"
  - name: "Melee strike"
    desc: "Bola +9 (`pf2:1`) (nonlethal, ranged trip, thrown 20), **Damage** 1d6+3 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Tangle Prey"
    desc: "`pf2:1` The dromaar draws a bola and Strikes a target within 20 feet. On a success, the dromaar immediately rolls an [[Athletics]] check against the target's Fortitude DC to [[Trip]] them."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Dromaar mountaineers are hardened half-orc scouts who often lead raiding or scouting parties on dangerous expeditions. Dromaar scouts who lead many successful expeditions can rise to positions of prominence within their holds, and those who command enough loyalty may even claim a hold of their own.

Many orcs are forged in the fires of violence and conflict, often from the moment they're born. As they live lives that are frequently cut brutally short, orcs revel in testing their strength against worthy foes, whether by challenging a higher-ranking member of their community for dominance, taming a powerful beast, or slaying a fearsome monster.

Tall and powerful, with long arms and thickly muscled legs, many orcs top 7 feet in height. Their heavy limbs and broad, almost bow-legged stances combine with a tendency to slouch forward to create an almost contradictory set of circumstances where an orc can tower over other humanoids while simultaneously staring them in the eye. These features, alongside a tendency to scar easily, can make them seem quite intimidating.

The half-orc dromaars, most commonly born of unions between orcs and humans, are often tested even more harshly than their full orc kin, but those who endure these tests can rise to positions of authority. "An orc can have what an orc can hold" is a saying that not only applies to an individual's ability to secure their own destiny and position, but is also likely the root of orcs referring to their communities as holds.

```statblock
creature: "Dromaar Mountaineer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
