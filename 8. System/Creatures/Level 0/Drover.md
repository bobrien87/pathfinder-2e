---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Drover"
level: "0"
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
    desc: "Athletics +7, Nature +5, Survival +5, Livestock Lore +6"
abilityMods: ["+3", "+2", "+2", "+0", "+1", "+0"]
abilities_top:
  - name: "Whistling"
    desc: "Drovers can whistle instead of speaking when communicating simple messages (such as \"go left,\" \"split the herd,\" and \"danger ahead\") to other drovers or when using the `act command-an-animal` action on their herding dogs."
armorclass:
  - name: AC
    desc: "15; **Fort** +6, **Ref** +6, **Will** +5"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Whip +7 (`pf2:1`) (disarm, nonlethal, reach, trip), **Damage** 1d4+3 slashing"
  - name: "Melee strike"
    desc: "Fist +7 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
  - name: "Ranged strike"
    desc: "Sling +6 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Hogtie"
    desc: "`pf2:2` **Requirements** A creature is [[Grabbed]] or [[Restrained]] by the drover's lasso <br>  <br> **Effect** The drover can pull the grabbed creature up to 20 feet. Then, if the creature is within reach, the drover hogties it, attempting to `act grapple` it again. On a success, the creature is restrained with the lasso, and the drover doesn't need to maintain the grapple. The hogtie lasts until the creature [[Escapes]] or the lasso is [[Forced Open]]. The drover can Interact to free a hogtied creature within reach."
  - name: "Lasso"
    desc: "`pf2:2` The drover uses their lasso to `act grapple` a Large or smaller creature up to 20 feet away. They can continue to Grapple to keep their hold on the target so long as the target remains within 20 feet and they continue to hold the end of the lasso. In addition to the [[Grabbed]] creature being able to [[Escape]], a successful DC 16 Athletics check to `act force-open dc=16` can remove the lasso entirely."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Drovers specialize in moving herds of livestock over large distances.

Society is built upon the backs of laborers.

```statblock
creature: "Drover"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
