---
type: creature
group: ["Beast", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hellcat"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Diabolic (Can't speak any language, Fiendish telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +17, Intimidation +14, Stealth +17, Survival +14"
abilityMods: ["+6", "+4", "+4", "+0", "+3", "+1"]
abilities_top:
  - name: "Fiendish Telepathy 100 feet"
    desc: "This functions as telepathy, except that the hellcat can speak mentally to any creature, regardless of language. This doesn't grant the hellcat the ability to understand what the other creature is thinking, unless that creature also understands Diabolic. <br>  <br> A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Fearful Attack"
    desc: "The hellcat deals an additional 1d6 precision damage to [[Frightened]] creatures."
armorclass:
  - name: AC
    desc: "25; **Fort** +15, **Ref** +17, **Will** +12"
health:
  - name: HP
    desc: "110; **Weaknesses** holy 5; **Resistances** fire 10, physical 5 except silver"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Elusive Terror"
    desc: "A hellcat can live within the fears of others and use their dread to hide from sight. The hellcat can `act hide` in the presence of [[Frightened]] creatures. If successful, the hellcat becomes [[Hidden]] from frightened creatures as if it moved behind cover or into concealment, but must otherwise Hide normally from non-frightened creatures."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile), **Damage** 2d8+8 slashing"
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`), **Damage** 2d12+8 piercing"
spellcasting: []
abilities_bot:
  - name: "Hell Pack Mindlink"
    desc: "`pf2:1` The hellcat telepathically links its senses to all other hellcats within 100 feet for 10 minutes. It loses this contact with any hellcat that moves out of a 100-foot radius. While linked to at least one ally, the hellcat can't be flanked and gains a +2 status bonus to Will saving throws."
  - name: "Menacing Growl"
    desc: "`pf2:2` The hellcat produces a low growl to disorient and frighten foes. The hellcat can cause this vocalization to originate from somewhere else within 30 feet. Non-fiends in a @Template[type:burst|distance:15] must attempt a DC 25 [[Will]] save. The hellcat can't issue another Menacing Growl for 1d4 rounds. <br> - **Critical Success** The creature is unaffected and is temporarily immune for 24 hours. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Pounce"
    desc: "`pf2:1` The hellcat Strides and makes a Strike at the end of that movement. If the hellcat began this action [[Hidden]], it remains hidden until after the ability's Strike."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Hellcats are devious predators native to the fiery pits of Hell. While the fiendish creatures resemble undead skeletal smilodons, bones smoking with heat and dripping with boiling blood, they're actually living hellspawn whose transparent flesh reveals their burning skeleton. A typical hellcat is 9 feet long and weighs 1,000 pounds.

Left to their own devices, hellcats spend their time hunting. As fiendish creatures, they don't need mortal sustenance but devour prey for the sheer pleasure of inflicting pain. They're also far more intelligent than most assume, and they resent being treated as unintelligent animals; those who treat a hellcat thusly might find themselves made into a trophy for its pack, as a hellcat will go to great lengths to coordinate elaborate revenge upon any who fail to show them proper respect.

Though they can't speak, hellcats know Diabolic and can communicate by telepathy with any creature capable of speech. They rarely say much except to whisper threats and acknowledge the orders of their diabolic masters.

Hellcats are quick to retreat if clearly outmatched or up against foes they're unable to reach, but they never forget prey that escapes them.

```statblock
creature: "Hellcat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
