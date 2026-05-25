---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tiger Topiary"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: "Muan (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +12, Nature +10, Stealth +12"
abilityMods: ["+4", "+4", "+3", "-2", "+0", "+3"]
abilities_top:
  - name: "Stalker"
    desc: "When in dense foliage or tall grass, the tiger topiary gains a +1 status bonus to checks to Hide."
  - name: "Walk Through Plants"
    desc: "The tiger topiary ignores difficult terrain caused by dense vegetation."
armorclass:
  - name: AC
    desc: "21; **Fort** +15, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "80; **Immunities** bleed; **Weaknesses** fire 8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +13 (`pf2:1`), **Damage** 2d6+7 slashing"
  - name: "Melee strike"
    desc: "Jaws +13 (`pf2:1`), **Damage** 2d8+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The tiger topiary Strides or Leaps and makes a Strike at the end of that movement. If it began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Pruning"
    desc: "`pf2:1` The tiger topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Medium or smaller animal. Until the next time it acts, the topiary has an automatic result of 32 for Deception checks and DCs to appear as a mundane topiary."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Tiger topiaries are most often found within the Impossible Lands and Tian Xia, adding a dangerous appearance to an enchanting garden. Souls of very proud and volatile individuals can become tiger topiaries, turning into silent stalkers and hunters. Following intruders throughout their territory until they're at their most vulnerable, they're known to pick off unsuspecting adventuring parties one member at a time. Seamlessly blending into nature, only experienced travelers can spot a tiger topiary in time to plot a different course.

Topiaries are an extremely common sight across Golarion, especially within the gleaming and well-manicured lawns of nobility. Living topiaries develop from the death of a lone soul in an overgrown area of deep primal magic, with the soul exploding into the plants around it and causing them to grow together into the form of an animal, often influenced by the personality of the dying person. Once fully formed, the living topiary lacks their original memories; however, they're filled with the desire to protect the area they were formed in, driving off invaders and those who would do harm to the flora and fauna.

```statblock
creature: "Tiger Topiary"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
