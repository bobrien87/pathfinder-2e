---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Badger"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +8, Stealth +7"
abilityMods: ["+4", "+1", "+3", "-4", "+3", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +10, **Ref** +6, **Will** +8"
health:
  - name: HP
    desc: "30"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +11 (`pf2:1`) (unarmed), **Damage** 1d8+4 piercing"
  - name: "Melee strike"
    desc: "Claw +11 (`pf2:1`) (agile, unarmed), **Damage** 1d6+4 slashing"
spellcasting: []
abilities_bot:
  - name: "Badger Rage"
    desc: "`pf2:1` The giant badger enters a state of pure rage that lasts for 1 minute, until there are no enemies it can perceive, or until it falls [[Unconscious]], whichever comes first. <br>  <br> While raging, the giant badger has AC 17, its jaws Strike deals 1d8+8 damage, and its claw Strike deals 1d6+6 damage. While raging, the giant badger also can't use actions that have the concentrate trait except for [[Seek]]. <br>  <br> After it has stopped raging, a giant badger can't use Badger Rage again for 1 minute. <br>  <br> > [!danger] Effect: Rage"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The violent, territorial giant badger is a relentless predator. An obligate carnivore, it can consume prey that ranges from rabbits to deer, livestock, and even the occasional adventurer. A giant badger's claws are sharp and strong enough to carve tunnels from solid rock. They typically stand 4 feet tall at the shoulder and weigh 500 pounds.

Giant badgers are fercely territorial and are known to defend their burrows with fury, even if a creature isn't necessarily threatening. These burrows tend to be larger than a giant badger typically needs, which sometimes draws the attention of other creatures seeking homes. This leads to many encounters between giant badgers and larger animals such as bears.

```statblock
creature: "Giant Badger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
