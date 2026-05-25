---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Arbiter"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Diabolic, Empyrean, Utopian"
skills:
  - name: Skills
    desc: "Acrobatics +9, Diplomacy +6, Stealth +9, Axis Lore +5"
abilityMods: ["+1", "+4", "+2", "+0", "+2", "+1"]
abilities_top:
  - name: "Locate Aeon"
    desc: "An arbiter can always sense the direction of the nearest non-arbiter aeon on the plane, but it can't sense the range to the aeon."
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +7, **Will** +7"
health:
  - name: HP
    desc: "22; **Immunities** death effects, disease, emotion, poison, unconscious; **Resistances** electricity 3"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +7 (`pf2:1`) (agile, finesse, magical, reach 0 ft., versatile s), **Damage** 1d6+1 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]]<br>**1st** [[Command]], [[Mending]], [[Sanctuary]]"
abilities_bot:
  - name: "Electrical Burst"
    desc: "`pf2:2` The arbiter releases an electrical burst from its body that deals @Damage[3d6[electricity]|options:area-damage] damage to all creatures in a @Template[emanation|distance:10], with a DC 17 [[Reflex]] save. The arbiter is then [[Stunned]] for 24 hours."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These spherical aeons are scouts and diplomats. Found throughout the multiverse, they have traditionally kept watch over chaos and its agents. With the announcement of the Convergence, many arbiters now serve as go-betweens among the aeon alliance and its mortal associates.

Aeons have always been the caretakers of reality and defenders of the natural order of balance. Each type of aeon takes on some form of duality in its manifestation and works either to shape the multiverse within the aspects of this duality in some way, or to correct imbalances to the perfect order of existence. Aeons' machinations can raise a nation, raze it, or restore it from ruin. Their reasons are their own, and they rarely share their motivations with others—through their strange envisioning mode of communication, they simply create the results they insist are necessary to maintain the balance of the multiverse.

As a result of recent shifts in reality, aeons have begun to reassert a presence in the perfect planar city of Axis. To aeons, this is merely the latest in a recurring cycle, albeit one that mortals have not yet borne witness to. Aeons have a name for this cyclic return, in which they welcome their industrious axiomite brethren back to their fold: the Convergence. At the onset of the Convergence, a council of pleroma aeons appeared in the Eternal City of Axis, where they revealed that axiomites were wayward aeons, split off long ago to pursue the act of creation. With the latest cycle of change, it was time for axiomites—and their mortal creations and kin—to rejoin the aeon cause. While most axiomites fell in line, realizing perhaps on a fundamental level of reality that what the aeons said was the truth, some refused to heed the call and waited for the wrath of the aeons. That wrath has yet to come. The dual-natured aeons have responded to those who have declined in confusing ways. With some they treat and even bargain, while a handful of others they have destroyed, and a few have been exterminated by the axiomites. But most of these quiet insurgents they leave alone, allowing these axiomites to continue to create in peace. How—or if—this Convergence will end is as little understood as aeons themselves.

```statblock
creature: "Arbiter"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
