---
type: creature
group: ["Humanoid", "Tripkee"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tripkee Camoufleur"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Tripkee"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +5, Crafting +7, Nature +7, Stealth +11, Survival +7"
abilityMods: ["+1", "+4", "+1", "+1", "+3", "+0"]
abilities_top:
  - name: "Camouflage Specialist"
    desc: "For encounters involving avoiding detection or hiding an object or creature, the camoufleur is a 5th-level challenge."
  - name: "Forest Passage"
    desc: "The camoufleur ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
  - name: "Natural Disguise"
    desc: "The camoufleur can use their [[Disguise Kit]] to disguise a creature or object as natural flora. A creature gains a +2 item bonus to Stealth checks while in a natural environment until its next daily preparations or until its disguise is ruined, whichever comes first. An object in a natural environment can be found only by actively searching (using the [[Search]] activity while exploring or the [[Seek]] action in an encounter) and uses the camoufleur's Stealth DC. <br>  <br> > [!danger] Effect: Natural Disguise"
armorclass:
  - name: AC
    desc: "18; **Fort** +5, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dart +10 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+3 piercing"
  - name: "Melee strike"
    desc: "Hand Adze +10 (`pf2:1`) (agile, finesse, sweep), **Damage** 1d4+3 slashing"
  - name: "Melee strike"
    desc: "Hand Adze +10 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d4+3 slashing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+3 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Camoufleurs, masters of natural camouflage, not only disguise their village scouts and warriors before they embark, but also create and maintain the village-wide concealment needed to keep their community hidden and safe. Just as others rely on engineers to build walls, tripkees rely on camoufleurs to protect their homes.

Traditionally making their homes in the treetops of tropical jungles and forests, these frog-like humanoids are often seen as resourceful and cautious, preferring to live and hunt hidden in the branches of tall trees.

```statblock
creature: "Tripkee Camoufleur"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
