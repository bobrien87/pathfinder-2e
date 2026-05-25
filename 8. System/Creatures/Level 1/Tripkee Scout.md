---
type: creature
group: ["Humanoid", "Tripkee"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tripkee Scout"
level: "1"
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
    desc: "+8; [[Darkvision]]"
languages: "Tripkee, Common"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +4, Nature +6, Stealth +7, Survival +6"
abilityMods: ["+1", "+4", "+2", "+0", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "17; **Fort** +7, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "20"
abilities_mid:
  - name: "Forest Passage"
    desc: "The scout ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dart +9 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Hand Adze +9 (`pf2:1`) (agile, finesse, sweep), **Damage** 1d4+1 slashing"
  - name: "Melee strike"
    desc: "Hand Adze +9 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d4+1 slashing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Hurl Net"
    desc: "`pf2:1` **Requirements** The scout is wielding a net in two hands <br>  <br> **Effect** The scout makes a ranged Strike (with a +9 modifier) against a Medium or smaller creature within 20 feet. On a hit, the target is [[Off Guard]] and takes a –10-foot circumstance penalty to its Speeds. On a critical hit, the creature is [[Restrained]] instead. The DC to Escape the net is 16. A creature adjacent to the target can Interact with the net to remove it. <br>  <br> > [!danger] Effect: Hurl Net"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Tripkee scouts are the first line of defense for their hidden treetop villages. They are often scattered throughout the forests in small groups to keep an eye out for anything new or dangerous that could pose a threat.

Traditionally making their homes in the treetops of tropical jungles and forests, these frog-like humanoids are often seen as resourceful and cautious, preferring to live and hunt hidden in the branches of tall trees.

```statblock
creature: "Tripkee Scout"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
