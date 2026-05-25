---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Judge"
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
    desc: "+8"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +8, Diplomacy +12, Intimidation +12, Society +14, Legal Lore +16"
abilityMods: ["+0", "-1", "+1", "+3", "+3", "+2"]
abilities_top:
  - name: "+7 to Sense Motive"
    desc: ""
  - name: "Group Impression"
    desc: "When the judge [[Makes an Impression]], they can compare their Diplomacy check result to the Will DCs of up to four targets instead of one."
  - name: "Legal Specialist"
    desc: "In a legal proceeding, the judge is a 6th-level challenge."
armorclass:
  - name: AC
    desc: "13; **Fort** +5, **Ref** +1, **Will** +12"
health:
  - name: HP
    desc: "5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
  - name: "Melee strike"
    desc: "Gavel +4 (`pf2:1`), **Damage** 1d6 bludgeoning"
  - name: "Melee strike"
    desc: "Gavel +3 (`pf2:1`) (thrown 10), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Remember, You're Under Oath"
    desc: "`pf2:2` The judge reminds a creature of the oath they swore to the court. The judge makes an [[Intimidation]] check against the target's Will DC. On a success, the target takes a –2 status penalty to Deception checks to [[Lie]] for 10 minutes (or a –4 status penalty on a critical success). Regardless of the result, the target is temporarily immune to this ability for 24 hours. <br>  <br> > [!danger] Effect: Remember, You're Under Oath"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Properly exercised, the duties of a judge include strict adherence to the law regardless of station, with minimal sentimentality. Yet for every unbiased justice, there's one who is zealously confident in their own agenda.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Judge"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
