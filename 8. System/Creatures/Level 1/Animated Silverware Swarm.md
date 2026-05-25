---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Animated Silverware Swarm"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: "Swarm"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+5; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +8"
abilityMods: ["+1", "+3", "+4", "-5", "+0", "-5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16 (12 when broken); construct armor; **Fort** +9, **Ref** +8, **Will** +3"
health:
  - name: HP
    desc: "14; **Immunities** precision; **Weaknesses** area damage 3, splash damage 3"
abilities_mid:
  - name: "Construct Armor (Hardness 3)"
    desc: "Like normal objects, an animated silverware swarm has Hardness. This Hardness reduces any damage the swarm takes by an amount equal to the Hardness. Once an animated silverware swarm is reduced to fewer than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, removing the Hardness and reducing its Armor Class to 12."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Slice and Dice"
    desc: "`pf2:1` Each enemy in the animated silverware swarm's space takes @Damage[1d6[piercing]|options:area-damage] damage or @Damage[1d6[slashing]|options:area-damage] damage (DC 17 [[Reflex]] save)"
  - name: "Stick a Fork in It"
    desc: "`pf2:1` The animated silverware swarm attempts to pin a single creature. <br>  <br> The target must attempt a DC 17 [[Reflex]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** Silverware pins portions of the target's clothing and gear. The target takes a –10-foot circumstance penalty to its Speeds as long as it remains in the swarm's space. <br> - **Failure** As success, and the target also can't Step until it leaves the swarm's space. <br>  <br> > [!danger] Effect: Stick a Fork in It <br> - **Critical Failure** The target is thoroughly pinned by the silverware, becoming [[Immobilized]] until it Escapes or uses 2 Interact actions to remove all of the silverware pinning them down."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nobles are known to pay great amounts to animate their silverware, both for ease in cleaning and to serve as novelties during dinner parties.

Many animated objects have useful functions but become dangers when uncontrolled.

```statblock
creature: "Animated Silverware Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
