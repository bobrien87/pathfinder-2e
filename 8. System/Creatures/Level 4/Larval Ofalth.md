---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Larval Ofalth"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +9"
abilityMods: ["+5", "+1", "+3", "-2", "+1", "-2"]
abilities_top:
  - name: "Hide in Filth"
    desc: "A larval ofalth can hide in any pile of filth or trash that is its size or larger, allowing it to use Stealth for initiative. If it rolls Stealth for initiative, on the first round of combat, creatures that haven't acted yet are [[Off Guard]] to it."
  - name: "Wretched Weeps"
    desc: "**Saving Throw** DC 19 [[Fortitude]] save <br>  <br> **Stage 1** carrier with no ill effect (1 day) <br>  <br> **Stage 2** 2d4 persistent bleed every hour and [[Enfeebled]] 1 (1 day); <br>  <br> **Stage 3** 2d6 persistent bleed every hour and [[Enfeebled]] 2 (1 day)"
armorclass:
  - name: AC
    desc: "20 (22 with trash shield raised); **Fort** +11, **Ref** +9, **Will** +9"
health:
  - name: HP
    desc: "60; **Immunities** disease, poison"
abilities_mid:
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
  - name: "Stench"
    desc: "30 feet. DC 19 [[Fortitude]] save <br>  <br> A creature entering the aura or starting its turn in the area must succeed at a Fortitude save or become [[Sickened]] 1 (plus [[Slowed]] 1 as long as it's sickened on a critical failure). A creature that succeeds at its save or recovers from being sickened is temporarily immune to all stench auras for 1 minute."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`) (unarmed), **Damage** 2d8+5 slashing plus [[Wretched Weeps]]"
  - name: "Ranged strike"
    desc: "Leachate +11 (`pf2:1`), **Damage** 3d8 acid plus [[Wretched Weeps]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Ofalths reproduce asexually. When they first hatch from their leathery eggs, larval ofalths resemble a tendril of flesh supported by spindly legs, but they soon cocoon themselves in trash, to serve as both armor and camouflage.

Found in castle dung heaps, city dumps, and sewers, ofalths are living amalgamations of wet detritus, sewage, and rubbish. They carry a disease called wretched weeps that causes the victim's blood to seep from its pores.

```statblock
creature: "Larval Ofalth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
