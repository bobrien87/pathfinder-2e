---
type: creature
group: ["Clockwork", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Clockwork Spy"
level: "-1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +5"
abilityMods: ["-1", "+3", "+0", "-5", "+2", "+0"]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, [[Thievery]] check, standby <br>  <br> For a clockwork to act, it must be wound with a unique key by another creature. This takes 1 minute. Once wound, it remains operational for the listed amount of time, usually 24 hours, after which time it becomes unaware of its surroundings and can't act until it's wound again. Some clockworks' abilities require them to spend some of their remaining operational time. They can't spend more than they have and shut down immediately once they have 0 time remaining. If it's unclear when a clockwork was last wound, most clockwork keepers wind all their clockworks at a set time, typically 8 a.m. <br>  <br> A clockwork that lists standby in its wind-up entry can enter standby mode as a 3-action activity. Its operational time doesn't decrease in standby, but it can sense its surroundings (with a -2 penalty to Perception). It can't act, with one exception: when it perceives a creature, it can exit standby as a reaction (rolling initiative if appropriate). <br>  <br> A creature can attempt to [[Disable a Device]] to wind a clockwork down (with a DC listed in the wind-up entry). For each success, the clockwork loses 1 hour of operational time. This can be done even if the clockwork is in standby mode."
armorclass:
  - name: AC
    desc: "17; **Fort** +2, **Ref** +7, **Will** +4"
health:
  - name: HP
    desc: "8; **Weaknesses** electricity 2, orichalcum 2"
abilities_mid:
  - name: "Self-Destruct"
    desc: "`pf2:r` A clockwork spy must use this reaction unless specifically programmed otherwise by its creator. <br>  <br> **Trigger** The clockwork spy is reduced to 0 Hit Points. <br>  <br> **Effect** The spy thrashes around and emits a tinny scream followed by a steady ticking sound. At the beginning of what would have been its next turn, the clockwork spy explodes, dealing @Damage[1d10[piercing]|options:area-damage] damage in a @Template[emanation|distance:5]{5-foot radius} (DC 16 [[Reflex]] save). Its gemstone is destroyed, along with any information contained inside it. <br>  <br> An adjacent creature can cancel the self-destruct sequence by succeeding at a DC 16 [[Thievery]] check to [[Disable a Device]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Spherical Body +7 (`pf2:1`) (finesse), **Damage** 1d6-1 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Record Audio"
    desc: "`pf2:1` The clockwork spy records all sounds within @Template[emanation|distance:25]{25 feet} onto a small gemstone worth 1 gp embedded in its body. The clockwork spy can record up to 1 hour of sound on a single gemstone. Once it begins recording, it can't cease recording early, nor can it record onto a gemstone that already contains a recording. Some clockwork spies contain multiple gemstones to allow for a series of recordings. Since clockwork spies are not intelligent, they must be given simple commands regarding when to start recording sounds. A clockwork spy can differentiate between different kinds of creatures but not between specific individuals. <br>  <br> The spy can start or stop playback of recorded sound by spending a single action. Removing a gemstone from or installing a gemstone into a clockwork spy requires a successful DC 14 Thievery check to [[Disable a Device]]; on a failure, the gemstone is undamaged, but any recorded sounds are erased and the gemstone still can't be used to make another recording."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Engineers, technologists, and mechanically gifted wizards employ clockwork spies-tiny, spiderlike constructs capable of recording and playing back audio-to surreptitiously surveil their enemies or steal secrets from competitors. Their spindly bodies and delicate components make them unsuitable for combat; in fact, most builders construct clockwork spies with a self-destruct mechanism to ensure the spies' meddling can't be traced back to them.

Intricate, complex machines, clockworks are built with care by highly skilled engineers. Though their creation involves some amount of magic, they're primarily mechanical, packed with precision-tuned gears and springs working in concert.

The sturdy mainspring within a clockwork must be wound to provide the energy needed to power the device. Some larger clockworks contain a series of springs for different limbs that each need to be wound. A clockwork's crafter creates a unique metal key while building the clockwork; winding the clockwork usually involves inserting the key into the machine's back and turning clockwise. Larger clockworks require greater strength to turn the key, and typically have larger keys to allow for more torque-some even accommodating a team of winders rather than an individual. Programming a clockwork requires both the key and the knowledge to set the program correctly, information usually reserved for the clockwork's creator or owner.

```statblock
creature: "Clockwork Spy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
