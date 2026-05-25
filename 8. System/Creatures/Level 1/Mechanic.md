---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mechanic"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +7, Crafting +16, Thievery +6, Engineering Lore +16"
abilityMods: ["+4", "+1", "+1", "+3", "+0", "+0"]
abilities_top:
  - name: "Mechanical Repair"
    desc: "The mechanic is trained in Crafting, but a master in Crafting for mechanical devices, siege weapons, and vehicles. They can Repair in 1 minute instead of 10 minutes, or in 3 actions for a mechanical device, siege weapon, or vehicle."
  - name: "Mechanical Specialist"
    desc: "For encounters involving mechanical repair, the mechanic is an 8th-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +8, **Ref** +6, **Will** +3"
health:
  - name: HP
    desc: "22"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Heavy Wrench +7 (`pf2:1`) (shove), **Damage** 1d6+4 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Arbalest +8 (`pf2:1`) (backstabber, reload 1, range 110 ft.), **Damage** 1d10 piercing"
spellcasting: []
abilities_bot:
  - name: "Risky Upgrade"
    desc: "`pf2:2` The mechanic pushes a mechanical device, siege weapon, or vehicle pasts its regular limits with a temporary upgrade chosen from the list below. An item can have only one risky upgrade at a time. If an item has an upgrade at the start of the mechanic's turn, the mechanic must attempt a DC 5 flat check. (These flat checks continue even if the mechanic is dead or otherwise can't take turns.) On a failure, the item explodes, dealing damage equal to the item's level to all adjacent creatures and ending the upgrade. <br>  <br> - **Overheat Weapons** If the item would deal damage, it deals an additional 1d6 fire damage. This increases to 2d6 if the item is 8th level or higher. <br> - **Pressured Plating** The item gains a +3 status bonus to its Hardness and gains temporary Hit Points equal to double its level that last for 10 minutes. <br> - **Propelled Boost** If the item has a Speed, the item gains a +15-foot status bonus to Speed."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

No one knows how to get the most out of their equipment better than a mechanic. A mechanic can repair just about any mechanical device you put in front of them with aplomb. However, they can also push the device to achieve more than you ever could have hoped for, provided you do not mind a small explosion every now and again. Don't get distracted by their impressive work, or you might be blindsided by a fast-swinging wrench.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Mechanic"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
