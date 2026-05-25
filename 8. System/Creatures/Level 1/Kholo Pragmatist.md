---
type: creature
group: ["Humanoid", "Kholo"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kholo Pragmatist"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Low-Light Vision]]"
languages: "Common, Kholo"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +6, Society +4, Stealth +7, Survival +7"
abilityMods: ["+2", "+2", "+1", "+2", "+2", "+0"]
abilities_top:
  - name: "Pack Attack"
    desc: "A kholo pragmatist deals 1d4 extra damage to any creature that's within reach of at least two of the kholo pragmatist's allies."
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +6, **Will** +8"
health:
  - name: HP
    desc: "22"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Longspear +7 (`pf2:1`) (reach), **Damage** 1d8+2 piercing"
  - name: "Melee strike"
    desc: "Jaws +7 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
  - name: "Ranged strike"
    desc: "Sling +7 (`pf2:1`) (propulsive, reload 1, range 50 ft.), **Damage** 1d6+1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Pragmatic Aid"
    desc: "`pf2:1` **Requirements** The kholo pragmatist is adjacent to a foe <br>  <br> **Effect** The kholo pragmatist sets up an advantageous avenue of attack for an ally within 10 feet of the same foe and then Steps away from that foe. The foe is [[Off Guard]] to the kholo pragmatist's ally's next attack."
  - name: "Spear Parry"
    desc: "`pf2:1` **Requirements** The kholo pragmatist is wielding a longspear <br>  <br> **Effect** The kholo pragmatist positions their spear defensively, gaining a +1 circumstance bonus to AC until the start of their next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Due to their aggressive lifestyle, kholo warriors rarely live to an old age. When a kholo pragmatist enters a fight, they would prefer to see another battle, so they use any possible advantage they can get to survive. They keep foes at a distance with their longspears have developed techniques to better block attacks with the weapon. If the tide of battle turns against them, kholo pragmatists will run or surrender if it's the most practical option.

These pragmatic hunters have earned a very poor reputation for their brutality in battle and worship of demons. While many kholos live up to the terrible stories of their ferocity and cannibalism, others are scavengers and trappers just trying to get by. Many of their cultural traditions are misunderstood by other ancestries, and some kholos play into the fear provoked in those who believe the twisted tales about their people. Kholos are often criticized for their lack of honor in battle, but a kholo understands honor doesn't bring you back home alive, nor does honor put food on the table. Ambushes, feints, and deceptions that lead to fewer kholo deaths and a quicker victory are simply the logical thing to do.

```statblock
creature: "Kholo Pragmatist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
