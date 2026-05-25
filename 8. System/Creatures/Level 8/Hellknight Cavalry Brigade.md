---
type: creature
group: ["Animal", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hellknight Cavalry Brigade"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: "Troop"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16"
languages: "Common, Diabolic"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +18, Intimidation +17, Religion +12, Society +12, Hell Lore +12"
abilityMods: ["+7", "+1", "+4", "+2", "+2", "+3"]
abilities_top:
  - name: "Trailblazing Stride"
    desc: "While moving on land, the Hellknight cavalry brigade ignores difficult terrain."
armorclass:
  - name: AC
    desc: "27; **Fort** +18, **Ref** +13, **Will** +16"
health:
  - name: HP
    desc: "135; troop defenses; **Weaknesses** area damage 8, splash damage 8; **Resistances** mental 5, slashing 5"
abilities_mid:
  - name: "Mounted Troop"
    desc: "Effects that target only animals or only humanoids might not work on the Hellknight cavalry brigade, subject to the GM's discretion."
  - name: "Troop Defenses"
    desc: "**Thresholds** 90 (3 segments), 45 (2 segments) <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Arrow Volley"
    desc: "`pf2:2` The Hellknights draw or reload their longbows, then launch a ranged attack in the form of a volley. This volley is a @Template[type:burst|distance:10] within 100 feet that deals @Damage[3d8[piercing]|options:area-damage] damage (DC 23 [[Reflex]] save). When the troop is reduced to 2 or fewer segments, this area decreases to a @Template[type:burst|distance:5]."
  - name: "Lance Charge"
    desc: "`pf2:3` The brigade Strides twice with a +10-foot circumstance bonus to its Speed. If it moves at least 10 feet, the brigade deals @Damage[(3d8+14)[piercing]|options:area-damage] damage with a DC 26 [[Reflex]] save to each enemy in a @Template[type:emanation|distance:10] at the end of its movement."
  - name: "Stab from the Saddle"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The brigade engages in a coordinated lance attack against each enemy in a @Template[type:emanation|distance:10] with a DC 23 [[Reflex]] save. The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[(1d6+3)[piercing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(2d6+10)[piercing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(3d6+14)[piercing]|options:area-damage] damage"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A Hellknight cavalry brigade consists of several Hellknights and a single field-maralictor, all wearing the distinctive armor of their order and wielding lances. The maralictor speaks for the brigade, questioning travelers the brigade encounters and barking orders. A Hellknight brigade is typically based at a keep or other fortification controlling an area measured by a day's ride in every direction—about 25 miles. Farther-ranging missions are possible but require substantial logistical support.

A military serves to defend and fight on behalf of nations and can be trained and deployed in various ways.

```statblock
creature: "Hellknight Cavalry Brigade"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
