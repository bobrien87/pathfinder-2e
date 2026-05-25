---
type: creature
group: ["Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hound Topiary"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Plant"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 40 feet"
languages: "Muan (can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +10, Nature +9, Stealth +10"
abilityMods: ["+4", "+2", "+3", "-2", "+0", "+3"]
abilities_top:
  - name: "Pack Attack"
    desc: "The hound topiary deals an extra 1d6 untyped damage to any creature within reach of at least two of its allies."
  - name: "Walk Through Plants"
    desc: "The hound topiary ignores difficult terrain caused by dense vegetation."
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +9, **Will** +6"
health:
  - name: HP
    desc: "50; **Immunities** bleed; **Weaknesses** fire 5"
abilities_mid:
  - name: "Warning Howl"
    desc: "`pf2:r` **Trigger** The hound topiary rolls for initiative using Stealth <br>  <br> **Effect** The hound shifts to life and howls, though without breath, no sound comes from its mouth. Creatures within 30 feet must attempt a DC 17 [[Will]] save or be [[Frightened]] 1. They're then immune to all hound topiaries' Warning Howls for 1 hour."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`), **Damage** 1d8+6 piercing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`), **Damage** 1d6+6 slashing"
spellcasting: []
abilities_bot:
  - name: "Pruning"
    desc: "`pf2:1` The hound topiary twists and contorts its shape, shedding branches and leaves as needed to change into a topiary of a Medium or smaller animal. Until the next time it acts, the topiary has an automatic result of 30 for Deception checks and DCs to appear as a mundane topiary."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A majestic hound can be found guarding the entrance to several noble gardens across Avistan, often as a warning sign to raiding goblin parties or a devotional plea for protection from Cayden Cailean or Dispater, depending on the region. In the wild, hound topiaries are found in areas with heavy foliage where they can camouflage their packs. No matter where they're found, they're formed from souls that were extremely loyal and protective of their fellows during life and now seek to ensure the safety of their chosen territories.

Topiaries are an extremely common sight across Golarion, especially within the gleaming and well-manicured lawns of nobility. Living topiaries develop from the death of a lone soul in an overgrown area of deep primal magic, with the soul exploding into the plants around it and causing them to grow together into the form of an animal, often influenced by the personality of the dying person. Once fully formed, the living topiary lacks their original memories; however, they're filled with the desire to protect the area they were formed in, driving off invaders and those who would do harm to the flora and fauna.

```statblock
creature: "Hound Topiary"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
