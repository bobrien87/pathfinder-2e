---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pegasus"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +10"
abilityMods: ["+3", "+4", "+2", "+0", "+2", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "55"
abilities_mid:
  - name: "Buck"
    desc: "`pf2:r` DC 19 [[Reflex]] save <br>  <br> Most monsters that serve as mounts can attempt to buck off unwanted or annoying riders, but most mounts will not use this reaction against a trusted creature unless the mounts are spooked or mistreated. <br>  <br> **Trigger** A creature [[Mounts]] or uses the [[Command an Animal]] action while riding the monster. <br>  <br> **Effect** The triggering creature must succeed at a Reflex saving throw against the listed DC or fall off the creature and land [[Prone]]. If the save is a critical failure, the triggering creature also takes 1d6 bludgeoning damage in addition to the normal damage for the fall."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +10 (`pf2:1`), **Damage** 1d8+5 bludgeoning"
  - name: "Melee strike"
    desc: "Wing +10 (`pf2:1`) (agile), **Damage** 1d6+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Assisted Mount"
    desc: "`pf2:1` **Requirements** The pegasus is Flying without a rider. <br>  <br> **Effect** The pegasus Flies. At any point during the movement, it can allow a willing adjacent creature to [[Mount]] it. That creature must use a reaction to do so."
  - name: "Gallop"
    desc: "`pf2:2` The pegasus uses 2 move actions, each of which can be either Stride or Fly. It gains a +20-foot circumstance bonus to its Speeds during a Gallop."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The pegasus is a winged horse prized for its capacity to serve as an aerial mount. Unfortunately for those who desire a saddle-trained pegasus, pegasi are wild creatures and do not readily accept even well-intentioned riders.

Pegasi actively resist being mounted or controlled by evil creatures, attempting to buck an unwanted rider at every opportunity. A typical pegasus stands 6 feet high at the shoulder, weighs 1,500 pounds, and has a wingspan of 20 feet.

Pegasi are highly intelligent beasts and have a strong sense of pride and honor. The best way to entreat a pegasus is by speaking to it with grace and offering gifts appropriate to a creature of such majesty. Prospective riders who seek the mount for a worthy cause or virtuous quest have a much easier time coaxing a pegasus into granting its favor. Regardless, a pegasus never accepts a bit or saddle, for reasons both practical (a standard horse saddle interferes with its wings) and purely out of its pride as a free and untamed creature.

In the wild, pegasi live in small herds and establish territories on remote mountains where they are relatively safe from hunters and foal thieves. They occasionally move to lower ground during foal fledging season. They mature at the same rate as horses and can even breed with other equines, though the outcome of such unions is typically a foal with the traits of its least magical parent. On rare occasions, the interbreeding of a pegasus and a unicorn may result in a winged unicorn with characteristics of both parents and an unrivaled sense of righteousness.

Some pegasi carry in them the blood of a mighty and heroic ancestor. These champions of pegasus-kind dedicate their long lives to the pursuit of justice. They possess powerful supernatural abilities to aid them in this fight, such as resistance to fire and poison, immunity to petrification, and holy hoof attacks.

```statblock
creature: "Pegasus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
