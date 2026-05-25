---
type: creature
group: ["Mindless", "Ooze"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tomb Jelly"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Mindless"
trait_02: "Ooze"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Motion Sense]] (precise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +13"
abilityMods: ["+6", "-5", "+6", "-5", "+0", "-5"]
abilities_top:
  - name: "Motion Sense"
    desc: "A tomb jelly can feel nearby motion through vibration and air movement."
  - name: "Flesh-dissolving Acid"
    desc: "A tomb jelly's acid damages only flesh."
  - name: "Tomb Curse"
    desc: "A creature hit by a tomb jelly's pseudopod takes 1d6 persistent void damage. If the creature dies while it has this persistent damage, its corpse is affected by [[Peaceful Rest]], except the tomb jelly can still dissolve its flesh."
armorclass:
  - name: AC
    desc: "12; **Fort** +15, **Ref** +4, **Will** +7"
health:
  - name: HP
    desc: "150; **Immunities** acid, visual, bleed, critical hits, precision, slashing, unconscious, void"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pseudopod +15 (`pf2:1`) (unarmed), **Damage** 1d6 acid plus 1d8+6 bludgeoning plus [[Tomb Curse]]"
spellcasting: []
abilities_bot:
  - name: "Bound in Death"
    desc: "`pf2:1` The tomb jelly splatters some of its substance on a willing undead creature within its reach. The target regains @Damage[5[void,healing]|shortLabel] HP and its melee Strikes get the benefits of tomb curse until the end of its next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Tomb jellies are animate masses of protoplasm with a sickly combination of yellow, gray, and black hues. Their acidic bodies dissolve flesh but leave other materials, including a victim's gear and bones, intact. Some ancient cultures entombed bodies in stone sarcophagi with tomb jellies to allow the ooze to break down the flesh and clean and polish the bones.

Slimes, molds, and other oozes can be found in dank dungeons and shadowed forests. While not necessarily evil, some grow to enormous sizes and have insatiable appetites.

```statblock
creature: "Tomb Jelly"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
