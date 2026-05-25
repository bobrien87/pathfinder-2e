---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pipefox"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]]"
languages: "Common, Draconic (Translate)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Arcana +9, Athletics +7, Occultism +9, Society +9, Stealth +8"
abilityMods: ["+3", "+4", "+3", "+4", "+1", "+3"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Master of Tongues"
    desc: "Even if the pipefox does not speak a creature's language, it can rapidly pick up on inflection, root words, and body language. If the pipefox interacts or observes a creature for at least 10 minutes and that creature can speak a language, it can communicate basic concepts to that creature."
armorclass:
  - name: AC
    desc: "19; **Fort** +8, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "30"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (finesse, reach 0 ft., unarmed), **Damage** 1d6+4 piercing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 18, attack +8<br>**2nd** [[Invisibility (At Will, Self Only)]], [[Translate]] (Constant)<br>**1st** [[Read Aura]]"
abilities_bot:
  - name: "Rapid Erudition"
    desc: "`pf2:1` **Requirements** The pipefox saw a cantrip cast within the last minute; <br>  <br> **Effect** The pipefox can cast the cantrip it saw as an innate arcane spell for 1 minute."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Pipefoxes are small, fluffy snakes with the head of a fox. They spend their days lurking in dark corners, hanging from trees, coiled around pipes, or otherwise lounging anywhere they can observe something interesting in peace and quiet. Pipefoxes are neither pests nor pets; they simply skulk around, acquiring knowledge and searching for a worthy scholar to disseminate their observations to.

Pipefoxes are as intense as they are capricious with their fixations. One might study blacksmithing for six months before suddenly switching their entire attention to studying the slang used by a group of local thieves, or the gossip of servants behind their employer's back. Regardless of the topic, they always study from a distance lest the object of their observation alter their behaviors. If a pipefox is discovered, they usually attempt to flee, only fighting as a last resort.

Pipefoxes view their knowledge as a form of currency that they protect at all costs. Because of this, they are secretive by nature. If they choose to reveal themselves to someone, it will be after much study and consideration. A pipefox will only approach someone they believe to be as invested in the pursuit of knowledge as they are. They are most attracted to spellcasters, alchemists, and inventors for this reason. However, while a pipefox may choose to approach and share what they know, they never do so freely. Like all currencies, knowledge must be equally exchanged.

Many scholars believe pipefoxes to be spirits and keepers of knowledge; in the event of a massive cataclysm, pipefoxes will be able to return lost knowledge to the world, preventing great dark ages. For this reason, many institutions of knowledge are aware of the spying of pipefoxes but pretend not to notice and prevent others from discovering them. This encourages pipefoxes to stay while also providing a backup cache of important knowledge in the form of a small, fluffy snake.

```statblock
creature: "Pipefox"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
