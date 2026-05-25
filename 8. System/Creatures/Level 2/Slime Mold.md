---
type: creature
group: ["Fungus", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Slime Mold"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Fungus"
trait_02: "Mindless"
trait_03: "Ooze"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +7, Stealth +6"
abilityMods: ["+3", "+0", "+5", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A slime mold can sense nearby creatures through vibration and air or water movement."
  - name: "Slime Rot"
    desc: "**Saving Throw** DC 18 [[Fortitude]] save <br>  <br> **Onset** 1d4 days <br>  <br> **Stage 1** [[Enfeebled]] 1 and [[Sickened]] 1 (1 day) <br>  <br> **Stage 2** as stage 1 (1 day) <br>  <br> **Stage 3** [[Drained]] 1, [[Enfeebled]] 2, and [[Sickened]] 2 (1 day) <br>  <br> **Stage 4** as stage 3 (1 day) <br>  <br> **Stage 5** [[Drained]] 2 plus [[Unconscious]] (no Perception check to wake up) (1 day) <br>  <br> **Stage 6** dead, and the body erupts to release a new slime mold"
armorclass:
  - name: AC
    desc: "12; **Fort** +11, **Ref** +3, **Will** +4"
health:
  - name: HP
    desc: "60; **Immunities** critical hits, precision, unconscious, visual"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +8 (`pf2:1`) (unarmed), **Damage** 1d8+3 bludgeoning plus [[Slime Rot]]"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A slime mold appears as a mound of earth and detritus covered in a thick layer of fungus that exudes a faint stink of decay. The fungus actually shares a symbiotic relationship with the slime mold, serving as an external digestive system while gaining access to the nutrients it needs. The ooze remains perfectly still until living prey passes within reach, then it lashes out with disgusting pseudopods. With a touch, a slime mold can infect its prey with a foul contagion known as slime rot, a horrific disease that painfully breaks down a victim's flesh. At first, the disease manifests as painful rashes and agonized joints. In the later stages, though, the flesh of the affected creature actually begins to liquefy and run in rivulets as the creature's spores continue to work. Death, when it occurs, swiftly causes the resulting body to split open and release a brand new slime mold.

Due to their bizarre physical structures and ability to break down and feed on a wide variety of materials, oozes are able to adapt to nearly any climate, especially when assisted by magical or alchemical tinkering. As a result, explorers frequently encounter new and terrifying varieties of these amorphous creatures.

```statblock
creature: "Slime Mold"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
