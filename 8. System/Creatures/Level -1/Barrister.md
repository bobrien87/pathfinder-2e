---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Barrister"
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
    desc: "+6"
languages: "Common"
skills:
  - name: Skills
    desc: "Deception +10, Diplomacy +12, Performance +10, Society +9, Legal Lore +13"
abilityMods: ["+0", "+1", "+1", "+3", "+2", "+4"]
abilities_top:
  - name: "Legal Specialist"
    desc: "In a court case or other legal proceeding, the barrister is a 4th-level challenge."
  - name: "Sway the Judge and Jury"
    desc: "A barrister gains a +2 circumstance bonus to Diplomacy checks to `act make-an-impression` or `act request` something of the deciding members within a courtroom. <br>  <br> If the barrister successfully DC 20 Performance check{Performs} against a DC of 20 during the 20 minutes prior to the check, they increase the circumstance bonus to +4."
armorclass:
  - name: AC
    desc: "13; **Fort** +3, **Ref** +3, **Will** +12"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +4 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Cite Precedent"
    desc: "`pf2:1` The barrister uses existing case law to undermine their opposition. If they succeed at a DC 20 Legal lore check{Legal Lore} check, they impose a -2 circumstance penalty on the next Diplomacy check an opponent attempts in a legal argument. <br>  <br> Any further attempts to Cite Precedent fail until a new topic with different precedents is being argued. <br>  <br> > [!danger] Effect: Cite Precedent"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Barristers may serve as criminal prosecutors or legal advocates, defending the rights of those accused of crimes or named as defendants in civil cases.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Barrister"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
