---
type: creature
group: ["Humanoid", "Titan"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elysian Titan"
level: "21"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Humanoid"
trait_02: "Titan"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Common, Empyrean (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +36, Athletics +43, Crafting +37, Diplomacy +37, Intimidation +35, Religion +37, Survival +37"
abilityMods: ["+10", "+7", "+8", "+6", "+8", "+6"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "46; **Fort** +37, **Ref** +34, **Will** +35"
health:
  - name: HP
    desc: "400; **Immunities** death effects, disease"
abilities_mid:
  - name: "+4 Status to All Saves vs. Mental"
    desc: ""
  - name: "Impossible Stature"
    desc: "100 feet. Titans warp perception and distance around them to seem even larger and more imposing. A creature that enters or begins its turn within the emanation must succeed at a DC 44 [[Will]] save or its movement toward the titan is movement over difficult terrain (greater difficult terrain on a critical failure) for 1 round."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Greatpick +41 (`pf2:1`) (fatal d12, magical, reach 15 ft.), **Damage** 4d10+20 piercing"
  - name: "Melee strike"
    desc: "Fist +38 (`pf2:1`) (agile, reach 30 ft.), **Damage** 4d8+20 bludgeoning"
  - name: "Ranged strike"
    desc: "Piercing Flash +35 (`pf2:1`) (agile, fire, light, magical, range 200 ft.), **Damage** 2d10 fire plus 3d12+10 piercing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 44, attack +36<br>**10th** [[Revival]]<br>**9th** [[Falling Stars]]<br>**7th** [[Interplanar Teleport]] (At Will)<br>**6th** [[Scrying]], [[Truesight]] (Constant)<br>**5th** [[Sending]]<br>**4th** [[Unfettered Movement]] (At Will)<br>**2nd** [[Dispel Magic]] (At Will)"
abilities_bot:
  - name: "Titanic Grasp"
    desc: "`pf2:1` The titan makes a fist Strike against a creature affected by their impossible stature, even if it's outside of the titan's normal reach. On a hit, the titan automatically [[Grab|Grabs]] the creature and, if out of their reach, pulls it within reach."
  - name: "Wide Cleave"
    desc: "`pf2:2` The titan makes a melee weapon Strike against each foe within their reach. This counts as three attacks for the titan's multiple attack penalty, but the penalty doesn't increase until all attacks have been made."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Those titans who remained true to their creators, refusing to participate in their peers' rebellion, earned their freedom while the others were imprisoned. Many Elysian titans train aspiring champions of freedom, sacrifice, and selflessness.

Created by ancient deities long before the rise of mortal ancestries, titans united and attempted to overthrow their deific progenitors. The resulting war still figures prominently throughout mortal myths, in which most titans were cast down and imprisoned for eons.

```statblock
creature: "Elysian Titan"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
