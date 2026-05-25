---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Cave Giant"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Jotun"
skills:
  - name: Skills
    desc: "Athletics +18, Intimidation +14"
abilityMods: ["+6", "+3", "+5", "-2", "+3", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "23; **Fort** +17, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greataxe +18 (`pf2:1`) (magical, reach 10 ft., sweep), **Damage** 1d12+9 slashing"
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, reach 10 ft., unarmed), **Damage** 1d8+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Rock +16 (`pf2:1`) (brutal, range 120 ft.), **Damage** 2d6+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Forceful Fracture"
    desc: "`pf2:1` **Requirements** The cave giant is within reach of any kind of stone <br>  <br> **Effect** The cave giant pounds their fist into the nearby stone, fracturing it into chunks to hurl at other creatures. The giant then makes two ranged rock Strikes, each targeting a separate creature. Both attacks count toward their multiple attack penalty, but the penalty doesn't increase until after they've made both attacks."
  - name: "Smear"
    desc: "`pf2:2` **Requirements** The cave giant is within reach of a creature that is adjacent to a wall or other solid vertical surface <br>  <br> **Effect** The cave giant snags the creature and smashes it against the wall. The giant attempts an Athletics check against the target's Reflex DC. On a success, the cave giant Grabs the creature and smears it along the nearby wall, dealing @Damage[(2d8+8)[bludgeoning]] damage. On a critical success, the damage is doubled."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Cave giants are the vicious loners of the giant world. Even other giantkin mostly find cave giants too brutal and antisocial to form alliances with. For their part, cave giants—garbed in stinking hides festooned with the rotting skulls of their victims—seem ambivalent about their foul reputation.

Spread across the world, giants are as diverse as the isolated places they inhabit. A giant makes a big impression on the local environment, especially on smaller and weaker creatures.

```statblock
creature: "Cave Giant"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
