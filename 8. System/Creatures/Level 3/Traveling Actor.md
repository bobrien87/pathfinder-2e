---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Traveling Actor"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12"
languages: "Common (up to 4 other languages)"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +7, Deception +10, Performance +10, Society +9, Theater Lore +9"
abilityMods: ["+2", "+3", "+0", "+1", "+1", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Dramatic Death"
    desc: "`pf2:r` **Trigger** The traveling actor takes any damage <br>  <br> **Effect** The traveling actor falls [[Prone]] and dramatically announces their death. They appear to have died. Anyone who is suspicious of this \"death\" can [[Seek]] to attempt a secret [[Perception]] check against the traveling actor's Performance DC. On a success, they see through the ruse."
  - name: "Versatile Performance"
    desc: "The traveling actor can use Performance instead of Diplomacy to `act make-an-impression statistic=performance` and instead of Intimidation to `act demoralize statistic=performance`."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Wooden Sword +12 (`pf2:1`) (agile, finesse, shove), **Damage** 1d4+6 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Overacted Strike"
    desc: "`pf2:2` The traveling actor puts all their expertise into an attack that strikes fear in those who witness it. The traveling actor Strikes. On a success, the traveling actor chooses another creature within 30 feet who can see the attack, who becomes [[Frightened]] 1 (or [[Frightened]] 2 on a critical success)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The life of a traveling actor is, contrary to belief, not one of glamor but effort. To be on the road going from town to town wearing a thousand faces invites little reward, save the adoration of the crowd. Even so, this is where they thrive. Actors typically travel in troupes, composed not only of other actors but also of stagehands, drivers, and assorted hangers-on. All of them fall under the thumb of a singular director, acting as both parent and manager to all within the troupe.

Performances come in a wide variety of forms, from musical methods like singing and instruments to physical dancing and juggling to simple orating and conversing.

```statblock
creature: "Traveling Actor"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
