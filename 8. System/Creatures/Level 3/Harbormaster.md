---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Harbormaster"
level: "3"
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
languages: "Common (up to 2 additional languages)"
skills:
  - name: Skills
    desc: "Acrobatics +9, Athletics +9, Diplomacy +5, Intimidation +5, Fishing Lore +8, Sailing Lore +10"
abilityMods: ["+4", "+2", "+2", "+2", "+1", "+0"]
abilities_top:
  - name: "Steady Balance"
    desc: "Whenever the harbormaster rolls a success on a check to `act balance`, they get a critical success instead. They're not [[Off Guard]] while Balancing on narrow surfaces and uneven ground."
  - name: "Experienced Hand"
    desc: "The harbormaster has endured their share of adverse conditions at sea. Any creature that's in adverse weather or aboard a vessel on rough water is [[Off Guard]] to the harbormaster."
armorclass:
  - name: AC
    desc: "18; **Fort** +8, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "45"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +12 (`pf2:1`) (agile, sweep), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Hatchet +10 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d6+7 slashing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+7 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A port must sustain itself on different types of flows: the seaward and coastal flows, marked by the rising and falling of the tides, and the constant flow of trade. A harbormaster is expected to know the former reflexively and encourage the latter within the jurisdictional rules of law.

Larger societies rely on those with the authority and the ability to interpret and enforce laws. Some carry out these duties fairly, but others are harsh and cruel, imposing severe punishments on anyone unable to pay for clemency.

```statblock
creature: "Harbormaster"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
