---
type: creature
group: ["Humanoid", "Kholo"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bone Scavenger"
level: "0"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Kholo"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: "Common, Kholo"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +2, Deception +4, Stealth +6, Survival +4"
abilityMods: ["+2", "+3", "+1", "-1", "+1", "+0"]
abilities_top:
  - name: "Rugged Travel"
    desc: "A kholo ignores the first square of difficult terrain they move into each time they Step or Stride."
armorclass:
  - name: AC
    desc: "16; **Fort** +3, **Ref** +6, **Will** +3"
health:
  - name: HP
    desc: "16"
abilities_mid:
  - name: "Bone Armor"
    desc: "`pf2:r` **Trigger** The bone scavenger takes bludgeoning damage <br>  <br> **Effect** The bone scavenger angles their makeshift armor to absorb some of the blow, causing shards of bone to splinter outward. All adjacent creatures take @Damage[2d4[piercing]|options:area-damage] damage (DC 16 [[Reflex]] save)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Dagger +6 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+2 piercing"
  - name: "Melee strike"
    desc: "Jaws +5 (`pf2:1`) (unarmed), **Damage** 1d6+2 piercing"
spellcasting: []
abilities_bot: []
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Kholos have a strong connection to their ancestors, often using their bones as art and weapons to further honor them. Bone scavengers are sent to the fields after a battle to collect the bones of their fellow allies. They often eschew the pack hunting techniques of other kholos, spreading out among their foes when encountered in groups.

These pragmatic hunters have earned a very poor reputation for their brutality in battle and worship of demons. While many kholos live up to the terrible stories of their ferocity and cannibalism, others are scavengers and trappers just trying to get by. Many of their cultural traditions are misunderstood by other ancestries, and some kholos play into the fear provoked in those who believe the twisted tales about their people. Kholos are often criticized for their lack of honor in battle, but a kholo understands honor doesn't bring you back home alive, nor does honor put food on the table. Ambushes, feints, and deceptions that lead to fewer kholo deaths and a quicker victory are simply the logical thing to do.

```statblock
creature: "Bone Scavenger"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
