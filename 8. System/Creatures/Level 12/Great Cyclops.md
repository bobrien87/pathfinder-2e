---
type: creature
group: ["Giant", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Great Cyclops"
level: "12"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Giant"
trait_02: "Humanoid"
trait_03: "Mutant"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Low-Light Vision]]"
languages: "Common, Cyclops, Jotun"
skills:
  - name: Skills
    desc: "Athletics +25, Survival +22, Any One Lore +18"
abilityMods: ["+7", "+1", "+6", "-2", "+4", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "32; **Fort** +25, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "235"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
  - name: "Flash of Brutality"
    desc: "`pf2:0` **Frequency** once per day, and recharges when the great cyclops uses Ferocity. <br>  <br> **Trigger** The great cyclops succeeds at an attack roll. <br>  <br> **Effect** The attack becomes a critical success."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatclub +25 (`pf2:1`) (backswing, reach 15 ft., shove), **Damage** 3d10+13 bludgeoning"
  - name: "Melee strike"
    desc: "Horn +25 (`pf2:1`) (reach 15 ft., unarmed), **Damage** 2d10+13 piercing"
  - name: "Melee strike"
    desc: "Fist +25 (`pf2:1`) (agile, reach 15 ft., unarmed), **Damage** 3d4+13 bludgeoning"
  - name: "Ranged strike"
    desc: "Rock +23 (`pf2:1`) (brutal, range 120 ft.), **Damage** 4d6+7 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Powerful Charge"
    desc: "`pf2:2` The great cyclops Strides twice and makes a horn Strike. If it moved at least 20 feet away from its starting position, the Strike's damage is increased to 3d10+20."
  - name: "Throw Rock"
    desc: "`pf2:1` The monster picks up a rock within reach or retrieves a stowed rock and throws it, making a ranged Strike."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Gigantic loners, the great cyclopes are their lesser kin writ large. They're stronger and more violent, but their uncontrolled vision of possible futures has driven them beyond reason. They see every moment as a potential storm of uncontrollable fury and, out of a desperate desire for peace, quiet, and an end to their hunger, lash out at any who come near. Wise creatures avoid great cyclopes at all cost. It's fortunate for humanoids that great cyclopes prefer to dwell far from settlements.

Debate has long raged over the origins of these massive, destructive giants. They are so large that it had long been assumed they were used as beasts of burden by their lesser kin, now free to hunt and kill without restraint. Other scholars believe the great cyclops is the ultimate fate of the entire cyclops species. Whatever foolish decision or wayward curse caused the end of their civilization is still playing out, occasionally causing a cyclops to withdraw from their own kind, lose all semblance of intellect, and mutate into a lumbering, feral colossus.

The cyclopes are violent giants with a tragic past. Although they possess only one eye, they could once see far more than most, possessing occult wisdom and divinatory magic that gave them the mystic ability of foresight. But their legendary oracular powers failed to prevent the fall of their society, and the vast kingdoms of the cyclops long ago collapsed into ruin. Today, cyclopes have forgotten much of what they once knew, and they skulk among the crumbling remains of their fallen cities like forgotten kings and queens of their own fallen kingdoms.

```statblock
creature: "Great Cyclops"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
