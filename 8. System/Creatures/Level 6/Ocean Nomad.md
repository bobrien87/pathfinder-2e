---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ocean Nomad"
level: "6"
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
    desc: "+16"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Athletics +15, Nature +10, Survival +13, Sailing Lore +18"
abilityMods: ["+4", "+4", "+2", "+0", "+3", "+0"]
abilities_top:
  - name: "Master Sailor"
    desc: "Any watercraft the ocean nomad pilots gains a +10-foot circumstance bonus to its Speed and reduces the minimum distance it must move to turn by half. An ocean nomad ignores difficult terrain or uneven ground from a ship's motion."
  - name: "Practiced Swimmer"
    desc: "When the ocean nomad rolls a success on an Athletics check to `act swim`, they get a critical success instead."
  - name: "Strong Lungs"
    desc: "The ocean nomad can hold their breath for up to 10 minutes (100 rounds)."
armorclass:
  - name: AC
    desc: "24; **Fort** +14, **Ref** +17, **Will** +11"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Tidal Pressure"
    desc: "`pf2:r` **Trigger** An adjacent creature attempts an Athletics check to Swim <br>  <br> **Effect** The ocean nomad chooses to either prop the swimmer up or yanks them down into the depths. Increase or decrease the result of the Athletics check by one step. If the ocean nomad chooses to decrease the result, the creature can attempt a DC 24 [[Fortitude]] save to negate the effect."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +17 (`pf2:1`), **Damage** 1d8+10 piercing"
  - name: "Melee strike"
    desc: "Trident +17 (`pf2:1`) (thrown 20), **Damage** 1d8+10 piercing"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Stab and Twist"
    desc: "`pf2:1` **Requirements** The ocean nomad's last action was a successful melee trident Strike <br>  <br> **Effect** The ocean nomad wrenches out the barbed tines of their trident, inflicting 1d6 bleed to the target."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Ocean Nomad"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
