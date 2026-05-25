---
type: creature
group: ["Humanoid", "Tripkee"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tripkee Fiend-Keeper"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Tripkee"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]]"
languages: "Chthonian, Common, Diabolic, Tripkee"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +13, Nature +16, Religion +16, Stealth +17, Survival +16"
abilityMods: ["+2", "+3", "+2", "+1", "+4", "+1"]
abilities_top:
  - name: "Forest Passage"
    desc: "The fiend keeper ignores difficult terrain caused by plants, such as bushes, vines, and undergrowth."
  - name: "Hunter of Virtue"
    desc: "Whenever the tripkee fiend keeper critically hits an unholy creature, they reduce the value of their [[Stupefied]] condition by 1."
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +15, **Will** +18"
health:
  - name: HP
    desc: "125"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cruuk +14 (`pf2:1`) (magical, shove), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Cruuk +17 (`pf2:1`) (magical, thrown 30), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +16 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Bounce Cruuk"
    desc: "`pf2:2` The tripkee fiend keeper makes a ranged Strike with their cruuk against a target within 30 feet. Once the Strike is complete, the cruuk ricochets back into the tripkee fiend keeper's hand. If their hands are full when the cruuk returns, it falls to the ground in their space."
  - name: "Harness Wickedness"
    desc: "`pf2:1` **Requirements** The tripkee fiend keeper isn't stupefied <br>  <br> **Effect** The tripkee fiend keeper allows a portion of the fiendish power they have absorbed to flow through their body. For the next minute, the tripkee fiend keeper's Strikes deal an additional die of damage and gain the unholy trait. The tripkee fiend keeper also gains 10 temporary Hit Points, a +5-foot status bonus to Speed for the duration, and weakness 5 to holy. At the end of the duration, the tripkee fiend keeper is [[Stupefied 1]] for 1 hour."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Tripkees have a technique for dealing with unholy threats that has been passed down through the generations. A fiend keeper can absorb unholy spirits into their body before those entities can cause trouble for their kin. Though they can tap into this power when necessary, tripkee fiend keepers try to cleanse themselves of its evil influence by undertaking good deeds.

Traditionally making their homes in the treetops of tropical jungles and forests, these frog-like humanoids are often seen as resourceful and cautious, preferring to live and hunt hidden in the branches of tall trees.

```statblock
creature: "Tripkee Fiend-Keeper"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
