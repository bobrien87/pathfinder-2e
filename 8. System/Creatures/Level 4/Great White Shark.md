---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Great White Shark"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Scent]] (imprecise) 100 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +14, Stealth +12, Survival +9"
abilityMods: ["+6", "+2", "+4", "-4", "+1", "-4"]
abilities_top:
  - name: "Blood Scent"
    desc: "The shark can smell blood in the water from up to 1 mile away."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +10, **Will** +9"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +14 (`pf2:1`) (unarmed), **Damage** 1d12+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Breach"
    desc: "`pf2:2` The shark Swims up to its swim Speed, then [[Leaps]] vertically out of the water up to 25 feet high, making a Strike against a creature at any point during the jump (this lets it attack a creature within 30 feet of the water's surface). After the Strike, the shark splashes back down into the water."
  - name: "Savage"
    desc: "`pf2:1` **Requirements** The shark hit with a jaws Strike on its most recent action this turn. <br>  <br> **Effect** The creature the shark hit takes 1d12 slashing damage."
  - name: "Strafing Chomp"
    desc: "`pf2:1` The shark Swims up to half its swim Speed, makes a jaws Strike, and then Swims up to half its Speed further. The Strike deals half damage."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

An apex predator among the coastal surface waters where it hunts, the great white shark is one of the largest shark species. These silent killers glide gracefully through the ocean, always in search of their next meal.

Sharks of all shapes and sizes have stalked the oceans, largely unchanged, since primordial times. They are efficient, ruthless predators with multiple rows of razor-sharp teeth capable of rending prey in an instant. Their uncanny ability to smell blood in the water means sharks might show up at any scene of aquatic carnage.

```statblock
creature: "Great White Shark"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
