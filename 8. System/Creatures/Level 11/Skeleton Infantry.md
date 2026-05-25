---
type: creature
group: ["Mindless", "Skeleton"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Skeleton Infantry"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Mindless"
trait_02: "Skeleton"
trait_03: "Troop"
trait_04: "Undead"
trait_05: "Unholy"
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18"
abilityMods: ["+5", "+3", "+4", "-5", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "31; **Fort** +21, **Ref** +18, **Will** +19"
health:
  - name: HP
    desc: "180; troop defenses; **Immunities** bleed, death effects, disease, mental, paralyzed, poison, unconscious; **Weaknesses** area damage 10, splash damage 10; **Resistances** cold 5, electricity 5, fire 5, piercing 10, slashing 10"
abilities_mid:
  - name: "Form a Phalanx"
    desc: "`pf2:1` Many of the skeletons raise their shields to protect others. The infantry gain a +2 circumstance bonus to AC until the start of their next turn."
  - name: "Troop Defenses"
    desc: "**HP** 180 (4 segments); **Thresholds** 120 (3 segments), 60 (2 segments); <br>  <br> Troops are composed of many individuals, represented by four \"segments\" on a battle grid. Each segment is 10 feet on each side and as tall as the individual members of the troop. Segments must remain contiguous. Each one has to share at least 5 feet of one of its edges with another segment—being adjacent on a diagonal isn't sufficient! You can measure flanking, cover, and the like using the center of any segment. <br>  <br> A troop has two Hit Point thresholds in its HP entry and loses segments as it crosses thresholds. Typically, the higher threshold is at 2/3 of the troop's maximum Hit Points and the lower is at 1/3 of its maximum. Once the troop drops below the higher threshold, it loses one segment, leaving three segments (12 squares) remaining and setting the first threshold as the troop's new maximum Hit Points. This repeats when the troop drops below the lower threshold, leaving two segments (8 squares). At 0 Hit Points, the troop disperses entirely, with the few remaining members surrendering, [[Fleeing]], or easily dispatched, as determined by the GM. Typically the creature who caused the troop to lose a segment decides which to remove, or the GM decides when a specific creature wasn't responsible. To restore lost segments and maximum Hit Points, a troop needs to spend downtime to use long-term treatment on casualties or recruit new members to replace the fallen. <br>  <br> Troops are typically immune to non-damaging effects that target a single creature, such as a [[Charm]] spell or the [[Demoralize]] action. An ability that can target 5 or more creatures can target an entire segment, increasing to two segments if it can target 10 or more creatures and to the entire troop if it can target 20 or more creatures. An ability that affects all creatures in a certain range affects all segments in range (make any checks or saves separately for each segment). As examples, an 8th rank *charm* spell (with 10 targets) can affect two segments, and an ability that Demoralizes all creatures within 30 feet of you would affect all segments that are fully within that range. A non-damaging ability that would prevent a segment from acting, cause them to flee, or otherwise make them unable to function as part of the troop for a round or more removes the segment entirely. The troop loses a number of HP required to bring it to the next threshold. If an ability both deals damage and has a non-damaging effect, apply the damage then the rest of the effect."
  - name: "Troop Movement"
    desc: "Whenever a troop moves, you move one of its segments and the other segments follow behind it. At the end of the movement, you can group the other segments adjacent to the one you moved as you see fit, provided none of them moves farther than the moving segment. If you choose not to move the troop any distance, you can instead reshape the position of all the segments as long as one stays in place."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Hurl Javelins!"
    desc: "`pf2:2` The troop's members throw a volley of javelins. Each creature in a @Template[type:burst|distance:10] within 30 feet of the troop takes @Damage[(2d6+10)[piercing]|options:area-damage] damage (DC 27 [[Reflex]] save). When the troop is reduced to 2 segments, this area decreases to a @Template[type:burst|distance:5]."
  - name: "Lower Spears!"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Frequency** once per round <br>  <br> **Effect** The skeletons engage in a coordinated longspear attack against each enemy within @Template[emanation|distance:10]{10 feet} (DC 27 [[Reflex]] save). The damage depends on the number of actions. <br>  <br> `pf2:1` @Damage[2d8[piercing]|options:area-damage] damage <br>  <br> `pf2:2` @Damage[(3d8+7)[piercing]|options:area-damage] damage <br>  <br> `pf2:3` @Damage[(4d8+7)[piercing]|options:area-damage] damage"
  - name: "Phalanx Charge"
    desc: "`pf2:2` **Requirements** The infantry is in a phalanx <br>  <br> **Effect** The skeletons lower their longspears and charge. The troop Strides in a straight line until they're adjacent to an enemy then use Lower Spears!, dealing @Damage[(3d8+7)[piercing]] damage. Any creature that fails its save is also knocked [[Prone]]."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

This troop of skeletons was once a cohort of highly disciplined spear-and-shield infantry from an ancient empire.

Almost any creature that had bones in life and leaves them behind in death can become a shambling, undead skeleton-humanoids, beasts, aberrations, fey, and more.

```statblock
creature: "Skeleton Infantry"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
