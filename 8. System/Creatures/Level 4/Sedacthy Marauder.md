---
type: creature
group: ["Amphibious", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sedacthy Marauder"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Amphibious"
trait_02: "Humanoid"
trait_03: "Sedacthy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: "Thalassic (Sea Speech)"
skills:
  - name: Skills
    desc: "Athletics +14, Intimidation +13, Survival +9"
abilityMods: ["+6", "+3", "+4", "+0", "+1", "+3"]
abilities_top:
  - name: "Sea Speech"
    desc: "A sedacthy speaking Thalassic can be understood by any animal that has a swim Speed or the amphibious or aquatic trait. By spending a week regularly interacting with such an animal, the sedacthy can make it permanently helpful."
armorclass:
  - name: AC
    desc: "19; **Fort** +14, **Ref** +9, **Will** +9"
health:
  - name: HP
    desc: "75"
abilities_mid:
  - name: "Vengeful Throw"
    desc: "`pf2:r` **Trigger** The marauder takes damage from a creature 20 feet or further away <br>  <br> **Effect** The marauder makes a ranged spear Strike against the triggering creature. This attack doesn't take a range increment penalty if the target is within the second range increment."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +14 (`pf2:1`) (agile, unarmed), **Damage** 2d4+8 slashing"
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (unarmed), **Damage** 1d4 bleed plus 1d4+8 piercing"
  - name: "Melee strike"
    desc: "Spear +14 (`pf2:1`), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Spear +11 (`pf2:1`) (thrown 20), **Damage** 1d6+10 piercing"
spellcasting: []
abilities_bot:
  - name: "Challenging Shriek"
    desc: "`pf2:1` The marauder unleashes a terrifying battle cry. Each enemy in a @Template[emanation|distance:30] must attempt a DC 21 [[Will]] save. Regardless of the results, creatures are temporarily immune for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Immobilized]] for 1 round and [[Frightened]] 3."
  - name: "Shared Feast"
    desc: "`pf2:2` The sedacthy makes a jaws Strike. If it hits, an ally of their choice can spend a reaction to make a jaws Strike against the same target. Allies with beaks or similar attacks can use those instead of jaws."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Physically imposing sedacthies prove their status by controlling dangerous aquatic creatures like great white sharks and giant moray eels.

Sedacthies are amphibious, fish-like humanoids who lurk in Golarion's oceans and are known for leading their animal servants ashore to devour air breathers. When an entire fishing village disappears overnight, sedacthies are the first suspects. Sedacthies pride themselves as natural leaders, with ambition limited only by their strict adherence to hierarchy. A sedacthy's station is determined by the strength of the animal servants they press into service, and the mettle they prove during hunts and in battles against outsiders.

```statblock
creature: "Sedacthy Marauder"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
