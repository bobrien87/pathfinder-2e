---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ofalth"
level: "10"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +23, Stealth +19"
abilityMods: ["+7", "+3", "+6", "-2", "+2", "-2"]
abilities_top:
  - name: "Refuse Pile"
    desc: "When they're not in danger, an ofalth can spend 1 minute settling into a 10-foot pile that looks like a heap of garbage. Until the next time it takes an action, the ofalth gains a +2 circumstance bonus to AC. <br>  <br> A creature that enters the area of the garbage heap or interacts with it must attempt a save against the ofalth's stench."
  - name: "Wretched Weeps"
    desc: "**Saving Throw** DC 26 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** 2d4 persistent bleed every hour and [[Enfeebled]] 1 (1 day); <br>  <br> **Stage 3** 2d6 persistent bleed every hour and [[Enfeebled]] 2 (1 day)"
armorclass:
  - name: AC
    desc: "31; **Fort** +22, **Ref** +17, **Will** +18"
health:
  - name: HP
    desc: "170; filth wallow; **Immunities** disease, poison"
abilities_mid:
  - name: "Filth Wallow"
    desc: "An ofalth gains fast healing 2 when in an area with a high concentration of debris or excrement, such as a refuse heap or sewer."
  - name: "Stench"
    desc: "30 feet. DC 28 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d12+13 bludgeoning plus [[Wretched Weeps]]"
  - name: "Ranged strike"
    desc: "Offal +19 (`pf2:1`) (range 30 ft.), **Damage** 2d10+9 bludgeoning plus [[Wretched Weeps]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Fully grown ofalths capture victims and slowly eat them alive.

Found in castle dung heaps, city dumps, and sewers, ofalths are living amalgamations of wet detritus, sewage, and rubbish. They carry a disease called wretched weeps that causes the victim's blood to seep from its pores.

```statblock
creature: "Ofalth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
