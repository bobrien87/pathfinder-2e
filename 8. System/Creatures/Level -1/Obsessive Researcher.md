---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Obsessive Researcher"
level: "-1"
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
    desc: "+3"
languages: "Common (up to 3 additional uncommon languages)"
skills:
  - name: Skills
    desc: "Stealth +5, Academia Lore +19, Library Lore +23, Narrow Lore +25"
abilityMods: ["+0", "+1", "+2", "+5", "+0", "-1"]
abilities_top:
  - name: "Monomania"
    desc: "Each obsessive researcher is preoccupied with a hyper-specialized, niche body of knowledge (their Narrow Lore) in which they are the acknowledged world authority. The catch is that when such an expert goes wrong, they go badly wrong—if an obsessive researcher gets a success on a Narrow Lore roll, they get a critical success instead. But if they roll a failure, then they get a critical failure instead."
  - name: "World-Class Authority"
    desc: "In their narrow field of interest, the obsessive researcher is a 10th-level challenge."
armorclass:
  - name: AC
    desc: "14; **Fort** +3, **Ref** +2, **Will** +7"
health:
  - name: HP
    desc: "7"
abilities_mid:
  - name: "Idée Fixe"
    desc: "Nothing gets between the obsessive researcher and their subject. If the obsessive researcher is targeted by a spell or ability with a Will save that would prompt them to give up, ignore, or divert course from the subject of their Narrow Lore (for example, using a [[Suggestion]] to get a specialist in Jistkan artificing to give up a construct part), then the obsessive researcher can use their Narrow Lore skill in place of their Will save."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +5 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Pen +4 (`pf2:1`) (agile, finesse, nonlethal), **Damage** 1d4 piercing"
spellcasting: []
abilities_bot:
  - name: "Furious Harangue"
    desc: "`pf2:2` The researcher starts hectoring an enemy within 30 feet, upbraiding them for daring to interrupt such valuable research. The target must attempt a DC 15 [[Will]] save. On a failure, they are [[Frightened]] 2 ([[Frightened]] 3 and [[Fleeing]] for 1 round on a critical failure). Regardless of the result of its save, the target is temporarily immune for 1 hour."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Academia rewards specialization, and so the universities and athenaeums of the Inner Sea are full to the brim of sunlight-deprived scholars who are the world experts in such obscure topics such as the migratory habits of bogwids or the folklore of pre-Choral Brevoy.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Obsessive Researcher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
