---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dig-Widget"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]], [[Tremorsense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +9, Stealth +14, Thievery +15"
abilityMods: ["+2", "+5", "+1", "-5", "+0", "-5"]
abilities_top:
  - name: "Infiltration Tools"
    desc: "A dig-widget's face consists of a set of Infiltrator Thieves' Tools. They can be salvaged from a destroyed dig-widget with a successful DC 20 [[Crafting]] check. On a failed check, the tools are destroyed."
  - name: "Sneak Attack"
    desc: "A dig-widget's Strikes deal an additional 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "23; **Fort** +10, **Ref** +14, **Will** +7"
health:
  - name: HP
    desc: "65"
abilities_mid:
  - name: "Mechanical Vulnerability"
    desc: "A creature with expert proficiency in Thievery can attempt a check to `act disable-device dc=22` to damage a dig-widget. The DC is 22, and each success deals 20 untyped damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Drill +14 (`pf2:1`) (fatal d10, finesse), **Damage** 2d6+4 piercing plus 1d6 bleed"
  - name: "Melee strike"
    desc: "Corkscrew +14 (`pf2:1`) (finesse), **Damage** 2d8+4 piercing"
spellcasting: []
abilities_bot:
  - name: "Fastening Leap"
    desc: "`pf2:1` The dig-widget Leaps up 20 feet onto a creature or object and attempts a corkscrew Strike against it. If the Strike damages the target, the dig-widget attaches to the target (typically to the back of a creature). This is similar to [[Grabbing]] the creature, but the dig-widget moves with that creature rather than holding it in place. While attached, the dig-widget can't use its corkscrew. The dig-widget can be [[Shoved]] off, or it can detach itself with an Interact action."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Thieves covet dig-widgets, specialized constructs built for infiltration. Each dig-widget contains numerous simple tools, including a set of mechanical devices that function as thieves' tools, two arms with drills, and two arms with corkscrews for attaching to and climbing surfaces. Once activated, these devices propel themselves forward. Though they have the faculties typical of a construct, they usually follow a simple routine: avoid notice, pick any lock barring the path, dig past obstacles, and attack if caught. They're rarely left unattended, as a thief needs to be nearby to follow after—both to steal goods and to stop the dig-widget from engaging in further larceny once it's achieved its goal.

The source of a dig-widget's power is as much mechanical as it is magical. The gears and springs that provide a dig-widget mobility are an improvement over more primitive true clockwork creations (whose functions require constant winding to remain mobile), but at the cost of security, for a dig-widget's moving parts can be dismantled quickly by thieves and others with the proper training.

While many authorities ban dig-widgets, they have a harder time confiscating the machines than might be expected. A sizable number of people who encounter dig-widgets, from hired adventurers to tunneling kobolds, are far more inclined to keep the constructs for themselves than turn them over to be dismantled. Often, this is simply due to the novelty of the dig-widget rather than any desire to use it.

```statblock
creature: "Dig-Widget"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
