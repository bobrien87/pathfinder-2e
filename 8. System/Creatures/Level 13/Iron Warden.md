---
type: creature
group: ["Construct", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Iron Warden"
level: "13"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Construct"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +30"
abilityMods: ["+8", "-1", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Shield Arm"
    desc: "The iron warden has a shield built into its arm, that it can use as a steel shield (+2 to AC and Hardness 5). Because it's a part of the iron warden, all damage in excess of its Hardness is dealt only to the iron warden."
  - name: "Iron Warden Poison"
    desc: "Any drained value from this poison is reduced by 1 every hour <br>  <br> **Saving Throw** DC 33 [[Fortitude]] save; <br>  <br> **Maximum Duration** 4 rounds <br>  <br> **Stage 1** 2d6 poison and [[Drained]] 1 (1 round) <br>  <br> **Stage 2** 4d6 poison and [[Drained]] 2 (1 round) <br>  <br> **Stage 3** 8d6 poison and [[Drained]] 3 (1 round)"
armorclass:
  - name: AC
    desc: "33; **Fort** +26, **Ref** +19, **Will** +22"
health:
  - name: HP
    desc: "190; **Immunities** fire; **Resistances** physical 15 except adamantine"
abilities_mid:
  - name: "Shield Block"
    desc: "`pf2:r` **Trigger** The monster has its shield raised and takes damage from a physical attack. <br>  <br> **Effect** The monster snaps its shield into place to deflect a blow. The shield prevents the monster from taking an amount of damage up to the shield's Hardness. The monster and the shield each take any remaining damage, possibly breaking or destroying the shield."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +28 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 3d10+12 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Breath Poison"
    desc: "`pf2:2` The iron warden exhales poisonous gas in a @Template[burst|distance:10] centered on the corner of one of the iron warden's squares. The gas persists until the start of the warden's next turn. Any creature in the area (or that later enters the area) is exposed to the iron warden's poison. <br>  <br> The warden can't Breathe Poison again for 1d4 rounds."
  - name: "Inexorable March"
    desc: "`pf2:1` The iron warden Strides up to its Speed, pushing back each creature whose space it moves into and damaging them if they try to stop its movement. A creature can attempt to bar the way by succeeding at a DC 37 [[Fortitude]] save. On a critical success, the resisting creature takes no damage; otherwise, it's damaged as if hit by the iron warden's fist."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Traditionally crafted into the forms of giant suits of armor or powerful animals, iron wardens are products of exquisite artistry and skill. Their articulated joints and sturdy, armored bodies require great care and mathematical precision to craft, and regular cleaning and oiling ensure they don't rust over the ages. With proper care, iron wardens can remain in good shape for thousands of years, being passed down for generations, as long as they aren't destroyed by meddlesome adventurers. In addition to their incredible strength, iron wardens possess a potent toxic breath that is often more than enough to dispatch entire groups of opponents.

Though their impressive stature prevents them from being inconspicuous, iron wardens are often placed in areas where they are easily mistaken for decorative objects. An iron warden might be hidden among decorative suits of armor or disguised as a statue in a city square. Occasionally, locals are shocked when something they assumed to be a historic landmark animates into an iron warden, called to action by an unknown mystic command.

Stories tell of ancient civilizations, such as the Jistka Imperium, that created iron wardens of massive size. Most of these constructs have since been melted down for resources, but magicians and historians still chase down rumors of one of these lost colossi.

```statblock
creature: "Iron Warden"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
